# ==============================================================================
# EXERCÍCIO - CLASSE PET VIRTUAL (TAMAGOTCHI)
# ==============================================================================
# Crie uma estrutura do zero para controlar as necessidades de um bichinho virtual:
#
# 1. Classe PetVirtual:
#    - Atributos (__init__): nome (str), fome (int, iniciando em 5) e felicidade (int, iniciando em 5).
#    - Método alimentar(self):
#      * Se a fome for maior que 0, diminui a fome em 2 e exibe:
#        "[nome] foi alimentado! Fome atual: X"
#      * Se a fome já for 0, exibe: "[nome] já está de barriga cheia!"
#    - Método brincar(self):
#      * Aumenta a felicidade em 2 e aumenta a fome em 1.
#      * Exibe: "Você brincou com [nome]! Felicidade: X | Fome: Y"
#    - Método status(self):
#      * Exibe o nome do pet, a fome atual e a felicidade.
#      * Se a fome for maior ou igual a 8, exibe um alerta: "Atenção: [nome] precisa comer!"
#
# 2. Teste no Código:
#    - Instancie um pet virtual: meu_pet = PetVirtual("Pou")
#    - Chame o método status().
#    - Chame o método brincar() 2 vezes.
#    - Chame o método alimentar() 3 vezes.
#    - Chame o método status() novamente para conferir o resultado final.
# ==============================================================================

class PetVirtual:
    def __init__ (self, nome : str, fome : int = 5, felicidade : int = 5):
        self.nome  = nome
        self.fome = fome
        self.felicidade = felicidade

    def alimentar (self):
        if self.fome > 0:
            self.fome -= 2
            if self.fome < 0:
                self.fome = 0
                print(f"{self.nome} foi alimentado. Fome: {self.fome}")
            else:
                print(f"{self.nome} tá de barriga cheia")

    def brincar (self):
        self.felicidade += 2
        self.fome += 1
        print(f"Você brincou com {self.nome}. Felicidade: {self.felicidade}. Fome: {self.fome}")

    def status (self):
        print(f"STATUS DE: {self.nome}")
        print(f"Fome: {self.fome}. Felicidade: {self.felicidade}")
        if self.fome >= 8:
            print(f"{self.nome}, precisa comer")

meu_pet = PetVirtual ("Paçoca Bigode")
meu_pet.status()
meu_pet.brincar()
meu_pet.brincar()
meu_pet.alimentar()
meu_pet.alimentar()
meu_pet.alimentar()
meu_pet.status()