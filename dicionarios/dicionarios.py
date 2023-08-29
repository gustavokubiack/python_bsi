# Exercício 1 e 2
def informations_people():
    people = {}
    for i in range(3):
        name = input(f"Digite o nome da pessoa {i + 1}: ")
        age = int(input(f"Digite a idade de {name}: "))
        people[name] = age
    return people


dict_people = informations_people()

# Exercício 3


def whats_age(info_people, search_name):
    for name, age in info_people.items():
        if name == search_name:
            return (name, age)

    return "Nome não encontrado!"


print(whats_age(dict_people, "Turing"))
# Exercício 4


def new_age_person(info_people, search_name, new_age):
    for name, age in info_people.items():
        if search_name == name:
            info_people[search_name] = new_age
            return info_people
    return "Nome não encontrado!"


print(new_age_person(dict_people, "thj", 20))

# Exercício 5


def remove_person(info_people, search_name):
    for name, age in info_people.items():
        if name == search_name:
            removed = info_people.pop(search_name)
            return info_people
    return "Nome não encontrado!"


print(remove_person(dict_people, "thj"))

# Exercício 6


def how_many_people(info_people):
    return len(info_people)


print(how_many_people(dict_people))


# Exercício 7


def average_age(info_people):
    average = [age for name, age in info_people.items()]
    return f"A média é: {sum(average)/len(average)}"


print(average_age(dict_people))


# Exerício 8


def older_person(info_people):
    older = [age for name, age in info_people.items()]
    return max(older)


print(older_person(dict_people))


# Exercício 9


def newer_person(info_people):
    newer = [age for name, age in info_people.items()]
    return min(newer)


print(newer_person(dict_people))
# Exercício 10


def name_j(info_people):
    names = [name for name, age in info_people.items() if name.startswith("J")]
    return names


print(name_j(dict_people))
