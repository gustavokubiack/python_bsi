# Exercício 1

with open("texto.txt", "w") as f:
    f.write("Olá mundo!")
    f.close()

# Exercício 2

with open("texto.txt") as f:
    print(f.read())

# Exercício 3

with open("texto.txt") as f:
    count = 0
    for line in f.readlines():
        count += 1
    print(f"O número de linhas é: {count}")

# Exercício 4

with open("texto.txt") as f:
    text = f.read()
with open("copia.txt", "w") as f:
    f.write(text)

# Exercício 5

with open("texto.txt") as f:
    text = f.read()
with open("copia.txt") as f:
    copy = f.read()
with open("combinado.txt", "w") as f:
    text += "\n"
    f.write(text)
    f.write(copy)

# Exercício 6

with open("texto.txt") as f:
    lines = [line for line in f.readlines()]
    words = [word for line in lines for word in line.split()]
    print(f"A quantidade de palavras é: {len(words)}")

# Exercício 7
with open("texto.txt") as f:
    text = f.read()
    phrase = text.replace("mundo", "Python")
with open("modificado.txt", "w") as f:
    f.write(phrase)

# Exercício 8
with open("texto.txt", "a") as f:
    phrase = "\nIsso é incrível!"
    f.write(phrase)

# Exercício 9

with open("texto.txt") as f:
    lines = [line for line in f.readlines()]
    words = [word for line in lines for word in line.split()]
    count = 0
    for letter in words:
        count += len(letter)
    print(f"A quantidade de letras no texto.txt é: {count}")


# Exercício 10
with open("numeros.txt", "w") as f:
    for line in range(0, 101):
        if line < 100:
            f.write(f"{line},")
        else:
            f.write(f"{line}")

with open("numeros.txt") as f:
    lines = f.read()
    numbers = [int(number) for number in lines.split(",")]
    print(f"A soma de 0 a 100 é: {sum(numbers)}")
