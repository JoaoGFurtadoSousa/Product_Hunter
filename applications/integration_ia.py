from langchain_google_genai import GoogleGenerativeAI
from langchain_core.globals import set_llm_cache
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.cache import SQLiteCache
from decouple import config



set_llm_cache(SQLiteCache(database_path=config('NAME_DB_CACHE_LANGCHAIN')))


def details_the_app_description(description:str):
    print("entrou")
    model = GoogleGenerativeAI(model= "gemini-3.1-flash-lite",
                            api_key=config('GEMINI_API_KEY'),
                            )

   
    prompt = f"""Você é um especialista em copywriting para produtos digitais e aplicativos.

        Sua função é reescrever a descrição fornecida pelo usuário, tornando-a mais profissional, persuasiva e atrativa para potenciais clientes.

        Diretrizes:
        - Utilize técnicas de copywriting focadas em benefícios, valor percebido e resolução de problemas.
        - Expanda a descrição original adicionando detalhes relevantes sobre funcionalidades, diferenciais e casos de uso, sem inventar recursos que não estejam implícitos no contexto.
        - Destaque como o aplicativo ajuda o usuário e quais problemas ele resolve.
        - Utilize linguagem clara, moderna e envolvente.
        - Mantenha um tom profissional e comercial.
        - Evite listas, tópicos ou emojis.
        - Gere apenas um único parágrafo entre 3 e 5 linhas.
        - Preserve o significado principal da descrição original, apenas enriquecendo e melhorando sua comunicação.
        - No maximo em 250 caracteres

        Retorne somente a descrição reescrita.
        
        Descricao:
        {description}
        """

    response = model.invoke(prompt)
    return response


# def details_the_app_description(description_app: str):
#     response = client.models.generate_content(
#     model = "gemini-3-flash-preview", contents = f"Apresente melhor a descricao digitada a segui em no maximo um paragrafo de três à quatro linhas: {description_app}"
#     )

#     return response.text