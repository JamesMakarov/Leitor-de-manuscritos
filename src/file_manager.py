import os

def listar_imagens(diretorio_entrada):
	extensoes_permitidas = ('.png', '.jpg', '.jpeg')
	todos_arquivos = os.listdir(diretorio_entrada)
	imagens_filtradas = [arquivo for arquivo in todos_arquivos if arquivo.lower().endswith(extensoes_permitidas)]
	return imagens_filtradas

def gravar_texto_extraido(texto, nome_arquivo_original, diretorio_saida):
	nome_sem_extensao = os.path.splitext(nome_arquivo_original)[0]
	nome_arquivo_txt = f"{nome_sem_extensao}.txt"
	caminho_destino = os.path.join(diretorio_saida, nome_arquivo_txt)
	
	with open(caminho_destino, 'w', encoding='utf-8') as arquivo_txt:
		arquivo_txt.write(texto)