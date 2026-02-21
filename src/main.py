import os
import shutil
import threading
import time
import customtkinter as ctk
from tkinter import filedialog
from gemini_client import configurar_api, extrair_texto_da_imagem

class AplicacaoOCR(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.title("Leitor de Manuscritos")
		self.geometry("900x700")
		self.protocol("WM_DELETE_WINDOW", self.encerrar_aplicacao)
		self.diretorio_base = os.path.dirname(os.path.abspath(__file__))
		self.diretorio_paginas = os.path.join(self.diretorio_base, '..', 'paginas')
		self.caminhos_temporarios = []
		if not os.path.exists(self.diretorio_paginas):
			os.makedirs(self.diretorio_paginas)
		self.construir_interface()
		configurar_api()

	def construir_interface(self):
		self.botao_upload = ctk.CTkButton(self, text="Carregar Imagens", font=("Arial", 16), command=self.selecionar_imagens)
		self.botao_upload.pack(pady=20)
		
		self.caixa_texto = ctk.CTkTextbox(self, width=800, height=500, font=("Arial", 18))
		self.caixa_texto.pack(pady=10)
		
		self.botao_copiar = ctk.CTkButton(self, text="Copiar Texto", font=("Arial", 16), command=self.copiar_texto)
		self.botao_copiar.pack(pady=10)

	def selecionar_imagens(self):
		arquivos_selecionados = filedialog.askopenfilenames(
			title="Selecione as imagens",
			filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")]
		)
		if arquivos_selecionados:
			self.botao_upload.configure(state="disabled")
			for caminho_original in arquivos_selecionados:
				nome_arquivo = os.path.basename(caminho_original)
				caminho_destino = os.path.join(self.diretorio_paginas, nome_arquivo)
				shutil.copy(caminho_original, caminho_destino)
				if caminho_destino not in self.caminhos_temporarios:
					self.caminhos_temporarios.append(caminho_destino)
			
			threading.Thread(target=self.processar_lote, daemon=True).start()

	def processar_lote(self):
		for caminho_imagem in self.caminhos_temporarios:
			nome_arquivo = os.path.basename(caminho_imagem)
			self.inserir_texto_interface(f"\n--- Imagem: {nome_arquivo} ---\n")
			
			try:
				texto_extraido = extrair_texto_da_imagem(caminho_imagem)
				self.inserir_texto_interface(texto_extraido + "\n")
			except Exception as e:
				self.inserir_texto_interface(f"[Erro na API]: {str(e)}\n")
			
			time.sleep(5)
			
		self.botao_upload.configure(state="normal")
		self.inserir_texto_interface("\n--- Lote Finalizado ---\n")
		self.caminhos_temporarios.clear()

	def inserir_texto_interface(self, texto):
		self.caixa_texto.insert("end", texto)
		self.caixa_texto.see("end")

	def copiar_texto(self):
		texto_completo = self.caixa_texto.get("1.0", "end-1c")
		self.clipboard_clear()
		self.clipboard_append(texto_completo)

	def encerrar_aplicacao(self):
		for arquivo in os.listdir(self.diretorio_paginas):
			caminho_arquivo = os.path.join(self.diretorio_paginas, arquivo)
			try:
				os.remove(caminho_arquivo)
			except OSError:
				pass
		self.destroy()

if __name__ == "__main__":
	app = AplicacaoOCR()
	app.mainloop()