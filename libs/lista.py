# 1. Importe o módulo math e calcule a raiz quadrada de um número inteiro.
import math
import datetime
import random
import numpy as np
import matplotlib.pyplot as plt
import requests
import pandas as pd
import os
from bs4 import BeautifulSoup
import calculadora as calc

number = int(input("Informe um número: "))
result = math.sqrt(number)
print(result)

# 2. Importe o módulo datetime e exiba a data e hora atuais.

date = datetime.datetime.now()
print(date)

# 3. Use o módulo string para verificar se uma string contém apenas dígitos.

word = "gu12345"
if word.isdigit():
    print("A string contém apenas dígitos")
else:
    print("A string não contém apenas dígitos")

# 4. Importe o módulo random e gere um número aleatório entre 1 e 100.

number = random.randrange(0, 101)
print(number)

# 5. Importe a biblioteca numpy e crie uma array com os números de 1 a 10.

numbers = np.array([i for i in range(0, 11)])
print(numbers)

# 6. Escreva um programa que importe o pacote numpy e crie uma matriz de zeros com dimensões 3x3.
zero_mat = np.zeros((3, 3))
print(zero_mat)

# 7. Importe a biblioteca matplotlib e crie um gráfico de barras simples com alguns dados fictícios.

plt.style.use("_mpl-gallery")

x = 0.5 + np.arange(8)
y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]
fig, ax = plt.subplots()
ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()

# 8. Escreva um programa que importe o pacote matplotlib e plote a função seno.

x = np.linspace(-np.pi, np.pi, 201)
plt.plot(x, np.sin(x))
plt.xlabel("Angle [rad]")
plt.ylabel("sin(x)")
plt.axis("tight")
plt.show()

# 9. Importe o pacote requests e faça uma requisição HTTP para um URL e exiba o código de status.

url = "https://google.com"
response = requests.get(url)
print(f"O status da requisição: {response.status_code}")

# 10. Importe a biblioteca pandas, leia um arquivo CSV (por exemplo, "dados.csv") e exiba`` as primeiras linhas do DataFrame.

df = pd.read_csv("libs/dataset.csv")
print(df.head(10))

# 11. Escreva um programa que importe o módulo os e imprima o diretório de trabalho atual.

print(f"O diretório de trabalho é: {os.getcwdb()}")

# 12. Escreva um programa que importe o pacote beautifulsoup4 e faça a raspagem de dados (web crawling) de uma página HTML.

soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())

# 13. Crie um módulo personalizado chamado de calculadora com uma função que some dois números. Em seguida, importe e use essa função.

print(calc.soma(2, 2))

"""
14.

import game.Level.start

import game.Level.start.select_dificulty()

from game.Image import change

import game.Sound.play

"""
