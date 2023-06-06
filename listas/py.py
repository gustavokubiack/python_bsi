"""a) leia 100 valores numéricos e os armazene numa variável composta unidimensional A;
b) calcule e escreva:

, onde ai é o i-ésimo valor armazenado na variável A;

c) calcule e escreva quantos termos da série acima têm o numerador menor do que o
denominador."""

# a)

vetor = [float(input("Informe o valor do vetor: ")) for i in range(5)]
soma = [i / vetor[i] for i in range(len(vetor))]
print(soma)
print(sum(soma))

menor = [soma[i] for i in range(len(soma)) if soma[i] < vetor[i]]
print(len(menor))