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

# Exercício 8

vetor1 = [float(input("Informe o valor do primeiro vetor: ")) for _ in range(10)]
vetor2 = [float(input("Informe o valor do segundo vetor: ")) for _ in range(10)]
vetor3 = [vetor1[i] + vetor2[i] for i in range(len(vetor1))]

print(vetor1)
print(vetor2)
print(vetor3)


# Exercício 9

a = [float(input("Informe um valor: ")) for _ in range(5)]
b = [float(input("Informe um valor: ")) for _ in range(5)]
c = [num for par in zip(a, b) for num in par]
print(c)

# Exercício 10

vetor = [float(input("Informe um valor do vetor: ")) for _ in range(10)]
soma = [vetor[i] for i in vetor]
print(soma)

# Exercício 11

conjunto = [float(input("Informe um valor: ")) for _ in range(10)]
resultado = [num * 3 if num % 2 == 0 else num / 2 for num in conjunto]
print(resultado)

# Exercício 12

import random

a = [random.randint(0, 100) for i, _ in enumerate(range(10))]
print(a)
s = 0
for i in range(10):
    s += (a[i] - a[19-i])**2
print(f'Lista: {a}')
print(f'S = {s}')


# Exercício 13

frase = float(input("Informe uma frase: "))
if len(frase) > 50:
    raise ValueError("Frase maior que 50 caracteres!")
branco = frase.count("")
letra_a = frase.count("A")
print(f"Existem {branco} espaços em branco e {letra_a} aparece a letra A")

# Exercício 14

mercadorias = [mercadoria for mercadoria in range(10)]
precos = [preco for preco in range(10)]
faturamento = [mercadorias[elemento] * precos[elemento] for elemento in range(len(mercadorias))]
print(faturamento)

# Exercício 15

import random 

vet = [random.radint(1,100) for _ in range(20)]
vet.sort()
print(vet)

# Exercício 16

import string
alfabeto = string.ascii_uppercase
vetor = [random.choice(alfabeto) for _ in range(20)]
indices = [indice for indice, elemento in enumerate(vetor) if elemento == "K"]
if "K" not in vetor:
    print(f"CHAVE NÃO ENCONTRADA\nVetor: {vetor}")
else:
    print(f"O vetor é {vetor}\nPosição da chave: {indices}")

# Exercício 17

alfabeto = string.ascii_uppercase
vetor = [random.choice(alfabeto) for _ in range(20)]
vetor.sort()
print(vetor)
chave = input("Informe a chave: ")
inicio = 0
fim = len(vetor) - 1
meio = (inicio + fim) // 2
while inicio <= fim and vetor[meio] != chave:
    if chave < vetor[meio]:
        fim = meio - 1
    else:
        inicio = meio + 1
    meio = (inicio + fim) // 2
if vetor[meio] == chave:
    print(f"Chave encontrada na posição {meio}")
else:
    print("Chave não encontrada")

