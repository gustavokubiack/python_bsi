# Ler um valor e escrever se é positivo, negativo ou zero.

num = float(input("Informe o número: "))
if num > 0:
    print(f"O número {num} é positivo")
elif num < 0:
    print(f"O número {num} é negativo") 
else:
    print(f"O número {num} é igual que 0") 

# Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, caso contrário escrever NÃO É MAIOR QUE 10!

num = float(input("Informe o número: "))
if num >= 10:
    print(f"{num} é maior que 10.")
else:
    print(f"{num} é menor que 10.")

# Calcule a soma de dois números, se o resultado for maior que 10, mostre-o na tela.

num1 = float(input("Informe o primeiro número: "))
num2= float(input("Informe o segundo número: "))

if num1 + num2 > 10:
    print("É maior que 10")
else:
    print("Não é maior que 10")

# Entrar com um número e informar se ele é divisível por 5.

num = float(input("Informe o número: "))
if num % 5 == 0:
    print("É divisível por 5")
else:
    print("Não é divisível por 5")

# Construir um algoritmo que indique se o número digitado está entre 20 e 90 ou não.

num = float(input("Informe o número: "))

if num > 20 and num < 90:
    print(f"O {num} está entre 20 e 90.")
else:
    print(f'O {num} não está entre 20 e 90.')

# Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

ano_atual = int(input("Informe o ano atual: "))
ano_nascimento = int(input("Informe seu ano de nascimento: "))

if ano_atual - ano_nascimento >= 16:
    print('Você pode votar!')
else:
    print("Você não pode votar")

# Entrar com o ano de nascimento de uma pessoa e imprimir a idade dela. Verificar se o ano digitado é válido.

ano_nascimento = int(input("Informe seu ano de nascimento: "))
if ano_nascimento > 0 and ano_nascimento <= 2023:
    print(f"Ano válido! Sua idade é: {2023 - ano_nascimento}")
else: 
    print("Ano inválido!")

# Entrar com a idade de uma pessoa e exibir a mensagem; Maior de idade, menor de idade ou acima de 65 anos.
idade = float(input("Informe sua idade: "))
if idade < 18:
    print("Menor de idade!")
elif idade >= 18 and idade <= 65:
    print("Maior de idade!")
else: 
    print("Acima de 65 anos!")

# Ler as notas da 1a. e 2a . avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que se a nota for igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

if (nota1 + nota2) / 2 >= 6:
    print(f"Aprovado! Sua média é: {(nota1 + nota2) / 2}")
else:
    print(f"Reprovado! Sua média é: {(nota1 + nota2) / 2}")

# Escrever um algoritmo para ler duas notas de um aluno e escrever na tela a palavra “Aprovado” se a média das duas notas for maior ou igual a 7,0. Caso a média seja inferior a 7,0, o programa deve ler a nota do exame e calcular a média final. Se esta média for maior ou igual a 5,0, o programa deve escrever “Aprovado”, caso contrário deve escrever “Reprovado”.

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Aprovado!")
else:
    nota3 = float(input("Informe a nota do exame:"))
    exame = (nota1 + nota2 + nota3) / 3
    if exame >= 5:
        print("Aprovado em Exame!")
    else:
        print("Reprovado!")

# Escrever um algoritmo para ler a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um. Mostrar na tela qual dos professores tem salário total maior.

horas_prof1 = float(input("Informe a quantidade de horas do 1º professor: "))
valor_prof1 = float(input("Informe o valor dahora trabalhada do 1º professor: "))

horas_prof2 = float(input("Informe a quantidade de horas do 2º professor: "))
valor_prof2 = float(input("Informe o valor dahora trabalhada do 2º professor: "))

sal_prof1 = horas_prof1 * valor_prof1
sal_prof2 = horas_prof2 * valor_prof2

if sal_prof1 > sal_prof2:
    print("O Professor 1 tem um salário maior!")
else:
    print("O Professor 2 tem um salário maior!")

# Faça um algoritmo que leia um número inteiro e mostre uma mensagem indicando se este número é par ou ímpar.

num = int(input("Informe um número inteiro: "))
if num % 2 == 0:
    print(f"{num} é par!")
else:
    print(f"{num} não é par!")

# Ler o nome de 2 times e o número de gols marcados na partida. Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.

time1 = input("Informe o nome do primeiro time: ")
gol_1 = int(input(f"Informe os gols do {time1}: "))

time2 = input("Informe o nome do segundo time: ")
gol_2 = int(input(f"Informe os gols do {time2}: "))

if gol_1 > gol_2:
    print(f"{time1} venceu")
elif gol_2 > gol_1:
    print(f"{time2} venceu")
else: 
    print("O jogo terminou empatado!")

# Entrar com a sigla do estado de uma pessoa e imprimir uma das mensagens: “Carioca, Paulista, Mineiro ou Outros”

sigla = input("Informe a sigla do seu estado: ")
match sigla:
    case "RJ":
        print("Carioca")
    case "SP":
        print("Paulista")
    case "MG":
        print("Mineiro")
default: print("Outros")

# Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da compra for menor que R$ 20,00; Caso contrário, o lucro será de 30%. Entrar com o valor do produto e imprimir o valor da venda.

produto = float(input("Informe o valor de produto: "))

if produto < 20.00:
    print(f"Valor da compra: R$ {(produto * 0.45) + produto}")
else:
    print(f"Valor da compra: R$ {(produto * 0.30) + produto}")


# Entrar com um número de 1 a 12 e exibir o mês correspondente.

mes = int(input("Informe um número de 1 a 12: "))
match mes:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")

# Faça um algoritmo que verifique se uma letra digitada é vogal ou consoante.
letra = input("Informe uma letra: ")
if letra in "aeiouAEIOU":
    print(f"{letra} é uma vogal")
