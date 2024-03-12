# :robot: SalesGPT - Open Source AI Agent for Sales

This repo is an implementation of a **context-aware** AI Agent for Sales using LLMs and can work across voice, email and texting (SMS, WhatsApp, WeChat, Weibo, Telegram, etc.). 

SalesGPT is *context-aware*, which means it can understand what stage of a sales conversation it is in and act accordingly.
Morever, SalesGPT has access to tools, such as your own pre-defined product knowledge base, significantly reducing hallucinations.

This Repo has been updated by Tristan Perera to be able to utilize Text To Speech and Speech To Text using either gTTS or ElevenLabs API, and connected to VoIP via Twilio to make phone calls to 'talk' to users. 

Find the original repo here:
https://github.com/filip-michalsky/SalesGPT

# Setup

## Install

Make sure you have a **python >=3.8,<3.12**:

Create a virtual environment at a location on your computer. We use the generic "env" name for our virtual environment in the setup. You can rename this, but make sure to then use this name later when working with the environment (also rename the VENV variable in the Makefile accordingly to be able to use make commands successfully after cloning our repository):

#### For Windows:

- Open Command Prompt or PowerShell.
- Navigate to your project directory: `cd path\to\your\project`
- Create a virtual environment: `python -m venv env`
- Activate the virtual environment: `.\env\Scripts\activate`

#### For Mac:

- Open Terminal.
- Navigate to your project directory: `cd path/to/your/project`
- Create a virtual environment: `python3 -m venv env`
- Activate the virtual environment: `source env/bin/activate`

To deactivate a virtual environment after you have stopped using it simply run: `deactivate`

Clone the SalesGPT Github repository: 

`git clone https://github.com/filip-michalsky/SalesGPT.git`

Navigate to the repository and in case you used a different venv name rename the VENV variable in the Makefile: 

`cd SalesGPT`

If you simply want to work with SalesGPT as an end user without local changes you can install from PyPI using: 

`pip install salesgpt`

If you want to work on your own version of SalesGPT or contribute to our open-source version install by activating your virtual environment as aforementioned and then run: 

`make setup`

For more detailed installation steps along with the reasons for doing each please visit CONTRIBUTING.md

Finally, for use of SalesGPT create an `.env` file just as our `.env.example` and put your API keys there by specifying a new line just as we have done.

## Run the agent
- Navigate to to the root folder
- Update necessary variables
- Activate python env following the installation instructions above
- Run the main.py script
- Initiate the call by sending get request to /make_call (you can just visit this on the browser)

## Uninstall SalesGPT

To delete the virtual environment you used for SalesGPT programming and your SalesGPT repository from your system navigate to the directory where you installed your virtual environment and cloned SalesGPT and run: 
`make clean`