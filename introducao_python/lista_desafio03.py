import math

# 9) Faça um algoritmo que calcule o volume de uma lata de óleo. Escreva o resultado.

raio = float(input("Informe o raio: "))
altura = float(input("Informe a altura: "))
volume = math.pi * raio ** 2 * altura

print(f"O volume é: {volume}")

# 10) Faça um algoritmo que leia as 3 notas de um aluno e calcule e escreva a média final deste aluno Considerar que a média é ponderada e que o peso das notas é: 2,3 e 5, respectivamente.

nota1 = float(input("Informe a nota 1:"))
nota2 = float(input("Informe a nota 2:"))
nota3 = float(input("Informe a nota 3:"))

media = (nota1 + nota2 + nota3) / 10

print(f"Média ponderada: {media}")

# 11) Faça um algoritmo que leia as coordenadas de dois pontos, P1 (x1, y1) e P2 (x2, y2) respectivamente, e calcule e escreva a distância entre eles.

x1 = float(input("Informe a coordenada x1: "))
y1 = float(input("Informe a coordenada y1: "))
x2 = float(input("Informe a coordenada x2: "))
y2 = float(input("Informe a coordenada y2: "))

d = math.sqrt(((x2 - x1)** 2) + ((y2 - y1) ** 2))

print(f"Distância: {d}")

# 12) Equação lineares

a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))
d = float(input("Informe o valor de d: "))
e = float(input("Informe o valor de e: "))
f = float(input("Informe o valor de f: "))


x = (c * e) - (b *f) / (a * e) - (b *d)
y = (a * f) - (c * d) / (a * e) - (b *d)

print(f"Valor de x: {x}\nValor de y: {y}")

# 13) O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor.

preco_fabrica = float(input("Informe o preço de fábrica: "))
preco_dist = 0.28 * preco_fabrica
preco_imp = 0.45 * preco_fabrica
preco_final = preco_fabrica + preco_dist + preco_dist
print(f"Preço final: {preco_final}")

# 14) Faça um algoritmo que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.

idade = int(input("Informe sua idade em dias: "))
anos = idade // 365
meses = (idade % 365) // 30
dias = (idade % 365) % 30

print(f"Idade: {anos} anos, {meses} meses e {dias} dias.")

# 15) Faça um algoritmo que leia o tempo de duração de um evento em uma fábrica expressa em segundos e mostre-o expresso em horas, minutos e segundos.

tempo_evento = float(input("Informe o tempo do evento em segundos: "))
horas = tempo_evento // 3600
minutos = (tempo_evento % 3600) // 60
segundos = (tempo_evento % 3600) % 60

print(f"O evento durou: {horas} horas, {minutos} minutos e {segundos} segundos.")

# 16) O governador acaba de liberar R$ 1.000.000.000,00 para construção de casas populares. Cada casa custa o equivalente a 90 salários mínimos. Faça um algoritmo que leia o valor do salário mínimo e calcule a quantidade de casas que podem ser construídas com o recurso liberado.

sal_minimo = float(input("Informe o valor do salário mínimo: "))
casa = sal_minimo * 90
total_casas = 1000000000 // casa
print(f"Quantidade de casas que podem ser construídas: {total_casas}")
