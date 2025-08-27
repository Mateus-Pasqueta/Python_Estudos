import random
import textwrap


def menu():
    menu = """
    =========================
          JOGO DA FORCA
    =========================
    Escolha uma opção:
    1. Animais
    2. Cores
    3. Escolher minha palavra
    4. Sair
    """
    return input(textwrap.dedent(menu))


def mostrar_tela(categoria, erros=0):
    print(f"\n===== CATEGORIA: {categoria.upper()} =====")
    print(forca[erros])

forca = [
    """
      ------
      |    |
      |
      |
      |
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |
      |
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |    |
      |
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |   /|
      |
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   /
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   / \\
      |
    --------
    """,
]

animais = ["leao", "elefante", "macaco", "tigre", "cachorro", "gato", "cobra"]
cores = ["preto", "branco", "azul", "rosa", "verde", "vermelho", "laranja"]




def animais_aleatorios():
    animal_escolhido = random.choice(animais)
    escolher_animais_aleatorio.append(animal_escolhido)
    palavra_oculta = ["_" for _ in animal_escolhido]

    return animal_escolhido, palavra_oculta

def cores_aleatorias():
    cor_escolhida = random.choice(cores)
    escolher_cores_aleatoria.append(cor_escolhida)
    palavra_oculta = ["_" for _ in cor_escolhida]
    
    return cor_escolhida, palavra_oculta

def palavra_escondida(palavra):
    palavra_oculta = ["_" for _ in palavra]
    return palavra_oculta




while True:
    opcao = menu()
    if opcao == "1":
        tentativas = 6
        erros = 0
        escolher_animais_aleatorio = []
        letras_usadas = []
        animal, oculto = animais_aleatorios()

        while tentativas > 0:
            mostrar_tela("Animais", erros)
            print("Palavra escolhida (escondida):", " ".join(oculto))
            chute = input("Digite uma letra ou a palavra: ").lower()
            if chute.isdigit():
                print("Erro: você digitou apenas números. Tente de novo.")
            elif chute.strip() == "":
                print("Erro: não pode ser vazio. Tente de novo.")

            elif len(chute) == 1:
                if chute in letras_usadas:
                    print("Você já tentou essa letra!")
                elif chute in animal:
                    letras_usadas.append(chute)
                    for i, letra in enumerate(animal):
                        if letra == chute:
                            oculto[i] = chute
                    print("Boa! Letra encontrada.")
                else:
                    erros += 1
                    tentativas -= 1
                    mensagem = f"Você ainda tem {tentativas} tentativas." if tentativas > 0 else "Você não tem mais tentativas."
                    letras_usadas.append(chute)
                    print(f"\nErrou! {mensagem}")
                    if tentativas <= 0:
                        print("💀 Você perdeu! A palavra era:", animal)
            else:
                if chute == animal:
                    oculto = list(animal)
                else:
                    tentativas -= 1
                    print(f"Palavra errada! Você tem {tentativas} tentativas.")

                if "_" not in oculto:
                    print("\n🎉 Parabéns! Você acertou a palavra era:", animal)
                    tentativas = 6
                    escolher_animais_aleatorio.clear()
                    letras_usadas.clear()
                    break
                else:
                    print("\n💀 Você perdeu! A palavra era:", animal)
                    tentativas = 6
                    escolher_animais_aleatorio.clear()
                    letras_usadas.clear()
                    break

    

        

        
    elif opcao == "2":
        tentativas = 6
        erros = 0
        letras_usadas = []
        escolher_cores_aleatoria = []
        cor, oculto = cores_aleatorias()

        while tentativas > 0:
            mostrar_tela("Cores", erros)
            print("Palavra escolhida (escondida):", " ".join(oculto))
            chute = input("Digite uma letra ou a palavra: ").lower()
            if chute.isdigit():
                print("Erro: você digitou apenas números. Tente de novo.")
            elif chute.strip() == "":
                print("Erro: não pode ser vazio. Tente de novo.")

            elif len(chute) == 1:
                if chute in letras_usadas:
                    print("Você já tentou essa letra!")
                elif chute in cor:
                    letras_usadas.append(chute)
                    for i, letra in enumerate(cor):
                        if letra == chute:
                            oculto[i] = chute
                    print("Boa! Letra encontrada.")
                else:
                    erros += 1
                    tentativas -= 1
                    mensagem = f"Você ainda tem {tentativas} tentativas." if tentativas > 0 else "Você não tem mais tentativas."
                    letras_usadas.append(chute)
                    print(f"\nErrou! {mensagem}")
                    if tentativas <= 0:
                        print("💀 Você perdeu! A palavra era:", cor)
            else:
                if chute == cor:
                    oculto = list(cor)
                else:
                    tentativas -= 1
                    print(f"Palavra errada! Você tem {tentativas} tentativas.")

                if "_" not in oculto:
                    print("\n🎉 Parabéns! Você acertou a palavra era:", cor)
                    tentativas = 6
                    escolher_cores_aleatoria.clear()
                    letras_usadas.clear()
                    break
                else:
                    print("\n💀 Você perdeu! A palavra era:", cor)
                    tentativas = 6
                    escolher_cores_aleatoria.clear()
                    letras_usadas.clear()
                    break

    elif opcao == "3":
        tentativas = 6
        erros = 0
        palavra_escolhida = []
        letras_usadas = []

        esconder = input("Digite uma palavra, para começar o jogo: ").lower()

        if esconder.isdigit():
            print("Erro: você digitou apenas números. Tente de novo.")
        elif esconder.strip() == "":
                print("Erro: não pode ser vazio. Tente de novo.")
        else:
            palavra_escolhida.append(esconder)
            oculto = palavra_escondida(esconder)
            
        while tentativas > 0:
            mostrar_tela("Palavra Escolhida", erros)
            print("Palavra escolhida (escondida):", " ".join(oculto))
            chute = input("Digite uma letra ou a palavra: ").lower()
            if chute.isdigit():
                print("Erro: você digitou apenas números. Tente de novo.")
            elif chute.strip() == "":
                print("Erro: não pode ser vazio. Tente de novo.")

            elif len(chute) == 1:
                if chute in letras_usadas:
                    print("Você já tentou essa letra!")
                elif chute in esconder:
                    letras_usadas.append(chute)
                    for i, letra in enumerate(esconder):
                        if letra == chute:
                            oculto[i] = chute
                    print("Boa! Letra encontrada.")
                else:
                    erros += 1
                    tentativas -= 1
                    mensagem = f"Você ainda tem {tentativas} tentativas." if tentativas > 0 else "Você não tem mais tentativas."
                    letras_usadas.append(chute)
                    print(f"\nErrou! {mensagem}")
                    if tentativas <= 0:
                        print("💀 Você perdeu! A palavra era:", esconder)
            else:
                if chute == esconder:
                    oculto = list(esconder)
                else:
                    tentativas -= 1
                    print(f"Palavra errada! Você tem {tentativas} tentativas.")

                if "_" not in oculto:
                    print("\n🎉 Parabéns! Você acertou a palavra era:", esconder)
                    tentativas = 6
                    palavra_escolhida.clear()
                    letras_usadas.clear()
                    break
                else:
                    print("\n💀 Você perdeu! A palavra era:", esconder)
                    tentativas = 6
                    palavra_escolhida.clear()
                    letras_usadas.clear()
                    break
            

    elif opcao == "4":
        break
