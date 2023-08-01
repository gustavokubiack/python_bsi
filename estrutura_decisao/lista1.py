# Exercício 1

num = float(input("Informe o número: "))
if num > 0:
    print(f"O número {num} é positivo")
elif num < 0:
    print(f"O número {num} é negativo")
else:
    print(f"O número {num} é igual que 0")

# Exercício 2

num = float(input("Informe o número: "))
if num >= 10:
    print(f"{num} é maior que 10.")
else:
    print(f"{num} é menor que 10.")

# Exercício 3

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

if num1 + num2 > 10:
    print("É maior que 10")
else:
    print("Não é maior que 10")

# Exercício 4

num = float(input("Informe o número: "))

if num % 5 == 0:
    print("É divisível por 5")
else:
    print("Não é divisível por 5")

# Exercício 5

num = float(input("Informe o número: "))

if num > 20 and num < 90:
    print(f"O {num} está entre 20 e 90.")
else:
    print(f"O {num} não está entre 20 e 90.")

# Exercício 6

ano_atual = int(input("Informe o ano atual: "))
ano_nascimento = int(input("Informe seu ano de nascimento: "))

if ano_atual - ano_nascimento >= 16:
    print("Você pode votar!")
else:
    print("Você não pode votar")

# Exercício 7

ano_nascimento = int(input("Informe seu ano de nascimento: "))
if ano_nascimento > 0 and ano_nascimento <= 2023:
    print(f"Ano válido! Sua idade é: {2023 - ano_nascimento}")
else:
    print("Ano inválido!")

# Exercício 8
idade = float(input("Informe sua idade: "))
if idade < 18:
    print("Menor de idade!")
elif idade >= 18 and idade <= 65:
    print("Maior de idade!")
else:
    print("Acima de 65 anos!")

# Exercício 9

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

if (nota1 + nota2) / 2 >= 6:
    print(f"Aprovado! Sua média é: {(nota1 + nota2) / 2}")
else:
    print(f"Reprovado! Sua média é: {(nota1 + nota2) / 2}")

# Exercício 10

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

# Exercício 11

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

# Exercício 12

num = int(input("Informe um número inteiro: "))
if num % 2 == 0:
    print(f"{num} é par!")
else:
    print(f"{num} não é par!")

# Exercício 13

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

# Exercício 14

sigla = input("Informe a sigla do seu estado: ")
match sigla:
    case "RJ":
        print("Carioca")
    case "SP":
        print("Paulista")
    case "MG":
        print("Mineiro")
default: print("Outros")

# Exercício 15

produto = float(input("Informe o valor de produto: "))

if produto < 20.00:
    print(f"Valor da compra: R$ {(produto * 0.45) + produto}")
else:
    print(f"Valor da compra: R$ {(produto * 0.30) + produto}")


# Exercício 16

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

# Exercício 17

letra = input("Informe uma letra: ")
if letra in "aeiouAEIOU":
    print(f"{letra} é uma vogal")
else:
    print(f"{letra} é uma consoante")

# Exercício 18

num1 = float(input("Informe o primeiro valor: "))
num2 = float(input("Informe o segundo número: "))

if num1 == num2:
    print("Valores iguais")
elif num1 > num2:
    print(f"{num1} é maior que {num2}")
else:
    print(f"{num2} é maior que {num1}")

# Exercício 19

num1 = float(input("Informe o primeiro valor: "))
num2 = float(input("Informe o segundo número: "))

if num1 == num2:
    print("Valores iguais")
elif num1 > num2:
    print(f"{num2}, {num1}")
else:
    print(f"{num1}, {num2}")

# Exercício 20

