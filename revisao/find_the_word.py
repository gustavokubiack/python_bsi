from faker import Faker


class FindTheWord:
    def __init__(self):
        self.level = None
        self.category = None
        self.word = None

    def infos(self):
        self.level = input("Informe a dificuldade: ")
        self.category = input("Informe a categoria: ")

    def dicts(self, num_items):
        faker = Faker("pt-br")
        countries = [faker.country() for _ in range(num_items)]
        names = [faker.first_name() for _ in range(num_items)]
        colors = [faker.color_name() for _ in range(num_items)]
        data = {
            "Países": countries,
            "Nomes": names,
            "Cores": colors,
        }
        return data

    def choice_level(self):
        data = self.dicts(20)
        if self.level == "Fácil":
            return data[self.category][:5]
        elif self.level == "Médio":
            return data[self.category][:10]
        elif self.level == "Díficil":
            return data[self.category][:20]
        else:
            print("Erro! As opções de dificuldade são: 'Fácil', 'Médio' e 'Difícil'")