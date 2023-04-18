# Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print("Olá mundo!")

# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

num = float(input("Informe um número: "))
print(f"O número informado foi {num}")

# Faça um Programa que peça dois números e imprima a soma.

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

print(f"A soma é {num1 + num2}")

# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
n3 = float(input("Informe a terceira nota: "))
n4 = float(input("Informe a quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4

print(f"A média é: {media}")

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input("Informe o valor da hora trabalhada: "))
hora_mes = float(input("Informe a quantidade de horas trabalhadas no mês: "))
salario = valor_hora * hora_mes
print(f"O seu salário do mês será de: {salario}")

"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a. o produto do dobro do primeiro com metade do segundo .
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo.
"""

num1_int = int(input("Digite um número inteiro: "))
num2_int = int(input("Digite um número inteiro: "))
num_real = float(input("Informe um número real: "))

produto = (num1_int * 2) + (num2_int / 2)
soma = (num1_int * 3) + num_real
cubo_real = num_real ** 3

print(f"Produto: {produto}\nSoma: {soma}\nCubo: {cubo_real}")

# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58.

altura = float(input("Informe a sua altura: "))
peso_ideal = (72.7 * altura) - 58
print(f"Seu peso ideal é: {peso_ideal}")

"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto
de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
"""

valor_hora = float(input("Informe o valor da hora trabalhada: "))
hora_mes = float(input("Informe a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * hora_mes
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
sal_liquido = salario_bruto - (imposto_renda + inss + sindicato)

print(f"Salário bruto: {salario_bruto}\nImposto de renda: {imposto_renda}\nINSS:{inss}\nSindicato: {sindicato}\nSalário líquido: {sal_liquido}")

"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é
vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total.
"""

area = float(input("Informe a área a ser pintada: "))
litros = area / 3
latas = litros / 18
preco = latas * 80

print(f"Você precisará de {latas} latas de tinta e o preço total será de R$ {preco}")

"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é
vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre
- arredonde os valores para cima, isto é, considere latas cheias.
"""

area = float(input("Informe a área a ser pintada: "))
litros = area / 6
latas = litros / 18
galoes = litros / 3.6
preco_latas = latas * 80
preco_galoes = galoes * 25

print(f"Você precisará de {latas} latas de tinta e o preço total será de R$ {preco_latas}")
print(f"Você precisará de {galoes} galões de tinta e o preço total será de R$ {preco_galoes}")


"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de
Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em
minutos).
"""

tamanho_arquivo = float(input("Informe o tamanho do arquivo em MB: "))
velocidade_net = float(input("Informe a velocidade da internet em Mbps: "))

tempo_download = tamanho_arquivo / velocidade_net

print(f"O tempo aproximado de download é de {tempo_download} minutos")