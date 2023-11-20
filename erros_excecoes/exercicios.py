# Exercício 1

def divide_num(num1, num2):
    try:
        return num1 / num2
    except:
        return "Divisão por zero não permitida"

print(divide_num(2, 1))

# Exercício 2

from datetime import datetime

def input_date():
    try:
        data = input("Digite uma data no formato dd/mm/aaaa: ")
        formatt = '%d/%m/%Y'
        formatted_data = datetime.strptime(data, formatt)
        return (f"Data válida: {formatted_data}")
    except ValueError:
        return "Data inválida"

print(input_date())

# Exercício 3

def sum_list(lista):
    try:
        return sum(lista)
    except:
        return "Lista inválida!"

nums = [num for num in range(5)]
nums.append("7")
print(sum_list(nums))


# Exercício 4

def input_file():
    try:
        file = input("Insira o nome do arquivo txt: ")
        file = file + ".txt"
        with open(file) as f:
            f.read()
    except:
        return "Arquivo inválido!"

print(input_file())


# Exercício 5


def check_file():
    try:
        with open("erros_excecoes/usuarios.txt", "x") as f:
            f.write("Olá")
    except:
        return "Arquivo já existe!"

print(check_file())


# Exercício 6

import math

def factor_num(num):
    try:
        return math.factorial(num)
    except:
        return "Argumento inválido!"

num = -1.5
print(factor_num(num))

# Exercício 7

def count_vowels(word):
    try:
        vowels = [each for each in word if each in "aeiouAEIOU"]      
        return len(vowels)  
    except:
        return "Argumento inválido!"

word = "aeiou"
print(count_vowels(word))


# Exercício 8

def order_list(lista):
    try:
        return sorted(lista)
    except:
        return "Lista inválida"

print(order_list(lista=["a", "x", 'b', 1]))

# Exercício 9

def check_index(lista):
    try:
        index = int(input("Insire um index da lista: "))
        return lista[index]
    except:
        return "Índice não está na lista!"

print(check_index(lista=["1", "2", "3", "4", "5"]))

# Exercício 10

def convert_number_to_string():
    try:
        return str(input("Insira um número inteiro para converter para string: "))    
    except:
        return "Erro!"
    
print(convert_number_to_string())

# Exercício 11

def format_text():
    try:
        import os

        file_path = "erros_excecoes/texto.txt"
        file_path = os.path.abspath(file_path)
        with open(file_path, "r+") as f:
            content = f.read()
            content = ' '.join(content.split())
            f.seek(0)
            f.truncate(0)
            f.write(content)
    except Exception as e:
        return 'Erro ao formatar arquivo', e
    
    return 'Arquivo formatado com sucesso'

print(format_text())


# Exercício 12

data = {
    "name": "Gustavo Kubiack",
    "age": 20,
    "height": 1.87,
    "is_programmer": True,
}

def access_dict(data):
    try:
        key = input("Insira uma chave do dicionário: ")
        return data[key]
    except KeyError:
        return "Não foi possível acessar o dicionário, tente outra chave!"

print(access_dict(data))

# Exercício 13
def sum():
    try:
        num1 = int(input("Insira o primeiro número inteiro: "))
        num2 = int(input("Insira o segundo número inteiro: "))
        return num1 + num2
    except Exception:
        return f"Erro! É necessário inserir valores inteiros de 0 a 9."

print(sum())


# Exercício 14

def input_password():
    password = input("Insira uma senha com 8 caracteres: ")
    try:
        if len(password) >= 8:
            return password
        else:
            raise ValueError("Senha muito curta! Insira no mínimo 8 caracteres :)")
    except ValueError as e:
        return e
    
print(input_password())

# Exercício 15

def divide_list():
    try:
        nums = [_ for _ in range(1, 11)]
        divisor = int(input("Insira um divisor para a lista: "))
        sub_list_len = len(nums) // divisor
        resultado = [nums[i * sub_list_len: (i + 1) * sub_list_len] for i in range(divisor)]
        return resultado
    except:
        return "Não é possível dividir a lista em partes iguais!"
    
print(divide_list())

# Exercício 16

def show_number():
    try:
        return int(input("Insira um número inteiro: "))
    except ValueError:
        return "Insira somente valores inteiros."
    except TypeError:
        return "O tipo de entrada não pode ser convertido para um número."
    except:
        return "Algum erro aconteceu :("
    
print(show_number())

# Exercício 17

def add_numbers():
    try:
        while True:
            nums = []
            num = float(input("Insira um número na lista: "))
            nums.append(num)
    except:
        return "Insira somente valores números!"
            
print(add_numbers())

# Exercício 18

def factorial():
    try:
        num = int(input("Informe um número inteiro: "))
        try:
            if num > 0:
                return math.factorial(num)
            else:
                raise ValueError("Não é possível realizar o fatorial de valores negativos")
        except ValueError as e:
            return e
    except Exception:
        return "Erro! É necessário inserir um valor inteiro!"
    
print(factorial())


# Exercício 19

def higher_number():
    try:
        num1 = int(input("Insira o primeiro número inteiro: "))
        num2 = int(input("Insira o segundo número inteiro: "))
        if num1 > num2:
            return num1
        else:
            return num2 
    except ValueError:
        return "Erro: Insira somente valores inteiros!"
    except TypeError:
        return "Erro de tipagem!"
    else:
        return "Aconteceu algo!"
