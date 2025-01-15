# questao3.py
import json

def analisar_faturamento(dados_faturamento):
    valores = [dia['valor'] for dia in dados_faturamento if dia['valor'] > 0]
    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    media_mensal = sum(valores) / len(valores)
    dias_acima_media = sum(1 for dia in dados_faturamento if dia['valor'] > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_media

with open('dados.json', 'r') as file:
    faturamento_mensal = json.load(file)


menor, maior, dias = analisar_faturamento(faturamento_mensal)
print(f"Menor faturamento: R$ {menor:.2f}")
print(f"Maior faturamento: R$ {maior:.2f}")
print(f"Dias com faturamento acima da média: {dias}")