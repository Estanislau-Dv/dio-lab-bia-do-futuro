# 📊 Avaliação e Métricas

## 🔍Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. Testes Estruturados

(Base: Planejamento e Orçamentação)

Este primeiro eixo funciona como um sistema de simulação controlada, semelhante a um orçamento financeiro.

📌 Definição

Os testes estruturados consistem em perguntas, cenários ou problemas previamente definidos, onde já existe uma resposta esperada ou um padrão ideal de decisão.

⚙️ Como funciona
Definição de metas → Assim como um orçamento prevê receitas e despesas, aqui definem-se respostas ideais.
Execução do teste → O agente responde com base na sua lógica e modelos.
Comparação (Esperado vs. Real) → Avalia-se a diferença entre:
Resultado esperado (referência)
Resultado obtido (resposta do agente)
🎯 Objetivo
Identificar falhas de raciocínio
Detectar estimativas irreais
Ajustar modelos de decisão

👉 Em resumo: é um sistema de avaliação por previsão e controlo, tal como na gestão financeira.

---

## 📈 Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## 🧩 Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** Valor baseado no `transacoes.csv`
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil do cliente
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [ ] Correto  [ ] Incorreto

---

## 📦 Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- [Liste aqui]

**O que pode melhorar:**
- [Liste aqui]

---

## 🚀 Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
- Consumo de tokens e custos;
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
