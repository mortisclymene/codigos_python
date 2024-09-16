
print("Cadastro do Usuário 1")
login1 = input("Digite o login para o Usuário 1: ")


while True:
    senha1 = input("Digite a senha para o Usuário 1: ")
    if senha1 == login1:
        print("Erro: A senha não pode ser igual ao login. Tente novamente.")
    else:
        break

print("Usuário 1 cadastrado com sucesso!\n")


print("\nCadastro do Usuário 2")

while True:
    login2 = input("Digite o login para o Usuário 2: ")
    if login2 == login1:
        print("Erro: Esse login já foi escolhido pelo primeiro usuário. Escolha outro.")
    else:
        break


while True:
    senha2 = input("Digite a senha para o Usuário 2: ")
    if senha2 == login2:
        print("Erro: A senha não pode ser igual ao login. Tente novamente.")
    else:
        break

print("Usuário 2 cadastrado com sucesso!\n")


print("Usuários cadastrados:")
print(f"Usuário 1: Login = {login1}, Senha = {senha1}")
print(f"Usuário 2: Login = {login2}, Senha = {senha2}")
