# 📂 Base de Conhecimento

## 📂 Base de Dados Estruturada – RiscoIntel
A base de dados do agente é organizada para suportar planejamento financeiro, decisão de investimento, mitigação de riscos e alinhamento de interesses, reduzindo assimetria de informação e conflitos de agência.

| 📁 Arquivo                      | 🎯 Finalidade Estratégica no Agente                                                                                                                                                                                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`perfil_investidor.json`**    | Classifica o usuário segundo o **perfil de risco (Conservador, Moderado ou Agressivo)**, horizonte temporal e objetivos financeiros. Garante que recomendações estejam alinhadas à **tolerância ao risco**, preservação de capital ou maximização de retorno. |
| **`produtos_financeiros.json`** | Contém o catálogo estruturado de ativos de **Renda Fixa (CDB, Tesouro, Poupança)** e **Renda Variável (Ações, Fundos, Imóveis)**. Permite ao agente sugerir **alocação eficiente de capital**, respeitando o perfil do investidor e o cenário macroeconômico. |
| **`transacoes.csv`**            | Base para diagnóstico do **fluxo de caixa**, análise de padrões de consumo e organização orçamentária. Apoia a distinção rigorosa entre **necessidades e desejos**, prevenindo endividamento por impulso.                                                     |
| **`historico_atendimento.csv`** | Registro de interações anteriores e decisões passadas. Utilizado para análise comportamental, correção de desvios financeiros e construção de planejamento orientado ao futuro com base no passado.                                                           |


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
