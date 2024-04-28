import requests
import os
from twilio.rest import Client

api_key = os.getenv("ELEVENLABS_API_KEY", "")

# Twilio credentials
account_sid = os.getenv("TWILIO_ACCOUNT_SID", "")
auth_token = os.getenv("TWILIO_AUTH_TOKEN", "")

johnny_voice_id = "lO13rwEA0kJZxoDihEmQ"
sally_voice_id = "QN4adxZqLZhkZgz3VKyS"
santa_voice_id = "Gqe8GJJLg3haJkTwYj2L"
wesley_voice_id = "GduC2RjzvNKCozZY5lPD"
david_voice_id = "y1adqrqs4jNaANXsIZnD"
jameson_voice_id = "Mu5jxyqZOLIGltFpfalg"
natasha_voice_id = "lNXoiG0t150DtDjGdo2y"

client = Client(account_sid, auth_token)


def eleven_speech(text, output_filename):
    url = "https://api.elevenlabs.io/v1/text-to-speech/" + natasha_voice_id

    headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": api_key
    }

    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.request("POST", url, json=data, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # save the audio file and upload to twilio
        # with open(output_filename, 'wb') as audio_file:
        #     audio_file.write(response.content)
        #     asset = client.assets.create(
        #         friendly_name='speech_file',
        #         file_path=output_filename
        #     )
        # # Print the asset's URL
        # print("-----")
        # print("-----")
        # print("-----")
        # print("-----")
        # print(asset.url)
        # print(asset.url)
        # print(asset.url)
        # print("-----")
        # print("-----")
        # print("-----")
        # print("-----")



        # Write the binary content of the response to a file
        with open(output_filename, 'wb') as audio_file:
            audio_file.write(response.content)
        print(f"Audio content saved to {output_filename}")



    else:
        print(f"Failed to convert text to speech. Status code: {response.status_code}")
        print(response.text)