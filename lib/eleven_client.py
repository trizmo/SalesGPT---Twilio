import os
from elevenlabs.client import ElevenLabs

# Assuming you've already set your ELEVENLABS_API_KEY in your environment
api_key = os.getenv("ELEVENLABS_API_KEY", "")

# Initialize the ElevenLabs client globally
client = ElevenLabs(api_key=api_key)