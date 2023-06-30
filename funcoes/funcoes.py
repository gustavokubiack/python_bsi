import math

def converter_celcius(f):
    return round((f - 32) * 5 / 9, 2) 


def calcular_hipotenusa(a, b):
    return math.sqrt(a**2 + b**2)


def media_aluno(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 6:
        return f"Parabéns! Você foi aprovado\nMédia: {media}"
    else:
        return f"Infelizmente você não passou :(\nMédia: {media}"


def peso_ideal(altura, sexo):
    if sexo == 1:
        peso_ideal_fem = (62.1 * altura) - 44.7
        return peso_ideal_fem
    elif sexo == 2:
        peso_ideal_masc = (72.7 * altura) - 58
        return peso_ideal_masc
    else:
        return "Número inválido!"


def forma_geometrica(lado, medida):
    if lado == 3:
        return f"Triângulo!\nPerímetro: {medida * 3}"
    elif lado == 4:
        return f"Quadrado!\nÁrea: {medida * medida}"
    elif lado == 5:
        return f"Pentágono!"
    else:
        return "Forma indisponível!"


def soma_intervalo(num1, num2):
    return sum([num for num in range(num1, num2 + 1)])


def mes_correspondente(mes):
    match mes:
        case 1:
            return 'Janeiro'
        case 2:
            return 'Fevereiro'
        case 3:
            return 'Março'            
        case 4:
            return 'Abril'
        case 5:
            return 'Maio'
        case 6:
            return 'Junho'
        case 7:
            return 'Julho'            
        case 8:
            return 'Agosto'
        case 9:
            return 'Setembro'
        case 10:
            return 'Outubro'
        case 11:
            return 'Novembro'            
        case 12:
            return 'Dezembro'


def dia_correspondente(dia):
    match dia:
        case 1:
            return 'DOM'
        case 2:
            return 'SEG'
        case 3:
            return 'TER'
        case 4: 
            return 'QUA'
        case 5:
            return 'QUI'
        case 6:
            return 'SEX'
        case 7:
            return 'SAB'


def verifica_divisivel(x, y):
    if x % y == 0:
        return 0
    else:
        return 1


def verifica_maior_valor(valor1, valor2):
    if valor1 > valor2:
        return valor1
    else:
        return valor2


def converte_pol_cm(pol):
    return pol * 2.54


# Testes 

# Exercício 1

f = float(input("Informe uma temperatura em Fahrenheit: "))
print(converter_celcius(f))

# Exercício 2

a = float(input("Informe o valor do cateto a: "))
b = float(input("Informe o valor do cateto b: "))
print(calcular_hipotenusa(a, b))

# Exercício 3

nota1 = float(input("Informe a nota1: "))
nota2 = float(input("Informe a nota2: "))
print(media_aluno(nota1, nota2))


# Exercício 4

sexo = int(input("Informe o sexo 1(feminino) 2(masculino): "))
altura = float(input("Informe a sua altura: "))
print(peso_ideal(altura, sexo))

# Exercício 5

lado = int(input("Informe a quantidade lados: "))
medida = float(input("Informe a medida do lado (cm): "))
print(forma_geometrica(lado, medida))

# Exercício 6

num1 = int(input("Informe o valor 1: "))
num2 = int(input("Informe o valor 2: "))
print(soma_intervalo(num1, num2))

# Exercício 7

mes = int(input("Informe um valor de 1 ao 12: "))
print(mes_correspondente(mes))

# Exercício 8

dia = int(input("Informe um valor de 1 a 7: "))
print(dia_correspondente(dia))

# Exercício 9

x = float(input("Informe o valor de x: "))
y = float(input("Informe o valor de y: "))
print(verifica_divisivel(x, y))

# Exercício 10

valor1 = float(input("Informe o valor de valor1: "))
valor2 = float(input("Informe o valor de valor2: "))
print(verifica_maior_valor(valor1, valor2))

# Exercício 11

pol = float(input("Informe a polegadas: "))
print(converte_pol_cm(pol))