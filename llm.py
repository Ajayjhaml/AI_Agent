from langchain_groq import ChatGroq
from config import GROQ_API_KEY


def get_llm():
    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="openai/gpt-oss-120b",
        temperature=0.2,
    )