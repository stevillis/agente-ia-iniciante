from agent import InicianteAgent

if __name__ == "__main__":
    print("🤖 Agente IA Iniciante - Interface de Linha de Comando")
    print("Digite 'exit' para sair\n")

    try:
        agent = InicianteAgent()
    except ValueError as e:
        print(f"❌ Erro de inicialização: {e}")
        exit()

    while True:
        user_question = input("Como posso ajudá-lo? ")

        if user_question.lower() in ["exit", "quit", "sair"]:
            print("Até logo!")
            break

        if not user_question.strip():
            continue

        try:
            response = agent.run(user_question)
            print(f"\n🤖 {response['output']}\n")
        except Exception as e:
            print(f"\n❌ Erro: {str(e)}\n")
