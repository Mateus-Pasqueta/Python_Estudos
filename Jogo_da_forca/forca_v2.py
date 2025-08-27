import random
import textwrap

# ================= MENU =================
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

# ================= DESENHO FORCA =================
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

# ================= LISTAS =================
animais = ["leao", "elefante", "macaco", "tigre", "cachorro", "gato", "cobra"]
cores   = ["preto", "branco", "azul", "rosa", "verde", "vermelho", "laranja"]

# ================= FUNÇÕES =================
def mostrar_tela(categoria, erros=0):
    print(f"\n===== CATEGORIA: {categoria.upper()} =====")
    print(forca[erros])

def palavra_oculta(palavra):
    return ["_" for _ in palavra]

def jogar(palavra, categoria):
    tentativas = 6
    erros = 0
    letras_usadas = []
    oculto = palavra_oculta(palavra)

    while tentativas > 0:
        mostrar_tela(categoria, erros)
        print("Palavra:", " ".join(oculto))
        print("Letras usadas:", ", ".join(letras_usadas))
        chute = input("Digite uma letra ou a palavra: ").lower()

       
        if chute.isdigit():
            print("Erro: você digitou apenas números. Tente de novo.")
            
        elif chute.strip() == "":
            print("Erro: não pode ser vazio. Tente de novo.")
            

       
        if len(chute) == 1:
            if chute in letras_usadas:
                print("Você já tentou essa letra!")
            elif chute in palavra:
                letras_usadas.append(chute)
                for i, letra in enumerate(palavra):
                    if letra == chute:
                        oculto[i] = chute
                print("Boa! Letra encontrada.")
            else:
                erros += 1
                tentativas -= 1
                letras_usadas.append(chute)
                print(f"\nErrou! Você ainda tem {tentativas} tentativas.")
        else:  
            if chute == palavra:
                oculto = list(palavra)
            else:
                tentativas -= 1
                print(f"Palavra errada! Você tem {tentativas} tentativas.")

       
        if "_" not in oculto:
            print("\n🎉 Parabéns! Você acertou a palavra era:", palavra)
            break
        elif tentativas <= 0:
            print("\n💀 Você perdeu! A palavra era:", palavra)
            break

# ================= LOOP PRINCIPAL =================
while True:
    opcao = menu()
    if opcao == "1":
        palavra = random.choice(animais)
        jogar(palavra, "Animais")

    elif opcao == "2":
        palavra = random.choice(cores)
        jogar(palavra, "Cores")

    elif opcao == "3":
        palavra = input("Digite uma palavra, para começar o jogo: ").lower()
        if palavra.isdigit() or palavra.strip() == "":
            print("Palavra inválida! Tente de novo.")
        else:
            jogar(palavra, "Palavra escolhida")

    elif opcao == "4":
        print("Saindo do jogo...")
        break

    else:
        print("Opção inválida! Escolha entre 1 e 4.")
