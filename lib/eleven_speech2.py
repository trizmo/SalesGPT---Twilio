import requests
import os

from elevenlabs import play, Voice, VoiceSettings, save
from lib.eleven_client import client  # Import the globally initialized client

api_key = os.getenv("ELEVENLABS_API_KEY", "")

johnny_voice_id = "lO13rwEA0kJZxoDihEmQ"
sally_voice_id = "QN4adxZqLZhkZgz3VKyS"
santa_voice_id = "Gqe8GJJLg3haJkTwYj2L"
wesley_voice_id = "GduC2RjzvNKCozZY5lPD"
david_voice_id = "y1adqrqs4jNaANXsIZnD"
jameson_voice_id = "Mu5jxyqZOLIGltFpfalg"
natasha_voice_id = "lNXoiG0t150DtDjGdo2y"

def eleven_speech(text, output_filename):

    audio = client.generate(
        text=text,
        voice=Voice(
            voice_id=natasha_voice_id,
            settings=VoiceSettings(stability=0.35, similarity_boost=0.45, style=0.0, use_speaker_boost=True)
        )
    )

    save(audio, output_filename)