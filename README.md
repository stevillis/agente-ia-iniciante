# Agente IA Iniciante

Este projeto é um agente de IA construído com LangChain que pode responder a perguntas e realizar tarefas usando ferramentas como uma calculadora e a Wikipedia. Ele utiliza uma interface web criada com Streamlit para interação com o usuário, além de uma interface de linha de comando.

## Funcionalidades

- 📚 **Pesquisa na Wikipedia:** Busca informações na Wikipedia sobre diversos tópicos.
- 🧮 **Calculadora:** Avalia expressões matemáticas.
- 🤖 **Processamento de Linguagem Natural:** Entende perguntas feitas de forma conversacional.
- 🖥️ **Interface Web:** Interface moderna e intuitiva com Streamlit.
- 💻 **Interface CLI:** Versão de linha de comando para uso rápido.

## Como Usar

1.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Configure suas variáveis de ambiente:**
    Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API:
    ```
    GEMINI_API_KEY=sua_chave_gemini_aqui
    ```

3.  **Execute o aplicativo:**

    **Interface Web (Recomendado):**
    ```bash
    streamlit run src/app.py
    ```

    **Interface de Linha de Comando:**
    ```bash
    python src/cli.py
    ```

## Exemplos de Uso

- "Qual a capital do Japão?"
- "Quanto é `(100 / 25) * 5`?"
- "Quem escreveu o livro 'O Senhor dos Anéis'?"

## Referência

Este projeto foi inspirado no artigo:
[Desmistificando AI Agents: Um Guia Prático Para Iniciantes com Python e LangChain](https://www.dio.me/articles/desmistificando-ai-agents-um-guia-pratico-para-iniciantes-com-python-e-langchain)
