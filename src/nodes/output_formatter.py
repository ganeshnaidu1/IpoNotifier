from src.state.state import state

class OutputFormatter:
    def __init__(self, llm):
        self.llm = llm

    def format_output(self, state: state):
        prompt = f"""
        You are a helpful assistant that specializes in Indian IPO analysis. You have all the information about indian IPOs closing today format the message into a small whatsapp message so that i can draw clear insights from that to buy or not buy the ipo with GMP mentioned in the {state["output"]}"""
        state["formatted_output"] = self.llm.invoke(prompt)
        return state