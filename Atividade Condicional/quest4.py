sex = float(input("Digite (1) para masculino ou (2) para feminino: "))
alt = float(input("Digite sua altura: "))



if sex == 1:
  conta = ((72.7 * alt) - 58) 
print(f"Seu peso ideal {conta} \n")

if sex == 2:
  conta = ((62.1 * alt) - 44.7) 
print(f"Seu peso ideal {conta} \n")
