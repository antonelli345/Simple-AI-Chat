import google.generativeai as genai
import os
import sys
from dotenv import load_dotenv

# Função que adapta o comando de entrada (input) para diferentes versões do Python.
# Para Python 2, usa raw_input; para Python 3, usa input.

def inputpy():
    if sys.version_info.major == 2:
        return raw_input("Enter a prompt: ") # Compatível com Python 2.
    elif sys.version_info.major == 3:
        return input("Enter a prompt: ") # Compatível com Python 3.

def main():
    # Carrega as variáveis de ambiente do arquivo .env, permitindo armazenar a API key de forma segura.
    load_dotenv()
    # Obtém a chave de API armazenada na variável de ambiente "API_KEY" no arquivo .env.
    API_KEY = os.getenv("API_KEY")
    # Configura o módulo genai com a chave de API fornecida.
    # Essa chave permite autenticar as requisições para a API do Google Generative AI.
    genai.configure(api_key=API_KEY)
    # Instancia o modelo generativo do Google, especificando o modelo desejado ('gemini-pro').
    model = genai.GenerativeModel('gemini-pro')
    # Captura o input do usuário e utiliza-o como prompt para o modelo de IA.
    # A função `generate_content` processa o prompt e retorna uma resposta gerada pela IA.
    response = model.generate_content(inputpy())
    # Exibe o texto da resposta gerada pela IA no console.
    print(response.text)

# Executa a função principal.
main() 