num1 = float(input("Informe o primeiro valor: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} é maior que {num2} e {num3}")
elif num2 > num1 and num2 > num3:
    print(f"{num2} é maior que {num1} e {num3}")
else:
    print(f"{num3} é maior que {num1} e {num2}")

# Exercício 21

num1 = float(input("Informe o primeiro valor: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))

if num1 > num2 and num1 > num3:
    print(f"A soma de {num1} e {num2} é {num1 + num2}\n")
elif num2 > num1 and num2 > num3:
    print(f"A soma de {num2} e {num3} é {num2 + num3}\n")
else:
    print(f"A soma de {num3} e {num2} é {num3 + num2}\n")

# Exercício 22

# Ler três valores
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

valores_ordenados = sorted([valor1, valor2, valor3])
print("Valores em ordem crescente:", valores_ordenados)

# Exercício 23

nota1 = float(input("Informe a nota1: "))
nota2 = float(input("Informe a nota2: "))
media = (nota1 + nota2) / 2

if media <= 10 and media >= 9:
    print(f"APROVADO!\nMédia: {media}\nConceito A")
elif media >= 7.5 and media <= 9:
    print(f"APROVADO!\nMédia: {media}\nConceito B")
elif media >= 6.0 and media <= 7.5:
    print(f"APROVADO!\nMédia: {media}\nConceito C")
elif media >= 4.0 and media <= 6.0:
    print(f"REPROADO!\nMédia: {media}\nConceito D")
else:
    print(f"REPROVADO!\nMédia: {media}\nConceito E")

# Exercício 24

num1 = float(input("Informe o primeiro valor: "))
num2 = float(input("Informe o segundo valor: "))
operacao = int(
    input(
        "Informe a operação. 1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão: "
    )
)

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

# Exercício 25

import math

a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

delta = (b**2) - 4 * a * c
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

# Exercício 26 (FAZER)

a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))
if a < b + c and b < a + c and c < a + b:
    if a == b and a == c:
        print("Triângulo equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Os valores lidos não formam um triângulo")

# Exercício 27

opcao = int(
    input(
        "Digite a opção desejada (1 para ordem crescente, 2 para ordem decrescente ou 3 para o maior valor ficar entre os outros dois): "
    )
)
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if opcao == 1:
    if a <= b <= c:
        print(a, b, c)
    elif a <= c <= b:
        print(a, c, b)
    elif b <= a <= c:
        print(b, a, c)
    elif b <= c <= a:
        print(b, c, a)
    elif c <= a <= b:
        print(c, a, b)
    else:
        print(c, b, a)
elif opcao == 2:
    if a >= b >= c:
        print(a, b, c)
    elif a >= c >= b:
        print(a, c, b)
    elif b >= a >= c:
        print(b, a, c)
    elif b >= c >= a:
        print(b, c, a)
    elif c >= a >= b:
        print(c, a, b)
    else:
        print(c, b, a)
elif opcao == 3:
    if a >= b and a >= c:
        if b >= c:
            print(b, a, c)
        else:
            print(c, a, b)
    elif b >= a and b >= c:
        if a >= c:
            print(a, b, c)
        else:
            print(c, b, a)
    else:
        if a >= b:
            print(a, c, b)
        else:
            print(b, c, a)
else:
    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")


# Exercício 28

salario = float(input("Informe o salário: "))
if salario <= 400:
    print(
        f"Salário: {salario}\nReajuste: 15%\nNovo salário: {salario + (salario * 0.15)}"
    )
elif salario > 400 and salario <= 700:
    print(
        f"Salário: {salario}\nReajuste: 12%\nNovo salário: {salario + (salario * 0.12)}"
    )
elif salario > 700 and salario <= 1000:
    print(
        f"Salário: {salario}\nReajuste: 10%\nNovo salário: {salario + (salario * 0.10)}"
    )
elif salario > 1000 and salario <= 1500:
    print(
        f"Salário: {salario}\nReajuste: 7%\nNovo salário: {salario + (salario * 0.07)}"
    )
elif salario > 1500 and salario <= 2000:
    print(
        f"Salário: {salario}\nReajuste: 5%\nNovo salário: {salario + (salario * 0.05)}"
    )
else:
    print("Sem reajuste!")

# Exercício 30

temperatura = float(input("Informe a temperatura: "))
if temperatura <= 500:
    print("Temperatura inválida!")
elif temperatura < 700:
    print("Aquecimento ligado em 100%")
elif temperatura < 735:
    print("Aquecimento ligado em 50%")
elif temperatura >= 735:
    print("Aquecimento desligado")
elif temperatura > 780:
    print("Superaquecimento")
else:
    print("Valor inválido!")

# Exercício 31

valor = int(input("Informe um valor de 1 a 4: "))
num1 = float(input("Informe o primeiro valor: "))
num2 = float(input("Informe o segundo valor: "))
if valor == 0:
    print(f"Soma: {num1 + num2}")
elif valor == 1:
    print(f"Subtração: {num1 - num2}")
elif valor == 2:
    print(f"Multiplicação: {num1 * num2}")
elif valor == 3:
    print(f"Divisão: {num1 / num2}")
elif valor == 4:
    print(f"Média: {(num1 + num2) / 2}")
else:
    print("Valor errado. Programa encerrado sem cálculos")

# Exercício 32

num1 = int(input("Informe o primeiro valor: "))
num2 = int(input("Informe o segundo valor: "))
if num1 % num2 == 1:
    print(f"Soma: {num1 + num2 + (num1 % num2)}")
elif num1 % num2 == 2:
    if num1 % 2 == 0 and num2 % 2 == 0:
        print("Os dois números são pares")
    elif num1 % 2 == 0 and num2 % 2 != 0:
        print("O primeiro número é par e o segundo é ímpar")
    elif num1 % 2 != 0 and num2 % 2 == 0:
        print("O primeiro número é ímpar e o segundo é par")
    else:
        print("Os dois números são ímpares")
elif num1 % num2 == 3:
    print(f"Multiplicação: {(num1 + num2) * num1}")
elif num1 % num2 == 4:
    if num2 != 0:
        print(f"Divisão: {(num1 + num2) / num2}")
    else:
        print("O segundo número é igual a zero")
else:
    print(
        f"Quadrado do primeiro número: {num1 ** 2}\nQuadrado do segundo número: {num2 ** 2}"
    )

# Exercício 33

homem1 = int(input("Informe a idade do primeiro homem: "))
homem2 = int(input("Informe a idade do segundo homem: "))
mulher1 = int(input("Informe a idade da primeira mulher: "))
mulher2 = int(input("Informe a idade da segunda mulher: "))

if homem1 > homem2:
    homem_mais_velho = homem1
    homem_mais_novo = homem2
else:
    homem_mais_velho = homem2
    homem_mais_novo = homem1

if mulher1 > mulher2:
    mulher_mais_velha = mulher1
    mulher_mais_nova = mulher2
else:
    mulher_mais_velha = mulher2
    mulher_mais_nova = mulher1

print(
    f"Soma das idades do homem mais velho com a mulher mais nova: {homem_mais_velho + mulher_mais_nova}"
)

# Exercício 34

num = int(input("Informe um número de 4 dígitos: "))
if num >= 1000 and num <= 9999:
    dezena = num // 100
    unidade = num % 100
    milhar = num // 100
    centena = num % 100
    soma = (dezena + unidade) + (milhar + centena)
    quadrado = soma**2
    if quadrado == num:
        print(f"O quadrado do número {num} é {quadrado}")
    else:
        print(f"O quadrado do número {num} não é {quadrado}")
else:
    print("Número inválido!")
