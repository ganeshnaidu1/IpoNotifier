from fastapi import FastAPI
import uvicorn
from fastapi import Request
from src.graph.graph_builder import GraphBuilder
from src.llms.GroqLlm import GroqLlm
app = FastAPI()

@app.get("/")
async def root():
    ll = GroqLlm()
    llm = ll.get_llm()
    graph = GraphBuilder(llm)
    graph = graph.build_graph()
    result = graph.invoke({})  # Pass empty dict as initial state
    return {"message": result["formatted_output"].content}





if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)