from langchain_google_genai import ChatGoogleGenerativeAI
from triagem import TriagemOut
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm_triagem = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1,
    api_key=GEMINI_API_KEY
)

triagem_chain = llm_triagem.with_structured_output(TriagemOut)
