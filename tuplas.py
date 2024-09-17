#Trabalhando com Tuplas

objetos = ("lápis", "Borracha","Caderno")

print(type(objetos))# a função type() irá exibir o tipo de variáveç 'objetos', nesse caso irá aparecer 'tuple'

print(objetos)
print(objetos[1])# estamos exibindo apenas um item, que está na posuição 1

# Exibido todos os dados da tupla
print('-'*50)

for item in range(0,3):
    print(objetos[item])

# Exibido todos os dados sem a função range
print('-'*50)

for item in objetos:
    print(item)

# Tentando mudar o conteúdo da tupla
print('-'*50)

objetos[0] = "Caneta" #Irá ocorrer um erro pois os valores de uma tupla são imutáveis
print(objetos)
