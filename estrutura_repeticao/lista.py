"""Faça um algoritmo que:
• leia 5 números inteiros;
• escreva os números que são negativos;
• escreva a média dos números positivos."""

media = []
for num in range(3):
    num = int(input("Digite um número: "))
    if num < 0:
        print(f"O número {num} é negativo.")
    else:
        num > 0
        media.append(num)
        print(f"O número {num} é positivo.")

print(f"A média dos números positivos é {sum(media)/len(media)}")


"""Faça um algoritmo que leia 15 números inteiros e escreva, para cada número lido, se é
par ou ímpar."""

for num in range(16):
    num = int(input("Digite um número: "))
    if num % 2 == 0: 
        print(f"O número {num} é par.")
    else:
        print(f"O número {num} é ímpar.")

"""Faça um algoritmo que calcule e escreva a soma dos números pares e a soma dos
números ímpares entre 1 e 100."""

par = []
impar = []
for num in range(101):
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f"Soma dos números pares: {sum(par)}")
print(f"Soma dos números ímpares: {sum(impar)}")

"""Faça um algoritmo que leia a altura de 20 pessoas e calcule a média aritmética das
alturas."""

alturas = []
for altura in range(21):
    altura = float(input("Informe a sua altura: "))
    alturas.append(altura)
print(f"A média das alturas é {sum(alturas)/len(alturas)}")

"""Faça um algoritmo que leia n valores inteiros e escreva quantos desses valores são
negativos."""

n = int(input("Informe o valor de n: "))
for num in range(n):
    if num < 0:
        print(f"{n} é negativo")
    else:
        pass
