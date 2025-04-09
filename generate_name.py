import json
import os
import textwrap

import cohere
import streamlit as st

from main import cohere_client
# from generate_idea import generate_idea

# Set up Cohere client
# co = cohere.ClientV2("HhzJlm3RZOlFVqbRQcDUrkKQZsDcdrOp7dnlWSBS")
co = cohere_client()


def generate_name(idea, temperature):

    prompt= f"""
Generate a startup name given the startup idea. Return the startup name and without additional commentary.

Startup Idea: A platform that generates slide deck contents automatically based on a given outline
Startup Name: Deckerize

Startup Idea: An app that calculates the best position of your indoor plants for your apartment
Startup Name: Planteasy 

Startup Idea: A hearing aid for the elderly that automatically adjusts its levels and with a battery lasting a whole week
Startup Name: Hearspan

Startup Idea: An online primary school that lets students mix and match their own curriculum based on their interests and goals
Startup Name: Prime Age

Startup Idea: {idea}
Startup Name:"""

    # Call the Cohere Chat endpoint
    response = co.chat(
        messages=[{"role": "user", "content": prompt}],
        model="command-a-03-2025",
        temperature=temperature,
    )

    return response.message.content[0].text


# if __name__ == "__main__":
#     while True:
#         response = generate_idea(input("Enter industry: "))
#         name = generate_name(response)
#         print(f"Idea Name : {name}\n\nIdea: {response}")
#         print("*****************************\n")
