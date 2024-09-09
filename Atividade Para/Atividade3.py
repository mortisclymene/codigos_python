num = int(input("Digite o número: "))
print("Os divisores de", num, "são: ")

for div in range(1, num + 1):
    if num % div == 0:
        print('{}'.format(div), end=" ")
