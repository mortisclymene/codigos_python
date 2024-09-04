sal = int(input("Informe o valor de seu salário: "))
fin = int(input("Informe o valor de seu financiamento: "))

if fin <= sal * 5:
    print ("Financiamento Concedido\nObrigado por nos consultar")

else:
    print("Financiamento Negado\nObrigado por nos consultar")