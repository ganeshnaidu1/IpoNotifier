from fastapi import FastAPI
import uvicorn
from fastapi import Request
from src.graph.graph_builder import GraphBuilder
from src.llms.GroqLlm import GroqLlm
from src.services.twilio_service import TwilioService
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/")
async def root():
    # Get current time in Indian Standard Time
    ist = pytz.timezone('Asia/Kolkata')
    now = datetime.now(ist)
    weekday = now.weekday()  # Monday=0, Sunday=6
    current_time = now.strftime("%H:%M")
     # Only run on weekdays (Monday=0 to Friday=4) between 12:00 PM and 4:00 PM
    if weekday < 5 and "12:00" <= current_time <= "16:00":
        try:
            # Run IPO analysis
            ll = GroqLlm()
            llm = ll.get_llm()
            graph = GraphBuilder(llm)
            graph = graph.build_graph()
            result = graph.invoke({})
            message = result["formatted_output"].content
            
            # Send WhatsApp message
            twilio_service = TwilioService()
            twilio_service.send_whatsapp_message(message)
            
            return {"message": message, "whatsapp_sent": True}
        except Exception as e:
            return {"message": f"Error: {str(e)}", "whatsapp_sent": False}
    else:
        return {"message": f"Analysis only runs on weekdays between 12:00 PM and 4:00 PM. Current time: {now.strftime('%A, %H:%M')}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 