import streamlit as st

from agent import InicianteAgent


def main():
    st.set_page_config(
        page_title="Agente IA Iniciante", page_icon="🤖", layout="centered"
    )

    st.title("🤖 Agente IA Iniciante")
    st.markdown(
        "Um agente de IA para fazer cálculos matemáticos e pesquisar na Wikipedia."
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "agent" not in st.session_state:
        try:
            st.session_state.agent = InicianteAgent()
        except ValueError as e:
            st.error(e)
            return

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Faça sua pergunta..."):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Processando..."):
                try:
                    agent = st.session_state.agent
                    result = agent.run(prompt)

                    if isinstance(result, dict) and "output" in result:
                        response_text = result["output"]
                    else:
                        response_text = str(result)

                    st.markdown(response_text)
                except Exception as e:
                    error_message = f"Erro ao processar sua solicitação: {str(e)}"
                    st.error(error_message)
                    response_text = error_message

        st.session_state.messages.append(
            {"role": "assistant", "content": response_text}
        )

    with st.sidebar:
        st.markdown(
            """
        **ℹ️ Funcionalidades:**
        - 🧮 **Calculadora:** Realize cálculos matemáticos.
        - 📚 **Wikipedia:** Pesquise por tópicos na Wikipedia.

        **Exemplos de perguntas:**
        - "Quanto é 25 elevado a 5?"
        - "Qual a capital do Brasil?"
        - "Quem foi Albert Einstein?"
        """
        )

        if st.button("🗑️ Limpar Conversa"):
            st.session_state.messages = []
            if "agent" in st.session_state:
                del st.session_state["agent"]
            st.rerun()


if __name__ == "__main__":
    main()
