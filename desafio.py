class Banco:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.saques_diarios = 0
        self.LIMITE_SAQUES = 3
        self.LIMITE_SAQUE_VALOR = 500

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if self.saques_diarios >= self.LIMITE_SAQUES:
            print("Limite de saques diários atingido.")
        elif valor > self.LIMITE_SAQUE_VALOR:
            print(f"O limite máximo por saque é de R$ {self.LIMITE_SAQUE_VALOR:.2f}.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.saques_diarios += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de saque inválido.")

    def mostrar_extrato(self):
        print("\n========== EXTRATO ==========")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimento in self.extrato:
                print(movimento)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("=============================")

# Simulação do sistema
banco = Banco()

while True:
    print("\nEscolha uma opção:")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Sair")
    
    opcao = input("Opção: ")
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: R$ "))
        banco.depositar(valor)
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: R$ "))
        banco.sacar(valor)
    elif opcao == "3":
        banco.mostrar_extrato()
    elif opcao == "4":
        print("Saindo do sistema. Obrigado por utilizar nosso banco!")
        break
    else:
        print("Opção inválida. Tente novamente.")
