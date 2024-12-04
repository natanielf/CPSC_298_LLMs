#!/usr/bin/env python3

import json
import logging
import os
from typing_extensions import Annotated
import requests

from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

WEATHER_API_URL = "https://wttr.in"


def get_weather() -> Annotated[dict, "Current weather conditions"]:
    url = f"{WEATHER_API_URL}/?format=j1"
    response = requests.get(url)
    logging.info(response.status_code)
    logging.info(response.content)
    info = json.loads(response.content)
    current_conditions = info["current_condition"][0]
    area = info["nearest_area"][0]
    city = area["areaName"][0]["value"]
    region = area["region"][0]["value"]
    country = area["country"][0]["value"]
    location = f"{city}, {region}, {country}"
    weather_info = {
        "temp_fahrenheit": current_conditions["temp_F"],
        "precipitation_inches": current_conditions["precipInches"],
        "description": current_conditions["weatherDesc"][0]["value"],
        "location": location,
    }
    return weather_info


def main():
    # Load environment variables
    load_dotenv()

    # API config
    config_list = [
        {
            "model": "llama3-8b-8192",
            "base_url": "https://api.groq.com/openai/v1/",
            "api_key": os.getenv("GROQ_API_KEY"),
        }
    ]

    # Weather agent
    weather_assistant = AssistantAgent(
        name="Weather assistant",
        system_message="A helpful assistant that retrieves weather and location information",
        llm_config={"config_list": config_list},
        human_input_mode="NEVER",
        max_consecutive_auto_reply=2,
    )

    # Register the weather tool
    weather_assistant.register_for_llm(
        name="get_weather",
        description="Get the current weather conditions for the user's location",
    )(get_weather)

    # Activity agent
    activity_assistant = AssistantAgent(
        name="Activity assistant",
        system_message="""
                        A helpful assistant that suggests relevant activites
                        based on current weather conditions and attractions
                        near the provided location
                       """,
        llm_config={"config_list": config_list},
        human_input_mode="NEVER",
        max_consecutive_auto_reply=2,
    )

    # Register the weather tool
    activity_assistant.register_for_llm(
        name="get_weather",
        description="Get the current weather conditions for the user's location",
    )(get_weather)

    # User proxy agent
    user_proxy = UserProxyAgent(
        name="User proxy",
        code_execution_config={"use_docker": False},
        human_input_mode="NEVER",
    )

    user_proxy.register_for_execution(name="get_weather")(get_weather)

    user_proxy.initiate_chat(weather_assistant, message="What should I wear today?")

    user_proxy.initiate_chat(activity_assistant, message="What should I do today?")


if __name__ == "__main__":
    main()
