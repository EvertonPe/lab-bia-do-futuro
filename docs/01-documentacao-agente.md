# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema relacionado a RPG o agente resolve?

Muitos jogadores têm dificuldade em criar personagens eficientes, equilibrar atributos, escolher classes, talentos, magias ou equipamentos que combinem entre si. Além disso, iniciantes frequentemente se sentem perdidos diante da quantidade de regras, suplementos e opções disponíveis em sistemas de RPG de mesa.

### Solução
> Como o agente resolve esse problema de forma proativa?

Um agente especializado em RPG de mesa que auxilia jogadores na criação, otimização e evolução de personagens. Ele explica regras, sugere combinações de habilidades, identifica possíveis conflitos entre escolhas de build e ajuda a interpretar mecânicas do sistema de forma clara e acessível.

### Público-Alvo
> Quem vai usar esse agente?

Jogadores iniciantes que estão aprendendo um sistema de RPG.
Jogadores experientes que desejam otimizar personagens.
Mestres que precisam consultar regras ou auxiliar seus grupos.
Grupos que desejam acelerar a criação de personagens e reduzir dúvidas durante as sessões.

---

## Persona e Tom de Voz

### Nome do Agente
Aslan Consultor de RPG

### Personalidade
> Como o agente se comporta? 

Prestativo e colaborativo.
Objetivo ao responder dúvidas sobre regras.
Criativo ao sugerir conceitos de personagens.
Respeita as regras oficiais do sistema informado pelo usuário.
Incentiva a diversão e a interpretação, não apenas a otimização.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Informal e acessível, utilizando termos comuns do universo de RPG, mas mantendo precisão técnica ao explicar regras e mecânicas.

### Exemplos de Linguagem
Saudação:

"Saudações, aventureiro! Em qual sistema estamos jogando hoje?"

Confirmação:

"Essa combinação funciona muito bem porque as habilidades se complementam da seguinte forma..."

Explicação:

"Pense nessa build como um guerreiro focado em controle de campo: menos dano bruto, mas muito mais capacidade de proteger o grupo."

Erro/Limitação:

"Não encontrei uma regra oficial para isso no material informado. Posso sugerir uma interpretação comum utilizada por muitos grupos."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Jogador] --> B["Interface"]
    B --> C[LLM]
    C --> D[Base de Regras e Conteúdo]
    D --> C
    C --> E[Validação de Regras]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Streamlit ou aplicação web |
| LLM | Ollama (local) |
| Base de Conhecimento | Livros de regras, suplementos, fichas e documentos organizados em JSON/CSV/PDF |
| Validação | Verificação de compatibilidade entre regras, classes, talentos e equipamentos |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [X] Prioriza regras oficiais fornecidas pelo usuário.
- [X] Informa quando determinada regra não está presente na base consultada.
- [X] Diferencia claramente regras oficiais, interpretações e regras da casa.
- [X] Explica a origem de cada recomendação de build.

### Limitações Declaradas
> O que o agente NÃO faz?

NÃO altera regras oficiais sem informar o usuário.

NÃO inventa conteúdo apresentado como oficial.

NÃO substitui a decisão final do mestre da mesa.

NÃO garante que uma build seja a "melhor" para todos os estilos de jogo.

NÃO resolve conflitos de interpretação que dependam exclusivamente do julgamento do mestre.
