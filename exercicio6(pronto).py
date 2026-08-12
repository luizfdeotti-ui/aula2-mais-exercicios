# 1: Em Aplicativo - Guarde o nome e o consumo de bateria no próprio objeto aplicativo;

# 2: Em Celular - Verifique se o celular está ligado (self.ligado) E se a bateria é maior 
# ou igual ao consumo do objeto 'app' passado por parâmetro;

# 3: Em executar_app - Subtraia o consumo do aplicativo da bateria atual do celular,
# não deve ser possivel executar um app com o celular desligado,
# deve se mostrado na tela o nome do aplicativo que foi usado.

# 4: Crie dois objetos Aplicativo com consumos de bateria diferentes;
# 5: Crie um objeto Celular, ligue o aparelho e execute cada um dos aplicativos criados.

class Aplicativo:
    def __init__(self, nome, consumo_bateria):
        self.nome = nome
        self.consumo_bateria = consumo_bateria


class Celular:
    def __init__(self, marca, modelo, bateria=100):
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria
        self.ligado = True

    def ligar(self):
        self.ligado = True
        print(f"O {self.marca} {self.modelo} está ligado")
       
    def executar_app(self, app):
        if self.ligado and self.bateria >= app.consumo_bateria:
            self.bateria -= app.consumo_bateria
            print(f"App em funcionamento: {app.nome}. Bateria atual: {self.bateria}%")
        else:
            print("Não foi possível executar o aplicativo")

app1 = Aplicativo ("Snapchat", 10)
app2 = Aplicativo ("Free Fire", 50)

meu_celular = Celular ("Samsung", "Galaxy A17", bateria = 95)
meu_celular.ligar()
meu_celular.executar_app(app1)
meu_celular.executar_app(app2)