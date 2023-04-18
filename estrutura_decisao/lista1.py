# Ler um valor e escrever se é positivo, negativo ou zero.

num = float(input("Informe o número: "))
if num > 0:
    print(f"O número {num} é positivo")
elif num < 0:
    print(f"O número {num} é negativo") 
elif num == 0:
    print(f"O número {num} é igual que 0") 
