# Handwriting Transcriber

[![Python tests](https://github.com/JamesMakarov/Leitor-de-manuscritos/actions/workflows/ci.yml/badge.svg)](https://github.com/JamesMakarov/Leitor-de-manuscritos/actions/workflows/ci.yml)

Aplicação desktop em **Python + CustomTkinter** para transcrever texto manuscrito a partir de imagens usando a API do **Gemini**.

O usuário seleciona uma ou mais imagens, o aplicativo envia cada arquivo para o modelo, exibe a transcrição na interface e permite copiar o texto resultante.

## Funcionalidades

- seleção de múltiplas imagens;
- suporte a PNG, JPG e JPEG;
- processamento em lote;
- execução da transcrição em thread separada para não bloquear a interface;
- integração com a API Gemini;
- exibição das transcrições em uma caixa de texto;
- cópia do resultado para a área de transferência;
- uso de variável de ambiente para a chave da API.

## Tecnologias

- Python
- CustomTkinter
- Google Gen AI SDK
- python-dotenv
- Tkinter

## Estrutura

```text
.
├── src/
│   ├── main.py
│   ├── gemini_client.py
│   └── file_manager.py
├── examples/
│   ├── input.png
│   └── output.txt
├── requirements.txt
└── .env.example
```

## Executando

### 1. Clone o repositório

```bash
git clone https://github.com/JamesMakarov/Leitor-de-manuscritos.git
cd Leitor-de-manuscritos
```

### 2. Crie e ative um ambiente virtual

Windows:

```bat
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a API

Copie `.env.example` para `.env` e informe sua chave:

```env
GEMINI_API_KEY=your-api-key
```

### 5. Execute

```bash
python src/main.py
```

## Exemplo

A pasta `examples/` contém uma imagem de entrada e a transcrição correspondente, separadas dos arquivos temporários usados durante a execução.

## Como funciona

`gemini_client.py` carrega a chave `GEMINI_API_KEY`, envia a imagem para a API e solicita apenas a transcrição do conteúdo manuscrito.

A interface processa as imagens em sequência e exibe cada resultado associado ao nome do arquivo correspondente.

## Segurança

O arquivo `.env` não deve ser versionado. Apenas o modelo `.env.example` deve permanecer no repositório.
