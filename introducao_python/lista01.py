#Faça um programa que peça dois números inteiros e imprima a soma desses dois números.

num1 = int(input('Informe o primeiro o número: '))
num2 = int(input('Informe o segundo o número: '))

soma = num1 + num2

print(f"A soma é: {soma}")

#Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

metros = float(input("Infome um valor em metros: "))
milimetros = metros * 1000
print(f"O valor em milímetros é: {milimetros}mm")

# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dia = int(input("Informe a quantidade de dias: "))
horas = int(input("Informe a quantidade de horas: "))
minutos = int(input("Informe a quantidade de minutos: "))
segundos = int(input("Informe a quantidade de segundos: "))

total = segundos + (minutos * 60) + (horas * 3600) + (dia * 86400)
print(f"O total de segundos é: {total}s")

# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("Informe seu salário: "))
porcentagem = float(input("Informe a porcentagem de aumento do salário: "))

aumento = (salario * porcentagem) / 100
novo_salario = salario + aumento

print(f"O aumento no salário é de: R${aumento}\nO novo salário será de: R${novo_salario}")

# Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

produto = float(input("Informe o valor da mercadoria: "))
porcentagem = float(input("Informe o valor do desconto: "))

desconto = (produto * porcentagem) / 100
novo_preco = produto - desconto

print(f"O desconto será de: {desconto}\nO novo preço do produto será de: {novo_preco}")

# Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = float(input("Informe a distância percorrida: "))
vel_media = float(input("Informe a velocidade média percorrida: "))

tempo = distancia / vel_media

print(f"O tempo gasto na viagem é de: {tempo}h")

# Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32 . Faça agora o contrário, de Fahrenheit para Celsius.

temp_celcius = float(input("Informe uma temperatura em Celcius: "))
conv_fahrenheit = round((temp_celcius * 1.8) + 32,2)
print(f"A temperatura em Fahrenheit é: {conv_fahrenheit}")

temp_fahrenheit = float(input("Informe uma temperatur em Fahrenheit: "))
conv_celcius = round((temp_fahrenheit - 32 ) / 1.8,2)
print(f"A temperatura em Celcius é: {conv_celcius}")

# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km = float(input("Informe a quantidade de km: "))
dia = float(input("Informe a quantidade de dias: "))
total_pagar = (km * 0.15) + (dia * 60)
print(f"O total a pagar será de: R${total_pagar}")

# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

cigarros_dia = float(input("Informe o valor de cigarros fumados por dia: "))
anos_fumados = float(input("Informe a quantidade de anos fumados : "))
total_cigarros = (anos_fumados * 365) * cigarros_dia
dias = round(total_cigarros / 144,2)
print(f"Você perdeu {dias} dias da sua vida :(")

# Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.
x = 2 ** 10
print(len(str(f"A quantidade de caracteres é: ")))
