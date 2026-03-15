from rag_chatbot import ask_rag

print("RAG chatbot ready")

while True:

    query = input("Ask: ")

    if query == "exit":
        break

    answer = ask_rag(query)

    print(answer)