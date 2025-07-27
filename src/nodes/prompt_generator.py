from src.state.state import state
from datetime import datetime

class PromptGenerator:
    def __init__(self):
        pass

    def generate_prompt(self, state: state):
        """
        Generate a prompt to identify Indian IPOs closing today with GMP above 10%
        """
        today = datetime.now().strftime("%Y-%m-%d")
        
        prompt = f"""
        You are a helpful assistant that specializes in Indian IPO analysis. 
        
        Today's date is: {today}
        
        Please identify all Indian IPOs that are closing on ({today}) and have a Grey Market Premium (GMP) of above 10%.
        
        For each IPO found, provide the following information:
        1. Company name
        2. IPO issue size
        3. Current GMP percentage
        4. Closing date
        5. Price band
        6. Any notable details about the IPO
        
        If no IPOs are closing today with GMP above 10%, please state that clearly.
        
        Please provide accurate and up-to-date information based on the current market data.
        """
        
        state["prompt"] = prompt
        return state
