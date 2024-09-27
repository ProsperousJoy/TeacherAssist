from GeminiAIChat.core import API
import os
from dotenv import load_dotenv

load_dotenv()

res = API(os.environ['GEMINI_API_KEY'])
res.prompt("define what is python")
print(res.response())