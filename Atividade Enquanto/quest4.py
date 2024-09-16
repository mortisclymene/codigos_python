while True:
    nome = input("Digite um nome completo (nome e sobrenome): ")

    if len(nome) > 15:
        print(f"Nome aceito: {nome}")
        break
    else:
        print("Erro: O nome deve ter mais de 15 letras. Tente novamente.")

