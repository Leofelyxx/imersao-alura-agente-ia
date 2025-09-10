from prompts import TRIAGEM_PROMPT_HUMAN, TRIAGEM_PROMPT_AI
from triagem import TriagemService
from llm_config import triagem_chain

#Para configurar os prompts, altere o arquivo prompts.py
#Versão utilizada do Python: 3.13.7
triagem_service = TriagemService(triagem_chain, TRIAGEM_PROMPT_AI)

for mensagem in TRIAGEM_PROMPT_HUMAN:
    print(f"Pergunta: {mensagem}\n -> Resposta: {triagem_service.triagem(mensagem)}\n")