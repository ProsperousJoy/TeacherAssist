from GeminiAIChat.core import API
from dotenv import load_dotenv
import os

# Create your .env file in root folder and it will be loaded here
load_dotenv()

# Prompt
def prompt(material, n):
    res = API(os.environ['GEMINI_API_KEY'])
    res.prompt(f'''Start acting as a teacher, you will be given a material and a number n. You will create a powerpoint material and an image description of a stock image that suits the slide.

    Divide each slides with a "---SLIDE N".
    For example:
    ---SLIDE N
    (Material)
    Image description for slide: (image description)
    ---SLIDE N
    (Material)
    Image description for slide: (image description)

    Material: {material}
    Number of slides: {n}

    Do not add further comments, only the slide materials''')
    return res.response()
