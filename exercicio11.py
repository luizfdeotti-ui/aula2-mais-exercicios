# Define a estrutura e o comportamento da classe CofreDigital
class CofreDigital:
    # Método construtor: executado automaticamente quando criamos um novo objeto CofreDigital
    def __init__(self, titular: str, senha: str):
        # Armazena o nome do titular em um atributo público (pode ser acessado e alterado diretamente)
        self.titular = titular
        # Armazena a senha em um atributo privado (indicado pelos dois sublinhados '__' no início)
        self.__senha = senha
        # Define o saldo inicial como 0.0 em um atributo privado (protegido contra alterações diretas)
        self.__saldo = 0.0

    # Método responsável por adicionar saldo ao cofre
    def depositar(self, valor: float):
        # Verifica se o valor a ser depositado é um número positivo
        if valor > 0:
            # Soma o valor depositado ao saldo privado interno
            self.__saldo += valor
            # Exibe uma mensagem confirmando o depósito formatado com duas casas decimais
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        # Executado caso o valor fornecido seja zero ou negativo
        else:
            # Exibe uma mensagem avisando que o valor digitado é inválido
            print("O valor do depósito deve ser maior que zero.")

    # Método responsável por retirar valor do cofre, exigindo verificação de senha
    def sacar(self, valor: float, senha_informada: str):
        # Verifica se a senha fornecida pelo usuário é diferente da senha armazenada
        if senha_informada != self.__senha:
            # Exibe mensagem de erro caso as senhas não coincidam
            print("Senha incorreta! Acesso negado.")
            # Interrompe a execução do método para que o saque não continue
            return

        # Verifica se o valor solicitado para o saque é zero ou negativo
        if valor <= 0:
            # Exibe mensagem de erro avisando que a quantidade solicitada é inválida
            print("O valor do saque deve ser maior que zero.")
        # Verifica se a quantia solicitada é maior do que o saldo total disponível
        elif valor > self.__saldo:
            # Exibe mensagem avisando que não há dinheiro suficiente e exibe o saldo atual
            print(f"Saldo insuficiente! Saldo atual: R$ {self.__saldo:.2f}")
        # Executado quando a senha está correta e o saldo é suficiente
        else:
            # Subtrai o valor solicitado do saldo privado
            self.__saldo -= valor
            # Exibe mensagem de sucesso com a confirmação do saque e o valor restante
            print(f"Saque de R$ {valor:.2f} realizado com sucesso! Saldo restante: R$ {self.__saldo:.2f}")

    # Método auxiliar para visualizar o saldo mantendo a segurança do cofre
    def consultar_saldo(self, senha_informada: str):
        # Compara a senha informada com a senha privada guardada na classe
        if senha_informada == self.__senha:
            # Se a senha estiver certa, imprime o saldo privado formatado
            print(f"Saldo atual de {self.titular}: R$ {self.__saldo:.2f}")
        # Caso a senha fornecida esteja errada
        else:
            # Exibe aviso de acesso negado
            print("Senha incorreta! Acesso negado.")


# --- TESTES E DEMONSTRAÇÃO ---

# Instancia (cria) um novo objeto da classe CofreDigital com titular "Ana" e senha "1234"
meu_cofre = CofreDigital("Ana", "1234")

# Chama o método de depósito passando R$ 500.00
meu_cofre.depositar(600.0)

# Tenta realizar um saque informando a senha errada ("9999")
meu_cofre.sacar(100.0, "9999")

# Tenta realizar o saque informando a senha correta ("1234")
meu_cofre.sacar(100.0, "1234")

# Imprime uma linha divisória para organizar os testes no terminal
print("\n=== Testando o Encapsulamento ===")

# Tenta alterar diretamente a variável privada de saldo fora da classe
meu_cofre.__saldo = 1000000.0

# Tenta alterar diretamente a variável privada de senha fora da classe
meu_cofre.__senha = "0000"

# Tenta sacar R$ 50.0 usando a senha original ("1234") para provar que os atributos internos NÃO mudaram
meu_cofre.sacar(50.0, "1234")