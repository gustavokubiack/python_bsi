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
    print(count)

# Exercício 4

with open("texto.txt") as f:
    texto = f.read()
with open("copia.txt", "w") as f:
    f.write(texto)

# Exercício 5

with open("texto.txt") as f:
    texto = f.read()
with open("copia.txt") as f:
    copia = f.read()
with open("combinado.txt", "w") as f:
    texto += "\n"
    f.write(texto)
    f.write(copia)

