# ==============================================================================
# EXERCÍCIO - CLASSE BICICLETA
# ==============================================================================
# Crie uma estrutura para controlar a velocidade de uma bicicleta:
#
# 1. Classe Bicicleta:
#    - Atributos (__init__): modelo (str) e velocidade (int, iniciando em 0).
#    - Método pedalar(self): aumenta a velocidade em 5 e exibe:
#      "A bike [modelo] acelerou! Velocidade: X km/h"
#      A bike não pode passar de 60 km/h
#    - Método frear(self):
#      * Se a velocidade for maior que 0, diminui em 5 e exibe:
#        "Reduzindo... Velocidade: X km/h"
#      * Se a velocidade já for 0, exibe:
#        "A bicicleta já está totalmente parada!"
#    - Método radar_de_velocidade(self): exibe a velocidade atual.
#
# 2. Teste no Código:
#    - Instancie uma bicicleta: minha_bike = Bicicleta("Caloi")
#    - Chame o método pedalar() 2 vezes.
#    - Chame o método radar_de_velocidade().
#    - Chame o método frear() 3 vezes para validar a trava de velocidade zero.
# ==============================================================================

class Bicicleta:
    def __init__ (self, modelo : str, velocidade : int = 0):
        self.modelo = modelo
        self.velocidade = velocidade

    def pedalar(self):
        if self.velocidade + 10 <= 60:
            self.velocidade += 10
            print(f"A bicicleta {self.modelo} acelerou. Velocidade: {self.velocidade} km/h")
        else:
            self.velocidade >= 60
            print("Limite máximo de velocidade atingido")

    def freiar(self):
        if self.velocidade > 0:
            self.velocidade -= 8
            print(f"Reduzindo a velocidade. {self.velocidade} km/h")
        else:
            print("A bicicleta tá parada")

    def radar(self):
        print(f"Velocidade atual: {self.velocidade} km/h")

minha_bicicleta = Bicicleta ("Oggi")
minha_bicicleta.pedalar()
minha_bicicleta.pedalar()
minha_bicicleta.pedalar()
minha_bicicleta.pedalar()
minha_bicicleta.pedalar()
minha_bicicleta.pedalar()
minha_bicicleta.pedalar()
minha_bicicleta.radar()
minha_bicicleta.freiar()
minha_bicicleta.freiar()
minha_bicicleta.freiar()
minha_bicicleta.freiar()
minha_bicicleta.freiar()
minha_bicicleta.radar()