# Retorna das despesas
def calcular_total_despesas(despesas):
    return sum(despesa.valor for despesa in despesas)
