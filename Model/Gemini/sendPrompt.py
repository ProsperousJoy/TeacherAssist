from GeminiAIChat.core import API
from dotenv import load_dotenv
import os

# Create your .env file in root folder and it will be loaded here
load_dotenv()

# Prompts
res = API(os.environ['GEMINI_API_KEY'])
res.prompt("define what is python")
print(res.response())