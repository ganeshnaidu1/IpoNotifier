import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

class TwilioService:
    def __init__(self):
        self.account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.from_number = os.getenv('TWILIO_FROM_NUMBER')  # Your Twilio WhatsApp number
        self.to_number = os.getenv('TWILIO_TO_NUMBER')      # Your WhatsApp number
        
        if not all([self.account_sid, self.auth_token, self.from_number, self.to_number]):
            raise ValueError("Missing Twilio environment variables")
            
        self.client = Client(self.account_sid, self.auth_token)
    
    def send_whatsapp_message(self, message):
        """Send WhatsApp message via Twilio"""
        try:
            message = self.client.messages.create(
                from_=f'whatsapp:{self.from_number}',
                body=message,
                to=f'whatsapp:{self.to_number}'
            )
            print(f"WhatsApp message sent successfully! SID: {message.sid}")
            return True
        except Exception as e:
            print(f"Error sending WhatsApp message: {str(e)}")
            return False 