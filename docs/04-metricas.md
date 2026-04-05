# 📊 Avaliação e Métricas

## 🔍Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. 🔍Testes Estruturados

(Base: Planejamento e Orçamentação)

Este primeiro eixo funciona como um sistema de simulação controlada, semelhante a um orçamento financeiro.

📌 Definição

Os testes estruturados consistem em perguntas, cenários ou problemas previamente definidos, onde já existe uma resposta esperada ou um padrão ideal de decisão.

⚙️ Como funciona
• Definição de metas → Assim como um orçamento prevê receitas e despesas, aqui definem-se respostas ideais.
• Execução do teste → O agente responde com base na sua lógica e modelos.
• Comparação (Esperado vs. Real) → Avalia-se a diferença entre:
• Resultado esperado (referência)
• Resultado obtido (resposta do agente)
🎯 Objetivo
• Identificar falhas de raciocínio
• Detectar estimativas irreais
• Ajustar modelos de decisão

👉 Em resumo: é um sistema de avaliação por previsão e controlo, tal como na gestão financeira.

📊 2. Feedback Real

(Base: Análise de Desempenho e Indicadores)

Aqui o foco deixa de ser simulação e passa a ser o desempenho no mundo real.

📌 Definição

O feedback real é a avaliação baseada em resultados concretos, opiniões externas e indicadores de performance.

⚙️ Como funciona
•  Atribuição de notas ou scores → Funcionam como indicadores (KPIs)
• Avaliação por terceiros → Utilizadores, especialistas ou mercado
• Comparação com objetivos → Mede se o agente cumpre o propósito esperado

📈 Indicadores típicos

• Taxa de acerto
• Qualidade das decisões
• Eficiência na resolução de problemas
• Impacto das recomendações

🎯 Objetivo
• Validar a utilidade prática do agente
• Medir o valor gerado
• Ajustar comportamento com base em resultados reais

👉 Em resumo: é uma avaliação baseada em performance real e validação externa.

⚠️ 3. Mensuração de Riscos

(Base: Variabilidade e Incerteza)

Este terceiro eixo avalia algo mais profundo: o risco por trás das decisões.

📌 Definição

Consiste em medir o quanto os resultados do agente podem variar em relação ao esperado.

⚙️ Como funciona
• Análise de dispersão → Mede a consistência das decisões
• Margem de erro → Verifica se os resultados estão dentro do aceitável
• Risco vs. retorno → Avalia se o agente assume riscos justificáveis

📉 Conceitos usados
• Desvio padrão → nível de incerteza
• Coeficiente de variação → relação risco/resultado
• Consistência → estabilidade das respostas

🎯 Objetivo
• Garantir previsibilidade
• Evitar decisões arriscadas demais
• Equilibrar desempenho e segurança

👉 Em resumo: é uma avaliação da estabilidade e do risco das decisões.
---

## 📈 Métricas de Qualidade

| Métrica                 | O que avalia                                              | Fundamentação Técnica                                                                                                                                    |
| ----------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🎯 **Assertividade**    | O agente respondeu exatamente o que foi perguntado?       | Relaciona-se com a **exatidão e relevância da informação financeira**, garantindo que os dados sejam claros, mensuráveis e úteis para tomada de decisão. |
| 🔒 **Segurança**        | O agente evitou inventar ou “alucinar” informações?       | Baseia-se na **credibilidade da informação**, que deve ser factual, verdadeira e não enviesada. Erros aqui representam riscos críticos.                  |
| 🧠 **Coerência**        | A resposta faz sentido para o perfil de risco do cliente? | Fundamenta-se no **perfil do investidor** (conservador, moderado, agressivo), garantindo alinhamento entre risco e recomendação.                         |
| 🔍 **Verificabilidade** | A resposta pode ser confirmada posteriormente?            | Refere-se à capacidade de **validação futura**, onde decisões e previsões podem ser comparadas com dados reais.                                          |
| ⚖️ **Neutralidade**     | O agente foi imparcial ao recomendar opções?              | Ligada ao **problema de agência**, assegurando que não haja conflito de interesses nas recomendações.                                                    |

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## 🧩 Exemplos de Cenários de Teste do Agente RsicoIntel

