from google import genai
from decouple import config


client = genai.Client(api_key = config('GEMINI_API_KEY'))

def details_the_app_description(id: int):
    response = client.models.generate_content(
    model = "gemini-3-flash-preview", contents = "Me explique o que significa boa noite"
    )

print(response.text)