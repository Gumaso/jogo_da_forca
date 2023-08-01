from desenhos import (draw_head,
                      draw_mouth,
                      draw_neck,
                      draw_body,
                      draw_right_arm,
                      draw_left_arm,
                      draw_right_leg,
                      draw_left_leg,
                      draw_forca)
from random import choice

frutas = ["maçã", "banana", "laranja", "uva", "abacaxi", "morango", "melancia", "pera", "manga", "kiwi"]
verduras = ["alface", "cenoura", "tomate", "brócolis", "abóbora", "cebola", "couve", "rúcula", "espinafre", "pimentão"]
paises = ["brasil", "estados unidos", "canadá", "méxico", "japão", "itália", "alemanha", "frança", "austrália", "egito"]
partes_do_corpo = ["cabeça", "braço", "perna", "mão", "pé", "olho", "nariz", "orelha", "boca", "joelho"]
eletrodomesticos = ["geladeira", "fogão", "microondas", "liquidificador", "aspirador", "centrifuga", "cafeteira",
                    "torradeira", "batedeira", 'mixer']
cores = ["vermelho", "azul", "amarelo", "verde", "roxo", "laranja", "rosa", "preto", "branco", "marrom"]
formas_geometricas = ["triângulo", "quadrado", "retângulo", "círculo", "pentágono", "hexágono", "heptágono", "octógono",
                      "estrela", "losango"]
print("-" * 10 + "JOGO DA FORCA" + "-" * 10)
while True:
    jogar = int(input("""
    Menu principal:
    [0] - Sair do jogo
    [1] - Iniciar jogo"""))
    if jogar == 0:
        print("Jogo encerrado!")
        break
    elif jogar == 1:
        contador = 0
        while True:
            tema = int(input("""
                    Escolha um tema entre os disponiveis:
                    [1] - Frutas
                    [2] - Verduras
                    [3] - Países
                    [4] - Partes do corpo
                    [5] - Eletrodomésticos
                    [6] - Cores
                    [7] - Formas geométricas
                    """))
            if tema not in range(1, 8):
                print("Opção invalída!")
            elif tema == 1:
                palavra = choice(frutas)
                print("Palavra do tema selecionada")
                palavra_oculta = "_" * len(palavra)
                while True:
                    letra = input("Digite uma letra:")
                    if letra not in palavra:
                        pass
                    if letra in palavra:
                        indice = palavra.index(letra)
                        palavra_oculta[indice].replace('_', letra)


            elif tema == 2:
                palavra = choice(verduras)
                print("Palavra do tema selecionada")
                while True:
                    letra = input("Digite uma letra:")
                    if letra not in palavra:
                        pass
            elif tema == 3:
                palavra = choice(paises)
                print("Palavra do tema selecionada")
                while True:
                    letra = input("Digite uma letra:")
                    if letra not in palavra:
                        pass
            elif tema == 4:
                palavra = choice(partes_do_corpo)
                print("Palavra do tema selecionada")
                while True:
                    letra = input("Digite uma letra:")
                    if letra not in palavra:
                        pass
            elif tema == 5:
                palavra = choice(eletrodomesticos)
                print("Palavra do tema selecionada")
                while True:
                    letra = input("Digite uma letra:")
                    if letra not in palavra:
                        pass
            elif tema == 6:
                palavra = choice(cores)
                print("Palavra do tema selecionada")
                while True:
                    letra = input("Digite uma letra:")
                    if letra not in palavra:
                        pass
            elif tema == 7:
                palavra = choice(formas_geometricas)
                print("Palavra do tema selecionada")
                while True:
                    letra = input("Digite uma letra:")
                    if letra not in palavra:
                        pass
    else:
        print("Opção invalída")
