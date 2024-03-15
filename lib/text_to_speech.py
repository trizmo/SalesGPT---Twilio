# lib/text_to_speech.py

from gtts import gTTS
import os

def text_to_speech(text, output_filename):
    if os.path.exists(output_filename):
        os.remove(output_filename)
        print(f"Deleted {output_filename}")
        
    tts = gTTS(text=text, lang='en')
    tts.save(output_filename)
    print(f"Saved spoken text to {output_filename}")
