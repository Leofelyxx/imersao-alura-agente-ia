from pydantic import BaseModel, Field
from typing import Literal, List, Dict, Any
from langchain_core.messages import SystemMessage, HumanMessage

class TriagemOut(BaseModel):
    decisao: Literal["AUTO_RESOLVER", "PEDIR_INFO", "ABRIR_CHAMADO"]
    urgencia: Literal["BAIXA", "MEDIA", "ALTA"]
    campos_faltantes: List[str] = Field(default_factory=list)

class TriagemService:
    def __init__(self, triagem_chain: Any, triagem_prompt_ai: str):
        self.triagem_chain = triagem_chain
        self.triagem_prompt_ai = triagem_prompt_ai

    def triagem(self, mensagem: str) -> Dict:
        saida: TriagemOut = self.triagem_chain.invoke([
            SystemMessage(content=self.triagem_prompt_ai),
            HumanMessage(content=mensagem)
        ])

        return saida.model_dump()