nome = input("Informe seu nome: ")
end = input("Informe seu endereço: ")
idade = input("Informe sua idade: ")

# Exibindo dados das variáveis
print(nome, end, idade)

#1 forma de concatenação
print("\nOlá",nome," seu endereço é ",end," sua idade é ", idade)

#2 forma de concatenação
print("\nOlá {} seu endereço é {} sua idade é , {}".format(nome,end, idade))

#2 forma de concatenação
print(f"Bem vindo{nome}, voce mora na {end} e tem {idade}")