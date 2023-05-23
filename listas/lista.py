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

