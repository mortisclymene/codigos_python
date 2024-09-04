sal = float(input("Digite seu salário: "))

aum = 30/100

if sal <= 600:
    conta = sal * aum
    print(f"Quantidade total: {sal} + {conta}")
else:
    print("Você não tem direito ao aumento.")