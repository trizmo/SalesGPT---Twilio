import speech_recognition as sr

def speech_to_text():
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Using the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust the recognizer sensitivity to ambient noise and record audio
        r.adjust_for_ambient_noise(source, duration=1)
        # Listen for the first phrase and extract it into audio data, stopping if 3 seconds of silence are observed
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=3)
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            return ""  # Return an empty string if no speech is detected

    # Recognize speech using Google Web Speech API
    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        print(f"Transcription: {text}")
        return text
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")

    return ""  # Return an empty string if an error occurs
