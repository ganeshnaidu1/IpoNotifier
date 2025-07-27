import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
class GroqLlm:
    def __init__(self):
        os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
        self.llm=ChatGroq(model="llama3-8b-8192")

    def get_llm(self):
        return self.llm