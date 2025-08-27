import textwrap

def menu():
    menu = """
    Escolha uma operação:
    1. Adição
    2. Subtração
    3. Multiplicação
    4. Divisão
    5. Sair
    """
    return input(textwrap.dedent(menu))

def calcular(valor1,operacao, valor2):
    if operacao == '+':
        return valor1 + valor2
    if operacao == '-':
        return valor1 - valor2
    if operacao == '*':
        return valor1 * valor2
    if operacao == '/':
        if valor2 != 0:
            return valor1 / valor2
        else:
            return "Erro: Divisão por zero não é permitida."
    else:
        return "Operação inválida. Use '+', '-', '*', ou '/'."

def valores():
    try:
     valor1 = float(input("Informe o primeiro numero: "))
     valor2 = float(input("Informe o segundo numero:"))
     return valor1, valor2
    except ValueError:
        print("Erro: você deve digitar apenas números.")
        return valores()
        
while True:
    opcao = menu()

    if opcao == "1":
        valor1, valor2 = valores()
        resultado = calcular(valor1, '+', valor2)

        print(f"O resultado é {resultado:.2f}")
    
    elif opcao == "2":
        valor1, valor2 = valores()
        resultado = calcular(valor1, '-', valor2)

        print(f"O resultado é {resultado:.2f}")
    
    elif opcao == "3":
        valor1, valor2 = valores()
        resultado = calcular(valor1, '*', valor2)

        print(f"O resultado é {resultado:.2f}")

    elif opcao == "4":
        valor1, valor2 = valores()
        resultado = calcular(valor1, '/', valor2)
        # if valor2 == 0:
        #     print("Erro: Divisão por zero não é permitida.")
        # else:
        print(f"O resultado é {resultado:.2f}" if isinstance(resultado, (int, float)) else resultado)

    elif opcao == "5":
        break

    else:
        print("Opção inválida, tente novamente.")


