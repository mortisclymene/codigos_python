'''
for (contador = 1; contador <=5; contador++){


}
'''

#1 exemplo
for contador in range(1,6):
    print(contador)

#2 exemplo
for contador in range(1,11,2):# o 3 parametro ira aumentar  os valores que estao sendo exibidos
    print(contador)

print("-"*30)
#3 exemplo - numeros do maior para o menor
for contador in range('10,0,-1'):
    print(contador,end=" ")