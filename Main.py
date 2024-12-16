class Main:
    pass
import random
from Cliente import Cliente
from Conta import Conta
from Autenticacao import Autenticacao


auth = Autenticacao()
conta = None

while True:
    print("\n--- Menu Inical ---")
    print("1. Criar Registro")
    print("2. Entrar")
    print("3. Sair")
    opcao_inicial = input("Escolha uma opção(1/2/3):")

    if opcao_inicial == "1":
        # Criar Registro
        registro = input("Crie um registro único (ex: CPF ou ID): ")
        if registro in auth.usuarios:
            print("Registro já existe! Tente outro.")
        else:
            nome = input("Informe o nome do cliente: ")
            telefone = input("Informe o telefone do cliente: ")
            senha = input("Crie uma senha para o cliente: ")
            auth.registrar(registro, nome, telefone, senha)
            print("Registro criado com sucesso!")

    elif opcao_inicial == "2":
        registro = input("Informe seu registro: ")
        senha = input("Informe sua senha: ")
        if registro not in auth.usuarios:
            print("Conta não encontrada. Verifique o registro e tente novamente.")
        else:
            if auth.autenticar(registro, senha):
                print("Autenticação realizada com sucesso!")
                nome_cliente, telefone_cliente = auth.obter_dados_usuario(registro)

                cliente = Cliente(nome_cliente, telefone_cliente)

                if conta is None:
                    numero_conta = random.randint(10000,99999)
                    saldo_inicial = 1000
                    conta = Conta(nome_cliente, numero_conta,saldo_inicial)
                    print(f"Conta criada com número: {numero_conta}")

                    while True:
                        print("\n--- Menu de Operações ---")
                        print("1. Depósito")
                        print("2. Saque")
                        print("3. Extrato")
                        print("4 Informações do Usuário")
                        print("5. Sair")
                        opcao = input("Escolha uma operação (1/2/3/4): ")

                        if opcao == "1":
                            # Depósito
                            valor = float(input("Informe o valor para depósito: "))
                            conta.deposita(valor)
                        elif opcao == "2":
                            # Saque
                            valor = float(input("Informe o valor para saque: "))
                            conta.saque(valor)
                        elif opcao == "3":
                            # Extrato
                            conta.extrato()
                        elif opcao == "4":
                            print("\n--- Informações do Usuário ---")
                            print("Nome:", cliente.get_nome())
                            print("Telefone:", cliente.get_telefone())

                        elif opcao == "5":
                            # Sair
                            print("Encerrando o programa. Obrigado!")
                            exit()
                        else:
                            print("opção inválida! Tente novamente.")
                else:
                    print("Senha incorreta. tente novamente.")
            elif opcao_inicial == "3":
                print("Encerrando o programa. Obrigado!")
                break

            else:
                 print("Opção inválida! Tente novamente.")