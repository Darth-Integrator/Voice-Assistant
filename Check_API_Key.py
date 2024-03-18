import os
import openai
#importing dotenv to access the environment variable open ai key #from .env file
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
#lets list the LLM models available from openai
openai.Model.list()