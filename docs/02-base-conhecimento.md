# 📂 Base de Conhecimento

## 📂 Base de Dados Estruturada – RiscoIntel
A base de dados do agente é organizada para suportar planejamento financeiro, decisão de investimento, mitigação de riscos e alinhamento de interesses, reduzindo assimetria de informação e conflitos de agência.

| 📁 Arquivo                        | Formato | 🎯 Finalidade Estratégica no Agente
| --------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `perfil_investidor.json`          | JSON    | Contém informações pessoais, perfil de risco (Conservador, Moderado, Agressivo), horizonte de investimento, tolerância ao risco, objetivos financeiros e estratégia de crescimento. É usado pelo módulo de LLM e cálculos financeiros para alinhar recomendações ao usuário. |
| `produtos_financeiros.json`       | JSON    | Catálogo de ativos divididos entre Renda Fixa e Renda Variável, com risco, liquidez e retorno estimado. Permite que o agente sugira alocação coerente com o perfil e objetivos.                                                                                              |
| `indicadores_macroeconomicos.csv` | CSV     | Contém dados de inflação, juros, câmbio e desemprego, utilizados pelo gerenciador de contexto e cálculos financeiros para avaliar impactos externos nas decisões do usuário.                                                                                                 |
| `transacoes.csv`                  | CSV     | Registra receitas e despesas do usuário, classificadas por tipo e natureza (necessidade vs desejo). Permite análise de fluxo de caixa, avaliação de consumo consciente e cálculo de saldo disponível para investimento ou poupança.                                          |
                                                         |
                                                         
---

## 🛠️ Adaptações nos Dados do Agente RiscoIntel

Realizamos expansões estratégicas nos dados originais para que o agente RiscoIntel ofereça decisões financeiras mais inteligentes, personalizadas e seguras:

• Perfil do Investidor (perfil_investidor.json) – Inclui horizonte de investimento, tolerância ao risco e objetivos detalhados, permitindo recomendações altamente personalizadas.

• Produtos Financeiros (produtos_financeiros.json) – Ativos categorizados com risco, liquidez e retorno estimado, otimizando sugestões de alocação.

• Indicadores Macroeconômicos (indicadores_macroeconomicos.csv) – Dados de inflação, juros, câmbio e desemprego para análises de impacto externo e simulações financeiras.

• Transações (transacoes.csv) – Classificação de gastos em necessidades vs desejos, facilitando análise de fluxo de caixa e cálculo de saldo disponível para investimentos ou poupança.

> Essas melhorias tornam os dados mais coerentes, estratégicos e acionáveis, permitindo que o RiscoIntel mitigue riscos, reduza assimetrias de informação e guie o usuário em decisões financeiras inteligentes.
---

## 🔗 Estratégia de Integração e Carregamento de Dados do Agente RiscoIntel

O RiscoIntel foi projetado para integrar múltiplas fontes de dados financeiras e comportamentais, transformando essas informações em decisões inteligentes e personalizadas. A estratégia de integração segue quatro pilares principais:

1️⃣ Arquivo de Dados

• Os arquivos do usuário e do mercado (perfil_investidor.json, produtos_financeiros.json, indicadores_macroeconomicos.csv, transacoes.csv) são centralizados e normalizados para garantir consistência e qualidade.

• Cada dado é validado, permitindo que o agente trabalhe com informações confiáveis e prontas para análise.

2️⃣ Mapeamento e Alinhamento

• Cada arquivo é associado a funções específicas do agente:
>• perfil_investidor.json → Personalização de recomendações.
• produtos_financeiros.json → Sugestão de alocação de ativos.
• indicadores_macroeconomicos.csv → Ajuste de estratégias conforme cenário econômico.
• transacoes.csv → Avaliação de fluxo de caixa e saldo disponível.

• Essa integração garante decisões coerentes e alinhadas aos objetivos do usuário.

3️⃣ Pipeline de Carregamento

