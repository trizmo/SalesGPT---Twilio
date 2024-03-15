import json
import os

def save_speech_input(speech_text):
    # Remove file if it exists
    if os.path.exists('speech_inputs.txt'):
        os.remove('speech_inputs.txt')

    file_path = 'speech_inputs.txt'
    # Open the file in write mode ('w') which will create the file if it doesn't exist
    # or overwrite it if it does exist.
    with open(file_path, 'w') as file:
        file.write(speech_text)

def retrieve_speech_input():
    file_path = 'speech_inputs.txt'
    try:
        with open(file_path, 'r') as file:
            # Read the entire content of the file as a string
            speech_text = file.read()
            return speech_text
    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        print("File not found.")
        return None
