valor = float(input("Informe um valor númerico: "))

if valor > 200:
    print (f"Este valor não está entre 100 e 200\n")
if valor < 100 :
    print (f"Este valor não está entre 100 e 200\n")
#elif é o mesmo que else if, junção dos dois
elif valor >= 100 and valor < 200:
    print (f"O número {valor} está entre 100 e 200\n")