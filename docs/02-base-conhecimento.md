# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_sessoes.csv` | CSV | Registrar dúvidas anteriores, builds discutidas e decisões tomadas durante campanhas. |
| `perfil_jogador.json` | JSON | Armazenar preferências do jogador, sistemas favoritos, estilo de jogo e experiência. |
| `conteudo_regras.json` | JSON | Contém classes, raças, talentos, magias, equipamentos e regras oficiais do sistema. |
| `personagens.csv` | CSV | Armazena fichas resumidas dos personagens para análise e otimização. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

A base foi expandida para incluir informações de progressão de personagem, sinergias entre classes e restrições de regras. Também foram adicionados campos para identificar conteúdo oficial, suplementos e regras da casa, permitindo que o agente diferencie claramente cada fonte.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Existem duas possibilidades: injetar os dados diretamente no prompt ou carregá-los dinamicamente por código.

import pandas as pd
import json

perfil = json.load(open('./data/perfil_jogador.json'))
personagens = pd.read_csv('./data/personagens.csv')
historico = pd.read_csv('./data/historico_sessoes.csv')
regras = json.load(open('./data/conteudo_regras.json'))

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?
```text
Para simplificar, podemos injetar os dados diretamente no contexto do agente. Em aplicações mais robustas, o ideal é consultar apenas as informações relevantes para cada pergunta.

PERFIL DO JOGADOR (data/perfil_jogador.json):
{
  "nome": "Carlos Andrade",
  "experiencia": "intermediario",
  "sistema_preferido": "D&D 5e",
  "estilo_jogo": "combate_tatico",
  "classes_favoritas": [
    "Guerreiro",
    "Paladino"
  ],
  "objetivos": [
    "Criar personagens eficientes",
    "Aprender otimização de builds"
  ]
}

PERSONAGENS DO JOGADOR (data/personagens.csv):
nome,classe,nivel,atributo_principal,funcao
Arthos,Paladino,8,Carisma,Tanque
Lyra,Maga,5,Inteligencia,Controle
Kael,Ranger,6,Destreza,Dano

HISTÓRICO DE SESSÕES (data/historico_sessoes.csv):
data,tema,resumo,resolvido
2026-01-10,Multiclasse,Dúvida sobre Guerreiro/Paladino,sim
2026-01-18,Talentos,Comparação entre Sentinel e Polearm Master,sim
2026-02-05,Equipamentos,Otimização de armaduras pesadas,sim
2026-02-20,Magias,Melhores magias defensivas para Paladino,sim

REGRAS DISPONÍVEIS (data/conteudo_regras.json):
[
  {
    "nome": "Paladino",
    "categoria": "classe",
    "funcao": "Tanque e suporte",
    "atributo_principal": "Carisma",
    "dificuldade": "media"
  },
  {
    "nome": "Guerreiro",
    "categoria": "classe",
    "funcao": "Combate direto",
    "atributo_principal": "Força",
    "dificuldade": "baixa"
  },
  {
    "nome": "Sentinel",
    "categoria": "talento",
    "funcao": "Controle de campo"
  },
  {
    "nome": "Polearm Master",
    "categoria": "talento",
    "funcao": "Ataques adicionais e controle"
  },
  {
    "nome": "Fireball",
    "categoria": "magia",
    "nivel": 3,
    "escola": "Evocação"
  }
]
---
```
## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
O contexto abaixo resume apenas as informações mais relevantes para responder às dúvidas do jogador, reduzindo o consumo de tokens sem perder contexto importante.

PERFIL DO JOGADOR:
- Nome: Carlos Andrade
- Experiência: Intermediário
- Sistema: D&D 5e
- Estilo de jogo: Combate tático
- Classes favoritas: Guerreiro e Paladino

PERSONAGENS ATIVOS:
- Arthos (Paladino Nível 8)
- Lyra (Maga Nível 5)
- Kael (Ranger Nível 6)

DÚVIDAS RECENTES:
- Multiclasse Guerreiro/Paladino
- Comparação de talentos defensivos
- Otimização de equipamentos
- Magias defensivas

CONTEÚDO DISPONÍVEL:
CLASSES:
- Paladino
- Guerreiro

TALENTOS:
- Sentinel
- Polearm Master

MAGIAS:
- Fireball

INSTRUÇÕES PARA O AGENTE:
- Priorize regras oficiais.
- Diferencie regras da casa de regras oficiais.
- Explique vantagens e desvantagens de cada build.
- Informe quando uma informação não estiver presente na base de conhecimento.