> Como os dados são carregados:
• Os arquivos JSON e CSV são carregados no início de cada sessão do agente.
• Os dados são processados e transformados em objetos estruturados, que podem ser rapidamente consultados durante a execução do LLM.
• Toda a informação relevante é incluída no contexto do prompt, permitindo que o agente tenha uma visão completa do usuário e do mercado para gerar respostas e recomendações precisas.

4️⃣ Contexto e Uso no Prompt

• Após o carregamento e transformação, os dados são injetados no contexto do LLM, criando um panorama completo que inclui:
> • Perfil do investidor e tolerância ao risco.
• Produtos financeiros disponíveis com risco, liquidez e retorno estimado.
• Indicadores macroeconômicos atuais.
• Histórico de transações e saldo disponível.

• O agente utiliza esse contexto para:

> • Insights, simulações
• recomendações financeiras inteligentes
• Sugestões proativas de investimento.

## 📝 Resumo Visual

| Etapa                          | Emoji | Função                                                        |
| ------------------------------ | ----- | ------------------------------------------------------------- |
| Arquivos de Dados              | 📁🛠️ | Fonte de informações do usuário e do mercado                  |
| Carregamento & Normalização    | 📥    | Transformação em objetos confiáveis, prontos para uso         |
| Mapeamento & Transformação     | 🧩    | Associação de dados aos módulos do agente                     |
| Inclusão no Contexto do Prompt | 💬    | Criação de contexto completo para o LLM                       |
| Decisão & Recomendação         | 🎯    | Insights, simulações e recomendações financeiras inteligentes |

> Essa estrutura garante que o RiscoIntel seja proativo, preciso e contextual, oferecendo recomendações financeiras confiáveis e alinhadas aos objetivos do usuário.
---

## 🧩 Exemplo de Contexto Montado do Agente RiscoIntel

```
{
  "perfil_investidor": {
    "nome": "Estanislau Pucuta",
    "idade": 30,
    "perfil_risco": "Moderado",
    "horizonte_investimento": "5 anos",
    "tolerancia_risco": "Média",
    "objetivos_financeiros": [
      "Comprar casa",
      "Aposentadoria confortável",
      "Reserva de emergência"
    ]
  },
  "produtos_financeiros": [
    {
      "nome": "CDB Banco XYZ",
      "tipo": "Renda Fixa",
      "risco": "Baixo",
      "liquidez": "Diária",
      "retorno_estimado": "8% a.a."
    },
    {
      "nome": "ETF Ações Global",
      "tipo": "Renda Variável",
      "risco": "Moderado",
      "liquidez": "Semanal",
      "retorno_estimado": "12% a.a."
    }
  ],
  "indicadores_macroeconomicos": {
    "inflacao": "6.2%",
    "juros": "11.5%",
    "cambio": "USD/AKZ 830",
    "desemprego": "7.8%"
  },
  "transacoes": [
    {
      "data": "2026-02-01",
      "tipo": "Receita",
      "categoria": "Salário",
      "valor": 150000,
      "natureza": "Necessidade"
    },
    {
      "data": "2026-02-05",
      "tipo": "Despesa",
      "categoria": "Lazer",
      "valor": 5000,
      "natureza": "Desejo"
    }
  ]
}
```
🧠 Como o agente utiliza este contexto

1. Inclusão no Contexto do Prompt:
> • Todos os dados são carregados no início da sessão, permitindo que o LLM tenha uma visão completa do usuário e do mercado.

2. Consultas Dinâmicas:
> • Durante a interação, o agente acessa e filtra informações do contexto para gerar recomendações personalizadas.
> • Ex.: “Com base no seu perfil moderado e saldo disponível, sugiro alocar 60% em renda fixa e 40% em ETFs de ações.”

2. Simulações e Alertas de Risco:

> • Indicadores macroeconômicos ajudam o agente a avaliar impactos externos sobre a carteira.
> • Histórico de transações permite analisar padrões de consumo e fluxo de caixa, sugerindo otimizações.
