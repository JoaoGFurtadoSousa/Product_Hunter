from google import genai
from decouple import config


client = genai.Client(api_key = config('GEMINI_API_KEY'))

def details_the_app_description(description_app: str):
    response = client.models.generate_content(
    model = "gemini-3-flash-preview", contents = f"Apresente melhor a descricao digitada a segui em no maximo um paragrafo de três à quatro linhas: {description_app}"
    )

    return response.text