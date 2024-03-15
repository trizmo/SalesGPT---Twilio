import time
from lib.speech_inputs import retrieve_speech_input

def wait_for_speech_input(timeout=10):
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        text_input = retrieve_speech_input()
        if text_input:  # Checks if text_input is not None and not an empty string
            print(f"Retrieved speech input: {text_input}")
            return text_input
        elif elapsed_time >= timeout:
            print("Timeout waiting for speech input.")
            return ""
        else:
            time.sleep(1)  # Wait for a second before checking again

