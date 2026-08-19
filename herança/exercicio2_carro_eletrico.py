class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.combustivel = 100

    def acelerar(self):
        if self.combustivel >= 5:
            self.combustivel -= 5
            print(f"{self.marca} acelerou. Combustível restante: {self.combustivel}")
        else:
            print("Sem combustível")

    def painel(self):
        print("=== PAINEL DO VEÍCULO ===")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Combustível: {self.combustivel}")

class CarroEletrico(Carro):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.combustivel = 0
        self.bateria = 0        # Por que a bateria começa em 0? Seria mais fácil começar em 100 por padrão (passado como parametro >> bateria=100) 
        # e então utilizar self.bateria = bateria

    def acelerar(self):
        if self.bateria >= 5:
            self.bateria -= 5
            print(f"O carro acelerou. Bateria restante: {self.bateria}%")
        else:
            print("Sem bateria. Recarregar")

    def recarregar(self):
        self.bateria = 100
        print("Bateria totalmente recarregada.")

    def painel(self):
        print("=== PAINEL ===")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Bateria: {self.bateria}%")

meu_ev = CarroEletrico("BYD", "Dolphin Mini")
meu_ev.painel()
meu_ev.acelerar()
meu_ev.acelerar()
meu_ev.painel()
meu_ev.recarregar()
meu_ev.painel()
