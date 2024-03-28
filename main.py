from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse, Gather, Stream, Start
from lib.make_call import make_call
from run import process_call
import threading, os, time
from lib.process_speech_input import process_speech_input
from queue import Queue
from lib.speech_inputs import save_speech_input
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Assuming this is a global or shared queue where webhook handlers enqueue speech inputs
speech_inputs = Queue()

# Get Base URL
BASE_URL = os.getenv("BASE_URL_NGROK")

voice = 'Polly.Salli-Neural'

def handle_speech_input():
    while True:
        speech_text = speech_inputs.get()  # Wait for and get speech input from the queue
        if speech_text == "<END>":  # Assuming a way to signal the end of the session
            break
        processed_input = process_speech_input(speech_text)
        # Now, do something with processed_input, like feeding it to sales_agent
        print("Processed input:", processed_input)

# Url to Initiate the call to the user. Make a get request to /make_call
# with the phone_number as a query parameter
# Example: https://cda6-47-151-56-38.ngrok-free.app/make_call?phone_number=+15555555555
@app.route("/make_call", methods=['GET'])
def initiate_call():
    phone_number = request.args.get('phone_number')
    # Initialize the call
    make_call(phone_number)
    return "<h1>Making call...</h1>"

# Url to handle the user input. When the call is answered Twilio will make a post request to /answered_call
@app.route("/answered_call", methods=['POST'])
def answered_call():
    file_path = "output_text.txt"
    print(" ----- answered_call -----")
    # delete the file if it exists
    if os.path.exists(file_path):
        os.remove(file_path)

    # Create a thread to run process_call in the background
    thread = threading.Thread(target=process_call, args=(True, True, 'examples/endline_rep.json'))
    thread.start()
    print("Answered call. Starting SalesGPT. ::")

    # Wait for the MP3 file to be generated
    timeout = 30  # Maximum wait time in seconds
    start_time = time.time()

    while not os.path.exists(file_path) and (time.time() - start_time) < timeout:
        print('Waiting for text file to generate...')
        time.sleep(1)  # Wait 1 second before checking again

    response = VoiceResponse()

    # pause for 3 seconds
    response.pause(length=3)

    if os.path.exists(file_path):
        # get text from file
        with open(file_path, 'r') as file:
            text = file.read()

        # File is ready, play the MP3 and gather user response
        response.say(text, voice=voice)

        # Send the user to gather input
        response.redirect(url='/gather_input')

    else:
        # File wasn't generated in time, handle the error case
        response.say("Error 1. We are experiencing technical difficulties. Please try again later.")

    return str(response)
# def answered_call():
#     file_path = "static/audio/output.mp3"
#     print(" ----- answered_call -----")
#     # delete the file if it exists
#     if os.path.exists(file_path):
#         os.remove(file_path)

#     # Create a thread to run process_call in the background
#     thread = threading.Thread(target=process_call, args=(True, True, 'examples/endline_rep.json'))
#     thread.start()
#     print("Answered call. Starting SalesGPT. ::")

#     # Wait for the MP3 file to be generated
#     timeout = 30  # Maximum wait time in seconds
#     start_time = time.time()

#     while not os.path.exists(file_path) and (time.time() - start_time) < timeout:
#         print('Waiting for MP3 file to be generated...')
#         time.sleep(1)  # Wait 1 second before checking again

#     response = VoiceResponse()

#     if os.path.exists(file_path):
#         # get length of audio
#         audio_length = 0
#         audio_length = os.path.getsize(file_path)
#         audio_length = audio_length / 1000
#         print(f" -- Audio length: {audio_length} seconds")

#         # File is ready, play the MP3 and gather user response
#         response.play(url= BASE_URL + "/static/audio/output.mp3")

#         # Send the user to gather input
#         response.redirect(url='/gather_input')

#     else:
#         # File wasn't generated in time, handle the error case
#         response.say("Error 1. We are experiencing technical difficulties. Please try again later.")

#     return str(response)

# Process the users speech and give to SalesGPT
# Get audio from SalesGPT and play it for the user
# Redirect to gather_input to get the users response
@app.route("/process_speech", methods=['POST'])
def process_speech():
    print(" ----- process_speech -----")
    file_path = "output_text.txt"

    # delete the file if it exists
    if os.path.exists(file_path):
        os.remove(file_path)

    speech_text = request.form.get("SpeechResult", "")
    confidence = request.form.get("Confidence", "0")
    print(f"process_speech :: Received speech input: {speech_text} (Confidence: {confidence})")
    save_speech_input(speech_text)

    # Wait for the MP3 file to be generated
    timeout = 30  # Maximum wait time in seconds
    start_time = time.time()
    while not os.path.exists(file_path) and (time.time() - start_time) < timeout:
        print('Waiting for output text file to be generated...')
        time.sleep(1)  # Wait 1 second before checking again

    response = VoiceResponse()

    if os.path.exists(file_path):
        # get text from file
        with open(file_path, 'r') as file:
            text = file.read()

        # File is ready, play the MP3 and gather user response
        response.say(text, voice=voice)

        # Send the user to gather input
        response.redirect(url='/gather_input')

    else:
        # File wasn't generated in time, handle the error case
        response.say("Error 2. We are experiencing technical difficulties. Please try again later.")
    
    return str(response)
# def process_speech():
#     print(" ----- process_speech -----")
#     file_path = "static/audio/output.mp3"

#     # delete the file if it exists
#     if os.path.exists(file_path):
#         os.remove(file_path)

#     speech_text = request.form.get("SpeechResult", "")
#     confidence = request.form.get("Confidence", "0")
#     print(f"process_speech :: Received speech input: {speech_text} (Confidence: {confidence})")
#     save_speech_input(speech_text)

#     # Wait for the MP3 file to be generated
#     timeout = 30  # Maximum wait time in seconds
#     start_time = time.time()
#     while not os.path.exists(file_path) and (time.time() - start_time) < timeout:
#         print('Waiting for MP3 file to be generated...')
#         time.sleep(1)  # Wait 1 second before checking again


#     response = VoiceResponse()

#     if os.path.exists(file_path):
#         # get length of audio
#         audio_length = 0
#         audio_length = os.path.getsize(file_path)
#         audio_length = audio_length / 1000
#         print(f" -- Audio length: {audio_length} seconds")

#         # File is ready, play the MP3 and gather user response
#         response.play(url=BASE_URL + "/static/audio/output.mp3")

#         # Pause for audio_length before redirecting to gather_input
#         # response.pause(length=audio_length)

#         # Send the user to gather input
#         response.redirect(url='/gather_input')

#     else:
#         # File wasn't generated in time, handle the error case
#         response.say("Error 2. We are experiencing technical difficulties. Please try again later.")
    
#     return str(response)

# Gather the users speech input and send it to to process_speech
@app.route("/gather_input", methods=['POST'])
def gather_input():
    print(" ----- gather_input -----")

    response = VoiceResponse()
    # Now, initiate the Gather for input, ensuring the audio has finished playing
    gather = Gather(
        input='speech', 
        action='/process_speech', 
        method='POST',
        speechTimeout= 'auto',
        speechModel='phone_call',
        ) 
    response.append(gather)

    # If the user doesn't say anything for more than 5 seconds, then hang up
    # response.pause(length=5)
    # response.say("We didn't receive any input. Goodbye.")
    # print('We didn\'t receive any input. Goodbye.')
    # response.hangup()
    
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)