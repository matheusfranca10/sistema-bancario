menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")

        else:
            print ("Operação falhou! O valor informado é invalido")
    
    elif opcao == "s":

        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES


        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite de R$ 500.")

        elif excedeu_saques:
            print(f"Operação falhou! Você já fez {numero_saques} saques de um total de {LIMITE_SAQUES} permitidos.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")

        else:
            print("Operação falhou! o valor informado é inválido")
    
    elif opcao == "e":

        print()
        print("EXTRATO".center(50, "="))        
        print()

        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

        print()
        print("=".center(50, "="))

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")