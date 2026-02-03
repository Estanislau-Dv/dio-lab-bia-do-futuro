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

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

[Sua descrição aqui]

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

[ex: Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt]

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[Sua descrição aqui]

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
