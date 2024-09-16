soma_positivos = 0
contagem_negativos = 0
contador = 0 

while contador < 10:
    numero = int(input(f"Digite o {contador + 1}º valor inteiro: "))
    

    if numero > 0:
        soma_positivos += numero

    elif numero < 0:
        contagem_negativos += 1
    

    contador += 1

print(f"\nSoma dos números positivos: {soma_positivos}")
print(f"Quantidade de valores negativos: {contagem_negativos}")
