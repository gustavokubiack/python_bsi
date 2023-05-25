# Exercício 1
vetor = [num for num in range(100)]
print(vetor)

# Exercício 2
notas = [float(input("Informe a nota: ")) for _ in range(10)]
print(f"Média: {sum(notas)/len(notas)}") 

# Exercício 3
notas = [float(input("Informe a nota: ")) for _ in range(10)]
nota = [nota for nota in notas if nota >= 7]
print(f"Notas acima da média: {nota}")

# Exercício 4

notas = [float(input("Informe a nota: ")) for _ in range(5)]
abaixo_media = [nota for nota in notas if nota < 7]
notas.sort()
menor_nota = notas[0]
maior_nota = notas[-1]
media = (sum(notas) / len(notas))
print(f"Menor nota: {menor_nota}\nMaior nota: {maior_nota}\nMédia: {media}\nQuantidade de notas abaixo de 7: {len(abaixo_media)}")

# Exercício 5

vetor = [float(input("Informe um número: ")) for _ in range(10)]
for num in range(len(vetor)):
    if vetor[num] == 30:
        print(f"Posição em que o número 30 está armazenado: {num}")

# Exercício 6

numeros = [float(input("Informe um valor: ")) for _ in range(10)]
print(sum(numeros))

# Exercício 7

numeros = [float(input("Informe um valor: ")) for _ in range(10)]
numeros.reverse()
print(numeros)

# Exercício 9

a = [float(input("Informe um valor: ")) for _ in range(5)]
b = [float(input("Informe um valor: ")) for _ in range(5)]
c = [num for par in zip(a, b) for num in par]
print(c)


# Exercício 11

"""11) Faça um algoritmo que leia um conjunto de 10 elementos reais e os coloque em um vetor.
Construa um segundo vetor formado da seguinte maneira:
• Os elementos de ordem par são os correspondentes do primeiro vetor multiplicados por 3.
• Os elementos de ordem ímpar são os correspondentes do primeiro vetor divididos por 2.
• Imprima os dois vetores."""

conjunto = [float(input("Informe um valor: ")) for _ in range(10)]
resultado = [num * 3 if num % 2 == 0 else num / 2 for num in conjunto]
print(resultado)

# Exercício 13

frase = float(input("Informe uma frase: "))
if len(frase) > 50:
    raise ValueError("Frase maior que 50 caracteres!")
branco = frase.count("")
letra_a = frase.count("A")
print(f"Existem {branco} espaços em branco e {letra_a} aparece a letra A")