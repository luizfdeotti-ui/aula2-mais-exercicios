class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def fazer_som(self):
        print(f"{self.nome} fez som")

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, "Canino")
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} (o {self.raca} fez Au Au)")

class Gato(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, "Felino")
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} (o {self.raca} fez Miau)")

class Vaca(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, "Bovino")
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} (o {self.raca} fez Muuu)")

dog = Cachorro("Resto", "Vira-Lata")
cat = Gato("Preguiça", "Persa")
cow = Vaca("Leite", "Brahman")

animais = [dog, cat, cow]

for animal in animais:
    animal.fazer_som()