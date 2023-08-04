from desenhos import (forca, substituindo_letras, forca_acertou)
from random import choice

frutas = ["maça", "banana", "laranja", "uva", "abacaxi", "morango", "melancia", "pera", "manga", "kiwi"]
verduras = ["alface", "cenoura", "tomate", "brocolis", "abobora", "cebola", "couve", "rucula", "espinafre", "pimentao"]
paises = ["brasil", "estados unidos", "canada", "mexico", "japao", "italia", "alemanha", "frança", "australia", "egito"]
partes_do_corpo = ["cabeça", "braço", "perna", "mao", "pe", "olho", "nariz", "orelha", "boca", "joelho"]
eletrodomesticos = ["geladeira", "fogao", "microondas", "liquidificador", "aspirador", "centrifuga", "cafeteira",
                    "torradeira", "batedeira", 'mixer']
cores = ["vermelho", "azul", "amarelo", "verde", "roxo", "laranja", "rosa", "preto", "branco", "marrom"]
formas_geometricas = ["triangulo", "quadrado", "retangulo", "circulo", "pentagono", "hexagono", "heptagono", "octogono",
                      "estrela", "losango"]
print("-" * 10 + "JOGO DA FORCA" + "-" * 10)
while True:
    jogar = int(input("""
    Menu principal:
    [0] - Sair do jogo
    [1] - Iniciar jogo\n\t"""))
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
                palavra_oculta = list("_" * len(palavra))
                print(f"Palavra do tema selecionada {len(palavra)} - LETRAS")
                print(f"""
                                          ________
                                        |/      |
                                        |      
                                        |
                                        |
                                        |
                                        |
                                       _|{"_" * len(palavra)}
                                       """)
                soma = 0
                while True:
                    letra = input("Letra:").lower()
                    retorno_funcao = substituindo_letras(palavra=palavra, palavra_oculta=palavra_oculta, letra=letra)
                    if letra in palavra:
                        forca_acertou(soma=soma, funcao=retorno_funcao, letra=letra)
                        if palavra == retorno_funcao:
                            print("Palavra completa")
                            break
                    else:
                        soma += 1
                        forca(funcao=retorno_funcao, soma=soma, letra=letra)


            elif tema == 2:
                palavra = choice(verduras)
                palavra_oculta = "_" * len(palavra)
                print("Palavra do tema selecionada")
                while True:
                    letra = input("Digite uma letra:").lower()
                    if letra not in palavra:
                        pass
            elif tema == 3:
                palavra = choice(paises)
                palavra_oculta = "_" * len(palavra)
                print("Palavra do tema selecionada")
                while True:
                    letra = input("Digite uma letra:").lower()
                    if letra not in palavra:
                        pass
            elif tema == 4:
                palavra = choice(partes_do_corpo)
                palavra_oculta = "_" * len(palavra)
                print("Palavra do tema selecionada")
                while True:
                    letra = input("Digite uma letra:").lower()
                    if letra not in palavra:
                        pass
            elif tema == 5:
                palavra = choice(eletrodomesticos)
                palavra_oculta = "_" * len(palavra)
                print("Palavra do tema selecionada")
                while True:
                    letra = input("Digite uma letra:").lower()
                    if letra not in palavra:
                        pass
            elif tema == 6:
                palavra = choice(cores)
                palavra_oculta = "_" * len(palavra)
                print("Palavra do tema selecionada")
                while True:
                    letra = input("Digite uma letra:").lower()
                    if letra not in palavra:
                        pass
            elif tema == 7:
                palavra = choice(formas_geometricas)
                palavra_oculta = "_" * len(palavra)
                print("Palavra do tema selecionada")
                while True:
                    letra = input("Digite uma letra:").lower()
                    if letra not in palavra:
                        pass
    else:
        print("Opção invalída")
