# Ler lado do quadrado e mostrar área e perímetro

lado = float(input("Informe o valor do lado do quadrado: "))

area = lado * lado
perimetro = lado * 4

print(f"Área: {area}\nPerímetro: {perimetro}")

# Ler nome e quantidade de filhos

nome = input("Informe seu nome: ")
filhos = float(input("Informe a quantidade de filhos: "))

print(f"{nome} tem {filhos} filhos")

# Ler base e altura de um retângulo 

base = float(input("Informe a base de um retângulo: "))
altura = float(input("Informe a altura de um retângulo: "))

perimetro = 2 * (base + altura)
area = base * altura

print(f"Perímetro: {perimetro}\nÁrea: {area}")

# Ler valor de um cubo

lado = float(input("Informe o lado do cubo: "))
area = 6 * (lado * lado)
volume = lado ** 3

print(f"Aŕea: {area}\nVolume: {volume}")

# Ler dois números e mostrar o quociente e o resto da divisão inteira

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

quociente = num1 / num2
resto = num1 % num2

print(f"Quociente: {quociente}\nResto:{resto}")

