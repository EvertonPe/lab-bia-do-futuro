# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Definir cenários de RPG e verificar se o agente responde corretamente com base nas regras e na base de conhecimento;
2. **Feedback real:** Jogadores e mestres utilizam o agente durante a criação de personagens ou consulta de regras e avaliam a experiência.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Precisão das Regras** | O agente interpreta corretamente as regras do sistema? | Perguntar uma mecânica específica e verificar se a resposta corresponde ao livro de regras |
| **Segurança** | O agente evita inventar regras ou conteúdo oficial inexistente? | Perguntar sobre uma classe inexistente e verificar se ele admite não possuir a informação |
| **Coerência** | A resposta faz sentido para o personagem e contexto fornecidos? | Sugerir talentos compatíveis com a classe e atributos do personagem |
| **Utilidade** | A resposta ajuda o jogador a resolver seu problema? | Solicitar uma build e verificar se a explicação é prática e compreensível |
| **Personalização** | O agente utiliza corretamente os dados do jogador e da ficha? | Recomendar melhorias considerando o nível, classe e estilo de jogo informados |
---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta sobre Personagem
- **Pergunta:** "Qual é o personagem de nível mais alto da minha lista?"
- **Resposta esperada:** Arthos, Paladino nível 8 (baseado em personagens.csv)
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Quais talentos combinam com meu Paladino?"
- **Resposta esperada:** O agente apresenta talentos compatíveis e explica suas sinergias.
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual será a previsão do tempo amanhã?"
- **Resposta esperada:** O agente informa que é especializado em RPG de mesa.
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 4: Regra Não Disponível
- **Pergunta:** "Como funciona a classe Cavaleiro Arcano Supremo?"
- **Resposta esperada:** O agente informa que não encontrou essa informação na base de conhecimento.
- **Resultado:** [X] Correto  [ ] Incorreto

