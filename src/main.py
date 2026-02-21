import os
import sys
from file_manager import listar_imagens, gravar_texto_extraido
from gemini_client import configurar_api, extrair_texto_da_imagem

def main():
	diretorio_atual = os.path.dirname(os.path.abspath(__file__))
	pasta_entrada = os.path.join(diretorio_atual, '..', 'paginas')
	pasta_saida = os.path.join(diretorio_atual, '..', 'textos_extraidos')
	
	if not os.path.exists(pasta_saida):
		os.makedirs(pasta_saida)
		
	configurar_api()
	
	imagens = listar_imagens(pasta_entrada)
	
	if not imagens:
		print("Nenhuma imagem encontrada na pasta de entrada.")
		sys.exit(0)
		
	for imagem in imagens:
		caminho_imagem = os.path.join(pasta_entrada, imagem)
		print(f"Iniciando inferência multimodal para: {imagem}")
		
		texto_processado = extrair_texto_da_imagem(caminho_imagem)
		gravar_texto_extraido(texto_processado, imagem, pasta_saida)
		
		print(f"Escrita em disco concluída para: {imagem}")

if __name__ == '__main__':
	main()