valor_compra = float(input("Digite o valor da compra: "))
qtd_parcelas = int(input("Digite a quantidade de parcelas de 1 à 24: "))

if qtd_parcelas <= 12:
    valorparcela = valor_compra / qtd_parcelas
    print(f"O valor total da compra é {valor_compra} e o valor de cada parcela é {qtd_parcelas}")