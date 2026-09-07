contatos = []


def cadastrar_contato():
    pass


def listar_contatos():
    pass


def buscar_contato():
    pass


def remover_contato():
    pass


while True:
    print("\n1 - Cadastrar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contato")
    print("4 - Remover contato")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_contato()
    elif opcao == "2":
        listar_contatos()
    elif opcao == "3":
        buscar_contato()
    elif opcao == "4":
        remover_contato()
    elif opcao == "5":
        break
    else:
        print("Opção inválida.")