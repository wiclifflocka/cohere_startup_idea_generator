import json
import os
import textwrap

import cohere
import streamlit as st


def cohere_client():
    return cohere.ClientV2("HhzJlm3RZOlFVqbRQcDUrkKQZsDcdrOp7dnlWSBS")


# if __name__ == "__main__":
    # Set up Cohere client
    # co = cohere.ClientV2("HhzJlm3RZOlFVqbRQcDUrkKQZsDcdrOp7dnlWSBS")