import os
from google import genai
from dotenv import load_dotenv

def configurar_api():
    load_dotenv()

def extrair_texto_da_imagem(caminho_imagem):
    chave_api = os.getenv("GEMINI_API_KEY")
    if not chave_api:
        raise RuntimeError("GEMINI_API_KEY não foi configurada.")
    cliente = genai.Client(api_key=chave_api)
    arquivo_upload = cliente.files.upload(file=caminho_imagem)
    prompt = "Transcreva o texto manuscrito desta imagem. Retorne apenas a transcrição, sem explicações adicionais."
    resposta = cliente.models.generate_content(model='gemini-2.5-flash', contents=[prompt, arquivo_upload])
    return resposta.text