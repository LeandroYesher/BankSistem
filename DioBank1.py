#Sistema Bancário

saques = []
depositos = []
saldo = 0.0
saques_realizados = 0

def exibir_menu():
    print("$$$ DioBank - O banco dos Devs $$$")
    print("1. Saque")
    print("2. Depósito")
    print("3. Extrato")
    print("4. Sair")
    print("============================")

def realizar_saque():
    global saques, saldo, saques_realizados
    if saques_realizados >= 3:
        print("Você já atingiu o limite de saques (3 saques por dia).")
    else:
        valor = float(input("Digite o valor do saque: R$ "))
        if valor <= 0 or valor > 500:
            print("Valor inválido para saque. O valor máximo é R$ 500.")
        elif valor > saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            saques.append(-valor)
            saldo -= valor
            saques_realizados += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

def realizar_deposito():
    global depositos, saldo
    valor = float(input("Digite o valor do depósito: R$ "))
    if valor <= 0:
        print("Valor inválido para depósito. Insira um valor maior que zero.")
    else:
        depositos.append(valor)
        saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

def exibir_extrato():
    global saques, depositos, saldo
    print("===== Extrato Financeiro =====")
    if not saques and not depositos:
        print("Não foram realizadas movimentações.")
    else:
        print("Saques realizados:")
        for saque in saques:
            print(f" - R$ {abs(saque):.2f}")
        print("Depósitos realizados:")
        for deposito in depositos:
            print(f" + R$ {deposito:.2f}")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=============================")

def main():
    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada (1, 2, 3 ou 4): ")
        
        if opcao == '1':
            realizar_saque()
        elif opcao == '2':
            realizar_deposito()
        elif opcao == '3':
            exibir_extrato()
        elif opcao == '4':
            print("Saindo do sistema bancário. Obrigado por utilizar nossos serviços!")
            break
        else:
            print("Opção inválida. Digite um número válido.")

if __name__ == "__main__":
    main()