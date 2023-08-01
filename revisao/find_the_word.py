from faker import Faker


class FindTheWord:
    def __init__(self):
        self.level = None
        self.category = None
        self.word = None

    def infos(self):
        self.level = input("Informe a dificuldade: ")
        self.category = input("Informe a categoria: ")

    def dicts(self):
        faker = Faker("pt-br")
        countries = [faker.country() for _ in range(5)]
        names = [faker.first_name() for _ in range(5)]
        colors = [faker.color_name() for _ in range(5)]
        data = {
            "country": countries,
            "name": names,
            "color": colors,
        }
        return data

    def choice_level(self):
        try:
            if self.level == "Fácil":
                print("fácil")
            elif self.level == "Médio":
                print("médio")
            elif self.level == "Díficil":
                print("díficil")
            else:
                raise Exception(
                    "Erro! As opções de dificuldade são: 'Fácil', 'Médio' e 'Difícil'"
                )
        except Exception as e:
            print(e)
