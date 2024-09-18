
valores = []
for i in range (7): 
    numero = int(input(f"Digite o {i+1}º número: "))
    valores.append(numero)

imp = 0
for numero in valores:
    if numero % 2 != 0:
        imp += 1
        
print(f"Existem {imp} números ímpares")