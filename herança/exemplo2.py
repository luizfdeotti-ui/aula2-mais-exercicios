class Pessoa:
    def __init__ (self, nome, idade = 0):
        self.nome = nome
        self.idade = idade

    def __str__ (self):
        return f"Meu nome é {self.nome}"

class Aluno(Pessoa):
    def __init__ (self, nome):
        super().__init__(self)
        self.nome = nome

eu = Pessoa("Eu", 100)
print(eu)

roberto = Aluno("Roberto")
print(roberto)
print(roberto.idade)