else:
    print(f"{letra} é uma consoante")

# Ler 2 valores (considere que não serão lidos valores iguais) e escrever o maior deles.
num1 = float(input("Informe o primeiro valor: "))
num2 = float(input("Informe o segundo número: "))

if num1 == num2:
    print("Valores iguais")
elif num1 > num2:
    print(f"{num1} é maior que {num2}")
else:
    print(f"{num2} é maior que {num1}")

# Ler 2 valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

num1 = float(input("Informe o primeiro valor: "))
num2 = float(input("Informe o segundo número: "))

if num1 == num2:
    print("Valores iguais")
elif num1 > num2:
    print(f"{num2}, {num1}")
else:
    print(f"{num1}, {num2}")

# Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.

num1 = float(input("Informe o primeiro valor: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} é maior que {num2} e {num3}")
elif num2 > num1 and num2 > num3:
    print(f"{num2} é maior que {num1} e {num3}")
else:
    print(f"{num3} é maior que {num1} e {num2}")

# Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.

num1 = float(input("Informe o primeiro valor: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))

if num1 > num2 and num1 > num3:
    print(f"A soma de {num1} e {num2} é {num1 + num2}\n")
elif num2 > num1 and num2 > num3:
    print(f"A soma de {num2} e {num3} é {num2 + num3}\n")
else:
    print(f"A soma de {num3} e {num2} é {num3 + num2}\n")

# Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente. (FAZER)

# Faça um algoritmo que leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

nota1 = float(input("Informe a nota1: "))
nota2 = float(input("Informe a nota2: "))
media = (nota1 + nota2) / 2

if media <= 10 and media >= 9:
    print(f"APROVADO!\nMédia: {media}\nConceito A")
elif media >= 7.5 and media <= 9:
    print(f"APROVADO!\nMédia: {media}\nConceito B")
elif media >= 6.0  and media <= 7.5:
    print(f"APROVADO!\nMédia: {media}\nConceito C")
elif media >= 4.0 and media <= 6.0:
    print(f"REPROADO!\nMédia: {media}\nConceito D")
else:
    print(f"REPROVADO!\nMédia: {media}\nConceito E")

# Escrever um algoritmo para ler dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma: 1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). Calcular e escrever o resultado dessa operação sobre os dois valores lidos.

num1 = float(input("Informe o primeiro valor: "))
num2 = float(input("Informe o segundo valor: "))
operacao = int(input("Informe a operação. 1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão: "))

if operacao == 1:
    print(f"Adição: {num1 + num2}")
elif operacao == 2:
    print(f"Subtração: {num1 - num2}")
elif operacao == 3:
    print(f"Multiplicação: {num1 * num2}")
elif operacao == 4:
    print(f"Divisão: {num1 / num2}")
else:
    print("Valor inválido!")

"""Faça um algoritmo para calcular as raízes reais de uma equação quadrática: ax2 + bx + c = 0. Uma equação quadrática só tem raiz reais se (b2 - 4ac) for maior ou igual a zero. O algoritmo deverá informar as seguintes situações:
• Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao
usuário e encerre o programa;
• Se o delta calculado for igual a zero a equação possui apenas uma raiz real,
informe-a ao usuário;
• Se o delta for positivo, a equação possui duas raiz reais, informe-as ao usuário.
"""
import math

a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

delta = (b ** 2) - 4 * a * c
print(delta)
if delta < 0:
    print("Valor inválido!")
elif delta == 0:
    bhaskara = (-b + (math.sqrt(delta))) / 2 * a
    print(f"x1: {bhaskara}")
else:
    x1 = (-b + (math.sqrt(delta))) / (2 * a)
    print(x1)
    x2 = (-b - (math.sqrt(delta))) / (2 * a)
    print(f"x1: {x1} e x2: {x2}")
    
""" Faça um algoritmo que leia 3 valores a, b, c, e verifique se podem ser os comprimentos dos lados de um triângulo. Em caso afirmativo, verifique se é “triângulo equilátero”, “triângulo isósceles” ou “triângulo escaleno”. Em caso negativo, escreva uma mensagem: “os valores lidos não formam um triângulo”. Considere que:
• o comprimento de cada lado de um triângulo é menor que a soma dos
comprimentos dos outros lados
• um triângulo equilátero tem três lados iguais
• um triângulo isósceles tem dois lados iguais e um diferente """

# FAZER

"""Escreva um algoritmo que leia 4 valores (opção, a, b, c), onde opção é um valor
inteiro e positivo e a, b, c são quaisquer valores reais. Escreva os valores lidos da
seguinte maneira:
se opção = 1 Þ escreva os 3 valores a, b, c em ordem crescente
se opção = 2 Þ escreva os 3 valores a, b, c em ordem decrescente
se opção = 3 Þ escreva os 3 valores de forma que o maior valor entre a, b, c fica
entre os outros 2."""

# FAZER

# Exercício 29

salario = float(input("Informe o salário: "))
if salario <= 400:
    print(f"Salário: {salario}\nReajuste: 15%\nNovo salário: {salario + (salario * 0.15)}")
elif salario > 400 and salario <= 700:
    print(f"Salário: {salario}\nReajuste: 12%\nNovo salário: {salario + (salario * 0.12)}")
elif salario > 700 and salario <= 1000:
    print(f"Salário: {salario}\nReajuste: 10%\nNovo salário: {salario + (salario * 0.10)}")
elif salario > 1000 and salario <= 1500:
    print(f"Salário: {salario}\nReajuste: 7%\nNovo salário: {salario + (salario * 0.07)}")
elif salario > 1500 and salario <= 2000:
    print(f"Salário: {salario}\nReajuste: 5%\nNovo salário: {salario + (salario * 0.05)}")
else:
    print("Sem reajuste!")