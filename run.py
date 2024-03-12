import json
import os

from dotenv import load_dotenv
from langchain_community.chat_models import ChatLiteLLM

from salesgpt.agents import SalesGPT
from lib.wait_for_speech_input import wait_for_speech_input

def process_call(isVerbose, isConfig, use_config_path):
    load_dotenv()  # loads .env file

    # LangSmith settings
    os.environ["LANGCHAIN_TRACING_V2"] = "false"
    os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
    os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_SMITH_API_KEY", "")
    os.environ["LANGCHAIN_PROJECT"] = ""  # insert your project name here

    # Use the parameters directly instead of parsing them
    verbose = isVerbose
    config_path = use_config_path if isConfig else ""

    llm = ChatLiteLLM(temperature=0.2, model_name="gpt-4-0125-preview")

    if not config_path:
        print("No agent config specified, using a standard config")
        USE_TOOLS = True
        sales_agent_kwargs = {
            "verbose": verbose,
            "use_tools": USE_TOOLS,
        }

        if USE_TOOLS:
            sales_agent_kwargs.update({
                "product_catalog": "examples/sample_product_catalog.txt",
                "salesperson_name": "Ted Lasso",
            })

        sales_agent = SalesGPT.from_llm(llm, **sales_agent_kwargs)
    else:
        try:
            with open(config_path, "r", encoding="UTF-8") as f:
                config = json.load(f)
        except FileNotFoundError:
            print(f"Config file {config_path} not found.")
            return
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the config file {config_path}.")
            return

        print(f"Agent config {config}")
        sales_agent = SalesGPT.from_llm(llm, verbose=verbose, **config)

    sales_agent.seed_agent()
    print("=" * 10)
    cnt = 0
    max_num_turns = 10  # Assuming a default value, adjust as needed
    while cnt != max_num_turns:
        cnt += 1
        if cnt == max_num_turns:
            print("Maximum number of turns reached - ending the conversation.")
            break
        sales_agent.step()

        # Simulate end of conversation
        if "<END_OF_CALL>" in sales_agent.conversation_history[-1]:
            print("Sales Agent determined it is time to end the conversation.")
            break

        text_input = wait_for_speech_input(timeout=60) 
        
        # delete the speech_inputs.txt file
        if os.path.exists('speech_inputs.txt'):
            os.remove('speech_inputs.txt')

        print("text_input: ", text_input)

        human_input = text_input
        sales_agent.human_step(human_input)


        print("=" * 10)