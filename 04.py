faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}


faturamento_total = sum(faturamento_por_estado.values())

for estado, valor in faturamento_por_estado.items():
    porcentagem = (valor/faturamento_total) * 100
    print(f"O percentual de faturamento de {estado} foi de {porcentagem:.2f}%.") 