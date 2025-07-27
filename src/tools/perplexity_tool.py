import os
from langchain_core.tools import tool
from langchain_perplexity import ChatPerplexity
from src.state.state import state
class PerplexityTool:
    def __init__(self,state:state):
        self.perplexity_api_key=os.getenv("PERPLEXITY_API_KEY")
        self.state=state
        self.perplexity=ChatPerplexity(api_key=self.perplexity_api_key,model="sonar")

    def get_open_ipos(self, state: state):
        state["output"] = self.perplexity.invoke(state["prompt"])
        return state
        