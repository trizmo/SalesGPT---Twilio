# lib/text_to_speech.py

from gtts import gTTS
import os
from twilio.rest import Client

# Twilio credentials
account_sid = os.getenv("TWILIO_ACCOUNT_SID", "")
auth_token = os.getenv("TWILIO_AUTH_TOKEN", "")
client = Client(account_sid, auth_token)

def text_to_speech(text, output_filename):
    if os.path.exists(output_filename):
        os.remove(output_filename)
        print(f"Deleted {output_filename}")
        
    tts = gTTS(text=text, lang='en')
    tts.save(output_filename)

    print(f"Saved spoken text to {output_filename}")