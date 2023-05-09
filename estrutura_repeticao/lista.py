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

num_maior = int(input("Informe o maior valor: "))
num_menor = int(input("Informe o menor valor: "))
for num in range(num_menor, num_maior):
    if num_menor > num_maior:
        raise "Error"
    elif num < 0:
        print(f"{num}")

"""Faça um algoritmo que leia a quantidade de tinta que uma caneta, e enquanto a
caneta tiver tinta para escrever, escreva “Enquanto tem tinta a caneta escreve...”.
Considere que a cada comando de escrita a caneta gasta 2% da tinta que possui."""

quant_tinta = int(input("Informe a quantidade de tinta: "))
while quant_tinta != 0:
    quant_tinta += -2
    print("Tá escrevendo...")    

"""Faça um algoritmo que leia n pares de valores, sendo o primeiro valor o número de
inscrição do atleta e o segundo a altura (em cm) do atleta. Escreva:
• o número de inscrição e a altura do atleta mais alto;
• o número de inscrição e a altura do atleta mais baixo;
• a altura média do grupo de atletas."""

inscricoes = []
alturas = []

for i in range(3):
    inscricao = float(input("Informe a inscrição: "))
    altura = float(input("Informe a altura: "))
    inscricoes.append(inscricao)
    alturas.append(altura)

indice_mais_alto = alturas.index(max(alturas))
indice_mais_baixo = alturas.index(min(alturas))

inscricao_mais_alto = inscricoes[indice_mais_alto]
inscricao_mais_baixo = inscricoes[indice_mais_baixo]

print(f"Média das alturas: {sum(alturas) / len(alturas)}")
print(f"Atleta mais alto: Altura={max(alturas)}, Inscrição={inscricao_mais_alto}")
print(f"Atleta mais baixo: Altura={min(alturas)}, Inscrição={inscricao_mais_baixo}")

"""Construir um algoritmo que calcule o fatorial de um número N."""

fatorial = int(input("Informe um valor: "))
for num in range(1, fatorial):
    fatorial *= num
print(fatorial)

"""Faça um algoritmo que calcule e escreva a soma da seguinte série de 100 termos:"""

count = []
for num in range(1,101):
    count.append(num)
print(sum(count))


"""Faça um algoritmo que calcule e escreva a soma da seguinte série de 100 termos:"""
count = []
for num in range(1,101):
    a = 1/num
    count.append(a)
print(sum(count))


