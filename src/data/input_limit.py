
def input_limit():
    print("_______Defina o Limite de Requisição_______")
    print("Opções:")
    print("1. Limite padrão (1000)")
    print("2. Limite padrão (5000)")
    print("3. Limite padrão (10000)")
    choice = input("Escolha uma opção: ")
    if choice == "1":
        return 1000
    elif choice == "2":
        return 5000
    elif choice == "3":
        return 10000
    
    else:
        print("Opção inválida. Usando limite padrão de 1000.")
        return 1000

