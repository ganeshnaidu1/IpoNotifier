from fastapi import FastAPI
import uvicorn
from fastapi import Request
from src.graph.graph_builder import GraphBuilder
from src.llms.GroqLlm import GroqLlm
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
    # Only run on weekdays (Monday=0 to Friday=4) at 12:00 PM
    if weekday < 5 and current_time == "12:00":
        ll = GroqLlm()
        llm = ll.get_llm()
        graph = GraphBuilder(llm)
        graph = graph.build_graph()
        result = graph.invoke({})
        
        return {"message": result["formatted_output"].content}
    else:
        return {"message": f"Analysis only runs on weekdays at 12:00 PM. Current time: {now.strftime('%A, %H:%M')}"}





if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)