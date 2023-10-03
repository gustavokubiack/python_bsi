# 1. Importe o módulo math e calcule a raiz quadrada de um número inteiro.
import math

number = 49
result = math.sqrt(number)
print(result)

# 2. Importe o módulo datetime e exiba a data e hora atuais.

import datetime

date = datetime.datetime.now()
print(date)

# 3. Use o módulo string para verificar se uma string contém apenas dígitos.

word = "gu12345"
if word.isdigit():
    print("A string contém apenas dígitos")
else:
    print("A string não contém apenas dígitos")

# 4. Importe o módulo random e gere um número aleatório entre 1 e 100.

import random

number = random.randrange(0, 101)
print(number)

# 5. Importe a biblioteca numpy e crie uma array com os números de 1 a 10.

import numpy as np

numbers = np.array([i for i in range(0, 11)])
print(numbers)