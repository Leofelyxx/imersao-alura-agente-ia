# Imersão Agente IA

Projeto de triagem automatizada de mensagens para Service Desk utilizando IA generativa (Google Gemini) e validação de dados com Pydantic.

## Requisitos
- Python 3.13.7
- Ambiente virtual (recomendado)
- Chave de API Gemini (Google)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

2. Crie e ative um ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto com sua chave Gemini:
```
GEMINI_API_KEY=sua-chave-aqui
```

## Uso

Execute o script principal:
```bash
python3 main.py
```

As perguntas de exemplo e o prompt do sistema podem ser alterados no arquivo `prompts.py`.

## Observações
- Não compartilhe seu arquivo `.env`.
- O projeto está organizado em módulos para facilitar manutenção e expansão.

---

Feito com 💡 por Leonardo Felix
