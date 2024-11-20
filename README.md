
# **Simple-AI-Chat**

Um script simples que permite interação com uma API de IA generativa. O usuário insere um prompt, e a IA responde com base no modelo configurado.

---

## **Funcionalidades**
- Consumo de uma API de IA para gerar respostas baseadas no input do usuário.
- Utilização de variáveis de ambiente para armazenar a chave da API com segurança.
- Compatibilidade com Python 3 (e Python 2, se necessário).

---

## **Por que usamos o modelo Gemini?**
Optamos pelo modelo **Gemini** porque ele oferece um excelente equilíbrio entre capacidade e acessibilidade. Além disso, é possível utilizar o serviço **gratuitamente**, desde que o limite de requisições do plano gratuito não seja excedido. Isso o torna ideal para aprender, testar e desenvolver pequenos projetos sem custo inicial.

---

## **Pré-requisitos**
Certifique-se de ter as seguintes ferramentas instaladas antes de usar este projeto:
- [Python 3.x](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/)
- [Google Generative AI SDK](https://pypi.org/project/google-generativeai/)
- Biblioteca `dotenv` para gerenciar variáveis de ambiente.

---

## **Instalação**
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/simple-ai-chat.git
   cd simple-ai-chat
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure sua chave de API:
   - Crie um arquivo chamado `.env` no diretório raiz do projeto.
   - Adicione sua chave de API ao arquivo:
     ```plaintext
     API_KEY=SUA_CHAVE_AQUI
     ```

---

## **Como Usar**
1. Execute o script principal:
   ```bash
   python nome_do_arquivo.py
   ```

2. Insira um prompt no terminal quando solicitado, e a IA responderá.

Exemplo:
```bash
Enter a prompt: Qual é o significado da vida?
Resposta da IA: 42
```

---

## **Estrutura do Projeto**
```
simple-ai-chat/
├── main.py             # Script principal para executar o projeto
├── .env                # Arquivo contendo a chave da API (não incluso no repositório)
├── requirements.txt    # Lista de dependências do projeto
└── README.md           # Documentação do projeto
```

---

## **Contribuições**
Contribuições são bem-vindas! Siga estas etapas para colaborar:
1. Faça um fork do repositório.
2. Crie uma branch para suas alterações:
   ```bash
   git checkout -b minha-feature
   ```
3. Envie um pull request com uma descrição das alterações.

---

## **Licença**
Este projeto está licenciado sob a [MIT License](LICENSE). Você pode usá-lo, modificá-lo e distribuí-lo conforme as condições da licença.

---
