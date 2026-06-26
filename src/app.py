```python
import json
import pandas as pd
import requests
import streamlit as st

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# ============ CARREGAR DADOS ============
perfil = json.load(open('./data/perfil_jogador.json', encoding='utf-8'))
personagens = pd.read_csv('./data/personagens.csv')
historico = pd.read_csv('./data/historico_sessoes.csv')
regras = json.load(open('./data/conteudo_regras.json', encoding='utf-8'))

# ============ MONTAR CONTEXTO ============
contexto = f"""
JOGADOR: {perfil['nome']}
EXPERIÊNCIA: {perfil['experiencia']}
SISTEMA PREFERIDO: {perfil['sistema_preferido']}
ESTILO DE JOGO: {perfil['estilo_jogo']}

PERSONAGENS DO JOGADOR:
{personagens.to_string(index=False)}

HISTÓRICO DE CONSULTAS:
{historico.to_string(index=False)}

REGRAS E CONTEÚDO DISPONÍVEL:
{json.dumps(regras, indent=2, ensure_ascii=False)}
"""

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """
Você é Arkan, um consultor especializado em RPG de mesa.

OBJETIVO:
Ajudar jogadores e mestres a compreender regras, criar personagens,
otimizar builds e interpretar mecânicas do sistema informado.

REGRAS:
- Priorize regras oficiais presentes na base de conhecimento;
- Nunca invente regras oficiais;
- Diferencie claramente regras oficiais, interpretações e homebrews;
- Utilize os dados do jogador para personalizar sugestões;
- Explique vantagens e desvantagens de cada build;
- Não afirme que existe uma única build perfeita;
- Caso não encontre a informação, diga:
  "Não encontrei essa informação na base de conhecimento disponível.";
- Se o sistema de RPG não for informado, peça esclarecimento;
- Responda de forma objetiva e organizada;
- Mantenha linguagem amigável voltada para RPG de mesa.

ESCOPO:
- Classes e subclasses
- Raças e ancestrais
- Talentos
- Equipamentos
- Magias
- Progressão de nível
- Multiclasse
- Regras de combate
- Otimização de builds
- Criação de personagens

FORA DE ESCOPO:
- Assuntos não relacionados a RPG de mesa.
"""

# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO JOGADOR:
{contexto}

PERGUNTA:
{msg}
"""

    resposta = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False
        }
    )

    return resposta.json()["response"]

# ============ INTERFACE ============
st.set_page_config(
    page_title="Arkan - Consultor de RPG",
    page_icon="🎲"
)

st.title("🎲 Arkan - Consultor de RPG")
st.caption("Criação de personagens, builds, regras e otimização")

if pergunta := st.chat_input(
    "Pergunte sobre builds, classes, talentos ou regras..."
):
    st.chat_message("user").write(pergunta)

    with st.spinner("Consultando os tomos arcanos..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)
```

