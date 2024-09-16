contagem_impares = 0

while True:
    numero = int(input("Digite um valor numérico (ou 0 para parar): "))
    
    if numero == 0:
        break
    
    if numero % 2 != 0:
        contagem_impares += 1

print(f"Quantidade de números ímpares digitados: {contagem_impares}")