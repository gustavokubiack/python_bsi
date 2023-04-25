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




