numeros = []

while True:
    valor = int(input("Digite um valor (0 para encerrar): "))
    if valor == 0:
        break
    numeros.append(valor)


print("Lista original:", numeros)


numeros_impares = []
for numero in numeros:
    if numero % 2 != 0:
        numeros_impares.append(numero)

print("Lista sem números pares:", numeros_impares)