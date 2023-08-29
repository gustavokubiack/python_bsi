# Exercício 1
def merge_dict():
    people = {}
    animals = {}
    for i in range(2):
        name = input(f"Digite o nome da pessoa {i + 1}: ")
        age = int(input(f"Digite a idade de {name}: "))

        name_animal = input(f"Digite o nome do animal: {i + 1}: ")
        age_animal = int(input(f"Digite a idade de {name_animal}: "))
        people[name] = age
        animals[name_animal] = age_animal
        merge = people | animals
    return merge
