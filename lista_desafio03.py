import math

# Calcular volume do de uma lata de óleo.

raio = float(input("Informe o raio: "))
altura = float(input("Informe a altura: "))
volume = math.pi * raio ** 2 * altura

print(f"O volume é: {volume}")

# Calcular média ponderada de um aluno.

nota1 = float(input("Informe a nota 1:"))
nota2 = float(input("Informe a nota 2:"))
nota3 = float(input("Informe a nota 3:"))

media = (nota1 + nota2 + nota3) / 10

print(f"Média ponderada: {media}")

# Distância entre duas coordenadas.

x1 = float(input("Informe a coordenada x1: "))
y1 = float(input("Informe a coordenada y1: "))
x2 = float(input("Informe a coordenada x2: "))
y2 = float(input("Informe a coordenada y2: "))

d = math.sqrt(((x2 - x1)** 2) + ((y2 - y1) ** 2))

print(f"Distância: {d}")

# Equação lineares

a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))
d = float(input("Informe o valor de d: "))
e = float(input("Informe o valor de e: "))
f = float(input("Informe o valor de f: "))


x = (c * e) - (b *f) / (a * e) - (b *d)
y = (a * f) - (c * d) / (a * e) - (b *d)

print(f"Valor de x: {x}\nValor de y: {y}")

# Calcular preço final de carro ao consumidor.

preco_fabrica = float(input("Informe o preço de fábrica: "))
preco_dist = 0.28 * preco_fabrica
preco_imp = 0.45 * preco_fabrica
preco_final = preco_fabrica + preco_dist + preco_dist
print(f"Preço final: {preco_final}")

# Faça um algoritmo que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.

idade = int(input("Informe sua idade em dias: "))
anos = idade // 365
meses = (idade % 365) // 30
dias = (idade % 365) % 30

print(f"Idade: {anos} anos, {meses} meses e {dias} dias.")


