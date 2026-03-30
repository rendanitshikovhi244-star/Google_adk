import os
from google.adk.models.lite_llm import LiteLlm
from dotenv import load_dotenv

load_dotenv()

from google.adk.agents import Agent

hf_model = os.getenv("HF_MODEL")

root_agent = Agent(
    name="PostAgent",
    description="An agent that knows some things about the user and their posts preferences",
    model=LiteLlm(model=hf_model),
    instruction="""
        You are a helpful assistant that can respond about the user and their post preferences.

    The information about the user and their post preferences is given in the state context.
    Name: {user_name}
    Post Preferences: {user_post_preferences}
    """,
)