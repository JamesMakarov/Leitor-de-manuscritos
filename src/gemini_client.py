import os
import google.generativeai as genai
from dotenv import load_dotenv

def configurar_api():
	load_dotenv()
	chave_api = os.getenv("GEMINI_API_KEY")
	genai.configure(api_key=chave_api)

def extrair_texto_da_imagem(caminho_imagem):
	modelo = genai.GenerativeModel('gemini-1.5-flash')
	arquivo_upload = genai.upload_file(caminho_imagem)
	prompt = "Transcreva o texto manuscrito desta imagem. Retorne apenas a transcrição, sem explicações adicionais."
	resposta = modelo.generate_content([prompt, arquivo_upload])
	return resposta.text