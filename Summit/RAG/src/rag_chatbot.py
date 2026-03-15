from retriever import retrieve
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def ask_rag(question):

    contexts = retrieve(question)

    context_text = "\n\n".join(contexts)

    prompt = f"""
Use the context to answer.

Context:
{context_text}

Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text