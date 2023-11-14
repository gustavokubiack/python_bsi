"""" Escreva uma função que recebe dois números como argumentos e retorna a
divisão do primeiro pelo segundo. Use um bloco try/except para tratar o caso em
que o segundo número é zero e lance uma exceção personalizada com a
mensagem "Divisão por zero não permitida"."""

def divide_num(num1, num2):
    try:
        return num1 / num2
    except:
        return "Divisão por zero não permitida"

print(divide_num(2, 1))


"""Escreva um programa que solicita ao usuário uma data no formato "dd/mm/aaaa"
e verifica se ela é válida. Use um bloco `try/except` para tratar o caso em que o
usuário digita uma data inválida e lance uma exceção personalizada com a
mensagem “Data inválida”."""

def input_date(date):
    try:
        pass
    except:
        pass

"""Escreva uma função que recebe uma lista de números como argumento e retorna a
soma dos elementos da lista. Use um bloco `try/except` para tratar o caso em que
a lista contém algum elemento que não é um número e lance uma exceção
personalizada com a mensagem “Lista inválida”."""

def sum_list(lista):
    try:
        return sum(lista)
    except:
        return "Lista inválida!"

nums = [num for num in range(5)]
nums.append("7")
print(sum_list(nums))


"""
Escreva um programa que solicita ao usuário um nome de arquivo e tenta abri-lo
para leitura. Use um bloco `try/except` para tratar o caso em que o arquivo não
existe ou não pode ser aberto e lance uma exceção personalizada com a
mensagem “Arquivo inválido”. """

def input_file():
    try:
        file = input("Insira o nome do arquivo txt: ")
        file = file + ".txt"
        with open(file) as f:
            f.read()
    except:
        return "Arquivo inválido!"

print(input_file())


"""Escreva um código que tente abrir um arquivo com o modo de escrita, porém o
arquivo já existe. Se ocorrer uma exceção, imprima uma mensagem de erro."""

import os

def check_file():
    try:
        with open("usuarios.txt", "x") as f:
            f.write("Olá")
    except:
        return "Arquivo já existe!"

print(check_file())


"""Escreva uma função que recebe um número inteiro positivo como argumento e
retorna o fatorial desse número. Use um bloco `try/except` para tratar o caso em
que o argumento é negativo ou não é um inteiro e lance uma exceção
personalizada com a mensagem “Argumento inválido”."""

import math

def factor_num(num):
    try:
        return math.factorial(num)
    except:
        return "Argumento inválido!"

num = -1.5
print(factor_num(num))

"""Escreva uma função que recebe uma string como argumento e retorna o número
de vogais contidas nessa string. Use um bloco `try/except` para tratar o caso em
que o argumento não é uma string e lance uma exceção personalizada com a
mensagem “Argumento inválido”."""

def count_vowels(word):
    try:
        vowels = [each for each in word if each in "aeiouAEIOU"]      
        return len(vowels)  
    except:
        return "Argumento inválido!"

word = "aeiou"
print(count_vowels(word))


"""Escreva uma função que recebe uma lista de strings como argumento e retorna
uma nova lista com estas strings ordenadas alfabeticamente. Use um bloco
`try/except` para tratar o caso em que a lista contém algum elemento que não é
uma string e lance uma exceção personalizada com a mensagem “Lista inválida”."""

def order_list(lista):
    try:
        return sorted(lista)
    except:
        return "Lista inválida"

print(order_list(lista=["a", "x", 'b', 1]))

"""Escreva um programa que solicite ao usuário um índice e, em seguida, tente
acessar um elemento em uma lista. Trate exceções caso o índice esteja fora dos
limites da lista."""

def check_index(lista):
    try:
        index = int(input("Insire um index da lista: "))
        return lista[index]
    except:
        return "Índice não está na lista!"

print(check_index(lista=["1", "2", "3", "4", "5"]))
