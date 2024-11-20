#!/usr/bin/env python3

from beehive import Beehive, BeehiveAgent, FixedExecution
from openai import OpenAIModel


def main():
    print("Hello, world!")
    linguist_agent = BeehiveAgent(
        name="Linguist",
        backstory="You are an expert in linguistics. You work alongside another linguist to develop new languages.",
        model=OpenAIModel(
            model="gpt-4-turbo",
        ),
    )

    linguist_critic = BeehiveAgent(
        name="LinguistCritic",
        backstory="You are an expert in linguistics. Specifically, you are great at examining grammatical rules of new languages and suggesting improvements.",
        model=OpenAIModel(
            model="gpt-4-turbo",
        ),
    )

    beehive = Beehive(
        name="LanguageGeneratorBeehive",
        backstory="You are an expert in creating new languages.",
        model=OpenAIModel(
            model="gpt-4-turbo",
        ),
        execution_process=FixedExecution(route=(linguist_agent >> linguist_critic)),
        chat_loop=2,
        enable_questioning=True,
    )
    beehive.invoke(
        "Develop a new language using shapes and symbols. After you have developed a comprehensive set of grammar rules, provide some examples of sentences and their representation in the new language.",
        pass_back_model_errors=True,
    )


if __name__ == "__main__":
    main()
