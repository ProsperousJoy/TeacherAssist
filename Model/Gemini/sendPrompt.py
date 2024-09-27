from GeminiAIChat.core import API
import os

res = API(os.environ['GEMINI_API_KEY'])
res.prompt("test")
print(res.response)