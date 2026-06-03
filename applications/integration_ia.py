from langchain_google_genai import GoogleGenerativeAI
from langchain_core.globals import set_llm_cache
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_community.cache import SQLiteCache
from decouple import config



set_llm_cache(SQLiteCache(database_path=config('NAME_DB_CACHE_LANGCHAIN')))

model = GoogleGenerativeAI(model= "gemini-3.1-flash-lite",
                           api_key=config('GEMINI_API_KEY'),
                           )

prompt = "Me fale sobre django"

response = model.invoke(prompt)
print(response)


# def details_the_app_description(description_app: str):
#     response = client.models.generate_content(
#     model = "gemini-3-flash-preview", contents = f"Apresente melhor a descricao digitada a segui em no maximo um paragrafo de três à quatro linhas: {description_app}"
#     )

#     return response.text