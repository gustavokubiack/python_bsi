# Exercício 1 e 2
def info():
    people = {"names": [], "ages": []}
    for person in range(2):
        name = input("Informe seu nome: ")
        age = int(input("Informe sua idade: "))
        people["names"].append(name)
        people["ages"].append(age)

    return people


def whats_the_age(info, name):
    try:
        if name in info["names"]:
            index = info["names"].index(name)
            age = info["ages"][index]
            print(f"A idade do {name} é {age}")
        else:
            raise Exception("Nome não está no dicionário!")
    except Exception as e:
        print("Erro!", e)


people = info()
whats_the_age(people, "Gustavo")


def add_a_person(info, name, age):
    try:
        info["names"].append(name)
        info["ages"].append(age)
    except Exception as e:
        print("Erro!", e)
    return info


print(add_a_person(people, "Turing", 20))


def remove_a_person(info, name, age):
    try:
        info["names"].remove(name)
        info["ages"].remove(age)
    except Exception as e:
        print("Erro!", e)
    return info


print(remove_a_person(people, "Turing", 20))


def how_may_people(info):
    try:
        a = len(info)
    except Exception as e:
        print("Erro!", e)
    return a


print(how_may_people(people))


def average(info):
    try:
        average_age = sum(info["ages"]) / len(info["ages"])
    except Exception as e:
        print("Erro!", e)
    return average_age

print(average(people))
