animais = ['Cachorro','Gato','Tiktalik']
print(type(animais)) #exibindo o tipo da variável

print(animais)

print('-'*50)
#Estamos exibindo todos os itens da lista 'animais'
for elementos in animais:
    print(elementos)
















#3 etapa: Excluir itens na lista
print('-'*50)

#forma 1 - usando pop()
animais.pop()# irá excluir sempre o último item
print(animais)

#forma 2 - usando pop() com índice
animais.pop(0)#Aqui iremos escpçj