class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Salário: R$ {self.salario:.2f}")
        print("=" * 30)

    def aumentar_salario(self, percentual):
        aumento = self.salario * (percentual / 100)
        self.salario += aumento
        print(f"Salário de {self.nome} foi aumentado em {percentual}%. Novo salário: R$ {self.salario:.2f}")

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, setor):
        super().__init__(nome, cpf, salario)
        self.setor = setor

    def exibir_dados(self):
        print("=== GERENTE ===")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Setor: {self.setor}")
        print(f"Salario: {self.salario}")
        print("=" * 30)

    def receber_bonificacao(self):
        bonificacao = self.salario * 0.10
        self.salario += bonificacao
        print(f"Parabéns, {self.nome}. Você recebeu uma bonificação de 10% pelo seu desempenho no setor de {self.setor}")
        print(f"Novo salário: R$ {self.salario:.2f}")

func1 = Funcionario("Luiz", "099.029.509-57", 5000)
func1.exibir_dados()
func1.aumentar_salario(50)
print("\n")
gerente1 = Gerente("Luiz 2", "099.029.509-57", 15000, "Tecnologia")
gerente1.exibir_dados()
gerente1.receber_bonificacao()