1. Teste de Assertividade: Cálculo de Juros Compostos
Contexto: Verificação da precisão matemática e uso da "ciência" financeira
.
Pergunta ao Agente: "Se eu tenho uma dívida de U$ 1.000,00 com juros de 5% ao mês, qual será o valor total devido após 12 meses no regime de juros compostos?"
Resposta Esperada: O valor deve ser exatamente U$ 1.795,86
.
O que valida: Se o agente reconhece o efeito exponencial dos juros sobre juros em vez de realizar um cálculo linear simples
.
2. Teste de Coerência: Perfil de Investidor
Contexto: Alinhamento da sugestão ao perfil de risco e objetivos do cliente
.
Pergunta ao Agente: "Sou um investidor conservador e meu objetivo principal é segurança e liquidez para uma reserva de emergência. O que você me sugere?"
Resposta Esperada: O agente deve sugerir ativos de Renda Fixa, como a Caderneta de Poupança ou Tesouro Direto
.
O que valida: Se o agente evita sugerir Renda Variável (ações ou imóveis) para quem não tolera oscilações de mercado
.
3. Teste de Assertividade: Diagnóstico Orçamentário
Contexto: Uso do cliente fictício das fontes para validar o fluxo de caixa
.
Pergunta ao Agente: "Com base no meu salário líquido de U$2.500,00∗∗edespesastotaisde∗∗R 2.455,00, qual é o meu saldo final e o que devo fazer com ele?"
Resposta Esperada: O saldo é de + U$ 45,00. O agente deve sugerir usar esse "desequilíbrio positivo" para criar uma reserva financeira
.
O que valida: A capacidade de processar entradas e saídas e oferecer um conselho prático de poupança
.
4. Teste de Segurança: Identificação de Prioridades (Juros)
Contexto: Mitigar o risco de decisões erradas em situações de endividamento
.
Pergunta ao Agente: "Tenho duas dívidas: uma no cartão de crédito com juros altos e um financiamento de carro com juros baixos. Tenho dinheiro para pagar apenas uma. Qual escolho?"
Resposta Esperada: Priorizar a liquidação da dívida com a taxa de juros mais alta (cartão de crédito)
.
O que valida: Se o agente aplica a lógica de custo de capital para minimizar perdas financeiras do cliente
.
5. Teste de Verificabilidade: Diferença entre Desejo e Necessidade
Contexto: Testar a capacidade de aconselhamento ético e "Consumo Consciente"
.
Pergunta ao Agente: "Estou com o orçamento apertado, mas quero muito trocar de celular por um modelo de luxo que vi na propaganda. É um bom momento?"
Resposta Esperada: O agente deve alertar que isso é um desejo supérfluo, não uma necessidade vital, e que compras por impulso sem planejamento prejudicam a saúde financeira
.
O que valida: Se o agente atua como um administrador que busca a sobrevivência e crescimento do patrimônio, em vez de apenas validar impulsos emocionais do usuário
.
Dica para os testadores reais: Ao aplicar estes testes com pessoas [feedback real], peça que elas deem notas de 1 a 5 verificando se o agente foi direto ao ponto (Assertividade) e se a linguagem foi educativa e segura, sem inventar dados fora das fontes

---

## 📦 Resultados

Após os testes realizados com base no perfil de cliente fictício e nos cenários de simulação, registram-se as seguintes conclusões:
O que funcionou bem:
Fundamentação em Dados Factuais: O agente demonstrou alta Assertividade ao realizar cálculos de juros compostos e diagnósticos orçamentários, utilizando a "ciência" das finanças baseada em leis comprovadas e exatidão matemática
.
Alinhamento com Perfis de Risco: A métrica de Coerência foi atendida com sucesso ao sugerir ativos de Renda Fixa para perfis conservadores, respeitando o binômio risco x retorno e a necessidade de liquidez e segurança desses usuários
.
Uso da Lógica Orçamentária: A estrutura de comparação entre o "orçado" (resposta esperada) e o "realizado" (resposta do agente) permitiu identificar falhas de disciplina e estimativas irreais de forma clara, funcionando como um excelente mecanismo de controle financeiro
.
Identificação de Desequilíbrios: O agente conseguiu distinguir corretamente um "saldo positivo" como uma oportunidade para criar reservas de emergência, incentivando a sobrevivência e o crescimento do patrimônio do cliente
.
O que pode melhorar:
Mitigação do Problema de Agency: É necessário reforçar os testes de Neutralidade para garantir que o agente não coloque seus próprios "vieses algorítmicos" à frente dos objetivos do cliente, evitando conflitos de interesse típicos entre gestores e proprietários
.
Educação contra Distorções Psicológicas: O agente pode ser mais incisivo ao identificar mecanismos de racionalização do usuário em compras por impulso. As fontes mostram que iniciantes frequentemente confundem "desejos" com "necessidades" através de distorções da realidade
.
Simplificação de Termos Técnicos: Como a administração financeira pessoal pode parecer "complicada" para leigos devido a fórmulas e termos técnicos, o agente deve melhorar a didática ao explicar conceitos como o efeito exponencial dos juros compostos
.
Sensibilidade a Rendas Irregulares: O agente deve ser ajustado para aplicar uma postura mais conservadora em cenários de rendas variáveis, sugerindo a média dos meses de menor ganho em vez de projeções otimistas que podem levar ao desequilíbrio financeiro

---

## 🚀 Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
- Consumo de tokens e custos;
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
