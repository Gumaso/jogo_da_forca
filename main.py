from desenhos import (draw_head,
                      draw_neck,
                      draw_body,
                      draw_right_arm,
                      draw_left_arm,
                      draw_right_leg,
                      draw_left_leg, )
from random import choice
frutas = ["maçã", "banana", "laranja", "uva", "abacaxi", "morango", "melancia", "pera", "manga", "kiwi"]
verduras = ["alface", "cenoura", "tomate", "brócolis", "abóbora", "cebola", "couve", "rúcula", "espinafre", "pimentão"]
paises = ["brasil", "estados unidos", "canadá", "méxico", "japão", "itália", "alemanha", "frança", "austrália", "egito"]
partes_do_corpo = ["cabeça", "braço", "perna", "mão", "pé", "olho", "nariz", "orelha", "boca", "joelho"]
eletrodomesticos = ["geladeira", "fogão", "microondas", "liquidificador", "aspirador", "centrifuga", "cafeteira", "torradeira", "batedeira", 'mixer']
cores = ["vermelho", "azul", "amarelo", "verde", "roxo", "laranja", "rosa", "preto", "branco", "marrom"]
formas_geometricas = ["triângulo", "quadrado", "retângulo", "círculo", "pentágono", "hexágono", "heptágono", "octógono", "estrela", "losango"]
print("-"*10 + "JOGO DA FORCA" + "-"*10)
while True:
    jogar = int(input("""
    [0] - Sair do jogo
    [1] - Iniciar jogo"""))
    if jogar == 0:
        print("Jogo encerrado!")
        break
    elif jogar == 1:
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
                print(palavra)
            elif tema == 2:
                palavra = choice(verduras)
                print(palavra)
            elif tema == 3:
                palavra = choice(paises)
                print(palavra)
            elif tema == 4:
                palavra = choice(partes_do_corpo)
                print(palavra)
            elif tema == 5:
                palavra = choice(eletrodomesticos)
                print(palavra)
            elif tema == 6:
                palavra = choice(cores)
                print(palavra)
            elif tema == 7:
                palavra = choice(formas_geometricas)
                print(palavra)
    else:
        print("Opção invalída")

