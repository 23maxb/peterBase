import random
from http.client import responses

from openai import OpenAI

from text.resources import getPrompt, getTopics
from dotenv import load_dotenv


def getText(subject):
    client = OpenAI()
    response = client.responses.create(
        model="gpt-4.1-mini-2025-04-14",
        input=getPrompt(subject, 1),
    )
    return response.output_text


def addCaptions(clip):
    return "hi"


if __name__ == "__main__":
    if not load_dotenv(".env"):
        raise Exception("Failed to load .env file. Make sure it exists and is properly configured.")
    responses = getText(getTopics()[0])
    print(responses)