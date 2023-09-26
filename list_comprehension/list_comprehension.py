import random

# 1) Crie uma lista com os números de 1 a 10 usando compreensão de lista.

y = [x for x in range(11)]
print(y)

# 2) Crie uma lista com os números ímpares de 1 a 50.

num = [x for x in range(1, 51) if x % 2 == 1]
print(num)

# 3) Crie uma lista com as letras maiúsculas de uma string qualquer.

fruits = ["apple", "banana", "grape", "fig"]
capitalize_string = [x.capitalize() for x in fruits]
print(capitalize_string)

# 4) Crie uma lista com o comprimento de cada palavra em uma string.

length_words = len([x for x in fruits])
print(length_words)

# 5) Crie uma lista com os números divisíveis por 3 e 5 de 1 a 30.

a = [x for x in range(1, 31) if x % 3 == 0 and x % 5 == 0]
print(a)

# 6) Crie uma lista com as palavras de uma string que tenham mais de 3 letras.

more_three_words = [x for x in fruits if len(x) > 3]
print(more_three_words)


# 7) Crie uma lista com os números primos de 1 a 20. Dica: use uma função para verificar se o número é primo ou não.


def is_prime_number(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return None
                break
        else:
            return num
    else:
        return None


numbers = [number for number in range(0, 21) if is_prime_number(number) is not None]
print(numbers)

# 8) Crie uma lista com as datas de todos os dias de fevereiro em um ano bissexto (considerando que um ano bissexto é divisível por 4).

february = [day for day in range(1, 30)]
print(february)

all_names = [
    "alice",
    "bob",
    "carol",
    "david",
    "eva",
    "fernando",
    "grace",
    "hugo",
    "isabel",
    "joão",
    "lara",
    "miguel",
    "nina",
    "oliver",
    "patrícia",
    "quintino",
    "rafael",
    "sofia",
    "tomás",
]

# 9) Crie uma lista de strings com os primeiros 10 nomes da lista de nomes.

first_ten_names = [x for x in all_names[:10]]
print(first_ten_names)

# 10) Crie uma lista de strings com os nomes dos primeiros 10 nomes da lista de nomes, mas com as primeiras letras maiúsculas.

first_ten_names = [x.capitalize() for x in all_names[:10]]
print(first_ten_names)

# 11) Crie uma lista de strings com os nomes dos primeiros 10 nomes da lista de nomes, mas sem as vogais.


def remove_vowels(name):
    vowels = "aeiou"
    return "".join([char for char in name if char not in vowels])


first_ten_names = [remove_vowels(name) for name in all_names[:10]]
print(first_ten_names)

# 12) Concatenar elementos de sub-listas em uma única lista

fruits_and_names = [y for x in [fruits, all_names] for y in x]
print(fruits_and_names)

# 13) Criar um dicionário a partir de duas listas.

automobiles = {
    "Carros": [input("Informe um carro: ") for _ in range(2)],
    "Motos": [input("Informe uma moto: ") for _ in range(2)],
}

print(f"Esse é o dicionário: {automobiles}")
