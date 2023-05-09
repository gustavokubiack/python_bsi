"""Faça um algoritmo que calcule e escreva a soma da seguinte série de 100 termos: 1/ 1 + 1/2 + 1/3 + 1/4 + ... + 1/100"""

count = []
for num in range(1,101):
    a = 1/num
    count.append(a)
print(sum(count))
