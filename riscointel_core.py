import json
import pandas as pd

# 1. Carregar perfil do investidor

def carregar_perfil(caminho="data/perfil_investidor.json"):
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

# 2. Carregar produtos financeiros

def carregar_produtos(caminho="data/produtos_financeiros.json"):
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

# 3. Carregar indicadores macroeconômicos
def carregar_indicadores(caminho="data/indicadores_macroeconomicos.csv"):
    return pd.read_csv(caminho)
    
# 4. Carregar transações

def carregar_transacoes(caminho="data/transacoes.csv"):
    return pd.read_csv(caminho)

# 5. Diagnóstico de fluxo de caixa

def diagnostico_fluxo_caixa(df_transacoes):
    receitas = df_transacoes[df_transacoes['tipo'] == 'Receita']['valor'].sum()
    despesas = df_transacoes[df_transacoes['tipo'] == 'Despesa']['valor'].sum()
    saldo = receitas - despesas

    desejos = df_transacoes[df_transacoes['natureza'] == 'Desejo']['valor'].sum()
    percentual_desejos = (desejos / despesas) * 100 if despesas > 0 else 0

    return saldo, percentual_desejos

# 6. Geração de recomendações

def gerar_recomendacao(perfil, saldo, produtos):
    print(f"\n--- Diagnóstico RiscoIntel para {perfil['usuario']} ---")
    print(f"Perfil: {perfil['perfil']} | Objetivo: {perfil['objetivo_principal']}")
    print(f"Saldo Mensal: R$ {saldo:.2f}")

    if saldo > 0:
        print(f"Ação: Direcionar excedente para produtos adequados ao perfil {perfil['perfil']}:")
        for p in produtos:
            if perfil['perfil'] == "Conservador" and p['familia'] == "Renda Fixa":
                print(f"- {p['ativo']} ({p['risco']})")
            elif perfil['perfil'] == "Moderado":
                print(f"- {p['ativo']} ({p['risco']})")
            elif perfil['perfil'] == "Agressivo" and p['familia'] == "Renda Variável":
                print(f"- {p['ativo']} ({p.get('potencial_retorno', 'N/A')})")
    else:
        print("Ação: Reduzir despesas variáveis e desejos imediatamente.")
        
# 7. Execução principal

if __name__ == "__main__":
    perfil = carregar_perfil()
    produtos = carregar_produtos()
    indicadores = carregar_indicadores()
    transacoes = carregar_transacoes()

    saldo, percentual_desejos = diagnostico_fluxo_caixa(transacoes)
    print(f"Alerta: {percentual_desejos:.1f}% das despesas são desejos.\n")

    gerar_recomendacao(perfil, saldo, produtos)
