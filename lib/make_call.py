from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

# Twilio credentials
account_sid = os.getenv("TWILIO_ACCOUNT_SID", "")
auth_token = os.getenv("TWILIO_AUTH_TOKEN", "")
print(f"Account SID: {account_sid}")
print(f"Auth Token: {auth_token}")

client = Client(account_sid, auth_token)

# Get Base URL
BASE_URL = os.getenv("BASE_URL_NGROK")

# The URL for Twilio to request when the call is answered
# This should be a publicly accessible URL where you host your instructions (TwiML) for the call
answer_url =  BASE_URL + '/answered_call'

def make_call(phone_number):
    # Make the call
    call = client.calls.create(
        to=phone_number,  # The phone number to call
        from_=os.getenv("TWILIO_PHONE_NUMBER", ""),  # Your Twilio phone number
        url=answer_url  # The URL Twilio will request when the call is answered
    )

    print(f"Call initiated, SID: {call.sid}")