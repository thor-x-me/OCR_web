import google.generativeai as genai
from dotenv import load_dotenv
import os


def getResponseFromImage(image, question=None):
    load_dotenv()

    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

    genai.configure(api_key=GOOGLE_API_KEY)

    # Upload the file and print a confirmation.
    sample_file = genai.upload_file(path=image,
                                display_name=image.split('/')[-1])

    # Choose a Gemini API model.
    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

    # Prompt the model with text and the previously uploaded image.
    response = model.generate_content([sample_file, f"{question}"])

    return response.text

