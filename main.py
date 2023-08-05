# Importação de funções específicas do módulo "desenhos"
from desenhos import (forca, substituindo_letras, forca_acertou)

# Importação do módulo "choice" da biblioteca "random"
from random import choice

# Importação das funções específicas do módulo "cores"
from cores import modificar_letra, modificar_fundo

# Listas de palavras para os temas disponíveis
frutas = ["maça", "banana", "laranja", "uva", "abacaxi", "morango", "melancia", "pera", "manga", "kiwi"]
verduras = ["alface", "cenoura", "tomate", "brocolis", "abobora", "cebola", "couve", "rucula", "espinafre", "pimentao"]
paises = ["brasil", "estados unidos", "canada", "mexico", "japao", "italia", "alemanha", "frança", "australia", "egito"]
partes_do_corpo = ["cabeça", "braço", "perna", "mao", "pe", "olho", "nariz", "orelha", "boca", "joelho"]
eletrodomesticos = ["geladeira", "fogao", "microondas", "liquidificador", "aspirador", "centrifuga", "cafeteira",
                    "torradeira", "batedeira", 'mixer']
cores = ["vermelho", "azul", "amarelo", "verde", "roxo", "laranja", "rosa", "preto", "branco", "marrom"]
formas_geometricas = ["triangulo", "quadrado", "retangulo", "circulo", "pentagono", "hexagono", "heptagono", "octogono",
                      "estrela", "losango"]

# Mensagem de boas-vindas
print("-" * 10 + "JOGO DA FORCA" + "-" * 10)

#Loop principal do jogo
while True:
    # Exibição do menu principal
    jogar = int(input(f"""
    Menu principal:
    {modificar_letra.letra_AMARELA}[0] - Sair do jogo{modificar_letra.limpar_cores}
    {modificar_letra.letra_AZUL}[1] - Iniciar jogo{modificar_letra.limpar_cores}
    {modificar_letra.letra_VERDE}[2] - Informações{modificar_letra.limpar_cores}\n\t"""))

    if jogar == 0:
        # Encerramento do jogo caso a opção 0 seja escolhida
        print("Jogo encerrado!")
        break
    elif jogar == 1:
        # Início do jogo caso a opção 1 seja escolhida
        contador = 0
        while True:
            while True:
                try:
                    # Seleção do tema pelo usuário
                    tema = int(input(f"""
                            Escolha um tema entre os disponiveis:
                            {modificar_letra.letra_AMARELA}[00] - Menu principal{modificar_letra.limpar_cores}
                            [1] - Frutas
                            [2] - Verduras
                            [3] - Países
                            [4] - Partes do corpo
                            [5] - Eletrodomésticos
                            [6] - Cores
                            [7] - Formas geométricas
                            """))
                except ValueError:
                    print(f'Apenas números e positivos!')
                else:
                    break

            if tema not in range(1, 8) and tema != 00:
                # Mensagem de erro caso a opção do tema seja inválida
                print("Opção invalída!")
            elif tema == 00:
                # Retornar ao menu principal caso o usuário escolha a opção 00
                break

            elif tema == 1:
                # Jogo com o tema "Frutas"
                palavra = choice(frutas)
                palavra_oculta = list("_" * len(palavra))
                print('TEMA - FRUTAS')
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
                alfabeto = []
                letras_certas = []
                while True:
                    letra = input("Letra:").lower()
                    retorno_funcao = substituindo_letras(palavra=palavra, palavra_oculta=palavra_oculta, letra=letra)
                    if letra in alfabeto:
                        # Mensagem informando que a letra já foi informada anteriormente
                        print(modificar_letra.letra_AMARELA + "Letra já informada: " + modificar_letra.limpar_cores)
                        print(alfabeto)
                        continue
                    elif letra in letras_certas:
                        # Mensagem informando que a letra já foi acertada anteriormente
                        print(modificar_letra.letra_CIANO + "Letra já acertada!" + modificar_letra.limpar_cores)
                        continue
                    elif letra in palavra:
                        # Tratamento do acerto de letras
                        forca_acertou(soma=soma, funcao=retorno_funcao, letra=letra, modificar_letra=modificar_letra)
                        letras_certas.append(letra)
                        if palavra == retorno_funcao:
                            # Caso a palavra tenha sido completamente adivinhada
                            print(
                                modificar_letra.letra_CIANO + "******   Palavra completa   ******" + modificar_letra.limpar_cores)
                            break
                    elif letra not in palavra and letra not in alfabeto:
                        # Tratamento do erro de letras
                        print(f"{modificar_letra.letra_VERMELHA}Letra incorreta {letra}{modificar_letra.limpar_cores}")
                        alfabeto.append(letra)
                        soma += 1
                        forca(funcao=retorno_funcao, soma=soma)

                    if soma == 8:
                        # Condição de derrota
                        print("Você perdeu o jogo!")
                        print(f'A palavra era: {palavra}')
                        break
            elif tema == 2:
                # Seleciona uma palavra aleatória do tema "Verduras"
                palavra = choice(verduras)
                # Cria uma lista com underscores para representar a palavra oculta
                palavra_oculta = list("_" * len(palavra))
                print('TEMA - VERDURAS')
                print(f"Palavra do tema selecionada {len(palavra)} - LETRAS")
                # Exibição inicial da forca com a palavra oculta
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
                # Variáveis para controlar as tentativas e letras informadas
                soma = 0
                alfabeto = []
                letras_certas = []
                while True:
                    # Captura da letra informada pelo jogador
                    letra = input("Letra:").lower()
                    # Chama a função "substituindo_letras" para atualizar a palavra oculta
                    retorno_funcao = substituindo_letras(palavra=palavra, palavra_oculta=palavra_oculta,
                                                         letra=letra)
                    if letra in alfabeto:
                        # Mensagem informando que a letra já foi informada anteriormente
                        print(
                            modificar_letra.letra_AMARELA + "Letra já informada: " + modificar_letra.limpar_cores)
                        print(alfabeto)
                        continue
                    elif letra in letras_certas:
                        # Mensagem informando que a letra já foi acertada anteriormente
                        print(modificar_letra.letra_CIANO + "Letra já acertada!" + modificar_letra.limpar_cores)
                        continue
                    elif letra in palavra:
                        # Tratamento do acerto de letras
                        forca_acertou(soma=soma, funcao=retorno_funcao, letra=letra,
                                      modificar_letra=modificar_letra)
                        letras_certas.append(letra)
                        if palavra == retorno_funcao:
                            # Caso a palavra tenha sido completamente adivinhada
                            print(
                                modificar_letra.letra_CIANO + "******   Palavra completa   ******" + modificar_letra.limpar_cores)
                            break
                    elif letra not in palavra and letra not in alfabeto:
                        # Tratamento do erro de letras
                        print(
                            f"{modificar_letra.letra_VERMELHA}Letra incorreta {letra}{modificar_letra.limpar_cores}")
                        alfabeto.append(letra)
                        soma += 1
                        forca(funcao=retorno_funcao, soma=soma)

                    if soma == 8:
                        # Condição de derrota
                        print("Você perdeu o jogo!")
                        print(f'A palavra era: {palavra}')
                        break
            elif tema == 3:
                # Seleciona uma palavra aleatória do tema "Países"
                palavra = choice(paises)
                # Cria uma lista com underscores para representar a palavra oculta
                palavra_oculta = list("_" * len(palavra))
                print('TEMA - PAÍSES')
                print(f"Palavra do tema selecionada {len(palavra)} - LETRAS")
                # Exibição inicial da forca com a palavra oculta
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
                # Variáveis para controlar as tentativas e letras informadas
                soma = 0
                alfabeto = []
                letras_certas = []
                while True:
                    # Captura da letra informada pelo jogador
                    letra = input("Letra:").lower()
                    # Chama a função "substituindo_letras" para atualizar a palavra oculta
                    retorno_funcao = substituindo_letras(palavra=palavra, palavra_oculta=palavra_oculta,
                                                         letra=letra)
                    if letra in alfabeto:
                        # Mensagem informando que a letra já foi informada anteriormente
                        print(
                            modificar_letra.letra_AMARELA + "Letra já informada: " + modificar_letra.limpar_cores)
                        print(alfabeto)
                        continue
                    elif letra in letras_certas:
                        # Mensagem informando que a letra já foi acertada anteriormente
                        print(modificar_letra.letra_CIANO + "Letra já acertada!" + modificar_letra.limpar_cores)
                        continue
                    elif letra in palavra:
                        # Tratamento do acerto de letras
                        forca_acertou(soma=soma, funcao=retorno_funcao, letra=letra,
                                      modificar_letra=modificar_letra)
                        letras_certas.append(letra)
                        if palavra == retorno_funcao:
                            # Caso a palavra tenha sido completamente adivinhada
                            print(
                                modificar_letra.letra_CIANO + "******   Palavra completa   ******" + modificar_letra.limpar_cores)
                            break
                    elif letra not in palavra and letra not in alfabeto:
                        # Tratamento do erro de letras
                        print(
                            f"{modificar_letra.letra_VERMELHA}Letra incorreta {letra}{modificar_letra.limpar_cores}")
                        alfabeto.append(letra)
                        soma += 1
                        forca(funcao=retorno_funcao, soma=soma)

                    if soma == 8:
                        # Condição de derrota
                        print("Você perdeu o jogo!")
                        print(f'A palavra era: {palavra}')
                        break
            elif tema == 4:
                # Seleciona uma palavra aleatória do tema "Partes do Corpo"
                palavra = choice(partes_do_corpo)
                # Cria uma lista com underscores para representar a palavra oculta
                palavra_oculta = list("_" * len(palavra))
                print('TEMA - PARTES DO CORPO')
                print(f"Palavra do tema selecionada {len(palavra)} - LETRAS")
                # Exibição inicial da forca com a palavra oculta
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
                # Variáveis para controlar as tentativas e letras informadas
                soma = 0
                alfabeto = []
                letras_certas = []
                while True:
                    # Captura da letra informada pelo jogador
                    letra = input("Letra:").lower()
                    # Chama a função "substituindo_letras" para atualizar a palavra oculta
                    retorno_funcao = substituindo_letras(palavra=palavra, palavra_oculta=palavra_oculta, letra=letra)
                    if letra in alfabeto:
                        # Mensagem informando que a letra já foi informada anteriormente
                        print(modificar_letra.letra_AMARELA + "Letra já informada: " + modificar_letra.limpar_cores)
                        print(alfabeto)
                        continue
                    elif letra in letras_certas:
                        # Mensagem informando que a letra já foi acertada anteriormente
                        print(modificar_letra.letra_CIANO + "Letra já acertada!" + modificar_letra.limpar_cores)
                        continue
                    elif letra in palavra:
                        # Tratamento do acerto de letras
                        forca_acertou(soma=soma, funcao=retorno_funcao, letra=letra, modificar_letra=modificar_letra)
                        letras_certas.append(letra)
                        if palavra == retorno_funcao:
                            # Caso a palavra tenha sido completamente adivinhada
                            print(
                                modificar_letra.letra_CIANO + "******   Palavra completa   ******" + modificar_letra.limpar_cores)
                            break
                    elif letra not in palavra and letra not in alfabeto:
                        # Tratamento do erro de letras
                        print(f"{modificar_letra.letra_VERMELHA}Letra incorreta {letra}{modificar_letra.limpar_cores}")
                        alfabeto.append(letra)
                        soma += 1
                        forca(funcao=retorno_funcao, soma=soma)

                    if soma == 8:
                        # Condição de derrota
                        print("Você perdeu o jogo!")
                        print(f'A palavra era: {palavra}')
                        break

            elif tema == 5:
                # Seleciona uma palavra aleatória do tema "Eletrodomésticos"
                palavra = choice(eletrodomesticos)
                # Cria uma lista com underscores para representar a palavra oculta
                palavra_oculta = list("_" * len(palavra))
                print('TEMA - ELETRODOMÉSTICOS')
                print(f"Palavra do tema selecionada {len(palavra)} - LETRAS")
                # Exibição inicial da forca com a palavra oculta
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
                # Variáveis para controlar as tentativas e letras informadas
                soma = 0
                alfabeto = []
                letras_certas = []
                while True:
                    # Captura da letra informada pelo jogador
                    letra = input("Letra:").lower()
                    # Chama a função "substituindo_letras" para atualizar a palavra oculta
                    retorno_funcao = substituindo_letras(palavra=palavra, palavra_oculta=palavra_oculta, letra=letra)
                    if letra in alfabeto:
                        # Mensagem informando que a letra já foi informada anteriormente
                        print(modificar_letra.letra_AMARELA + "Letra já informada: " + modificar_letra.limpar_cores)
                        print(alfabeto)
                        continue
                    elif letra in letras_certas:
                        # Mensagem informando que a letra já foi acertada anteriormente
                        print(modificar_letra.letra_CIANO + "Letra já acertada!" + modificar_letra.limpar_cores)
                        continue
                    elif letra in palavra:
                        # Tratamento do acerto de letras
                        forca_acertou(soma=soma, funcao=retorno_funcao, letra=letra, modificar_letra=modificar_letra)
                        letras_certas.append(letra)
                        if palavra == retorno_funcao:
                            # Caso a palavra tenha sido completamente adivinhada
                            print(
                                modificar_letra.letra_CIANO + "******   Palavra completa   ******" + modificar_letra.limpar_cores)
                            break
                    elif letra not in palavra and letra not in alfabeto:
                        # Tratamento do erro de letras
                        print(f"{modificar_letra.letra_VERMELHA}Letra incorreta {letra}{modificar_letra.limpar_cores}")
                        alfabeto.append(letra)
                        soma += 1
                        forca(funcao=retorno_funcao, soma=soma)

                    if soma == 8:
                        # Condição de derrota
                        print("Você perdeu o jogo!")
                        print(f'A palavra era: {palavra}')
                        break
            elif tema == 6:
                # Seleciona uma palavra aleatória do tema "Cores"
                palavra = choice(cores)
                # Cria uma lista com underscores para representar a palavra oculta
                palavra_oculta = list("_" * len(palavra))
                print('TEMA - CORES')
                print(f"Palavra do tema selecionada {len(palavra)} - LETRAS")
                # Exibição inicial da forca com a palavra oculta
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
                # Variáveis para controlar as tentativas e letras informadas
                soma = 0
                alfabeto = []
                letras_certas = []
                while True:
                    # Captura da letra informada pelo jogador
                    letra = input("Letra:").lower()
                    # Chama a função "substituindo_letras" para atualizar a palavra oculta
                    retorno_funcao = substituindo_letras(palavra=palavra, palavra_oculta=palavra_oculta, letra=letra)
                    if letra in alfabeto:
                        # Mensagem informando que a letra já foi informada anteriormente
                        print(modificar_letra.letra_AMARELA + "Letra já informada: " + modificar_letra.limpar_cores)
                        print(alfabeto)
                        continue
                    elif letra in letras_certas:
                        # Mensagem informando que a letra já foi acertada anteriormente
                        print(modificar_letra.letra_CIANO + "Letra já acertada!" + modificar_letra.limpar_cores)
                        continue
                    elif letra in palavra:
                        # Tratamento do acerto de letras
                        forca_acertou(soma=soma, funcao=retorno_funcao, letra=letra, modificar_letra=modificar_letra)
                        letras_certas.append(letra)
                        if palavra == retorno_funcao:
                            # Caso a palavra tenha sido completamente adivinhada
                            print(
                                modificar_letra.letra_CIANO + "******   Palavra completa   ******" + modificar_letra.limpar_cores)
                            break
                    elif letra not in palavra and letra not in alfabeto:
                        # Tratamento do erro de letras
                        print(f"{modificar_letra.letra_VERMELHA}Letra incorreta {letra}{modificar_letra.limpar_cores}")
                        alfabeto.append(letra)
                        soma += 1
                        forca(funcao=retorno_funcao, soma=soma)

                    if soma == 8:
                        # Condição de derrota
                        print("Você perdeu o jogo!")
                        print(f'A palavra era: {palavra}')
                        break

            elif tema == 7:
                # Seleciona uma palavra aleatória do tema "Formas Geométricas"
                palavra = choice(formas_geometricas)
                # Cria uma lista com underscores para representar a palavra oculta
                palavra_oculta = list("_" * len(palavra))
                print('TEMA - FORMAS GEOMÉTRICAS')
                print(f"Palavra do tema selecionada {len(palavra)} - LETRAS")
                # Exibição inicial da forca com a palavra oculta
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
                # Variáveis para controlar as tentativas e letras informadas
                soma = 0
                alfabeto = []
                letras_certas = []
                while True:
                    # Captura da letra informada pelo jogador
                    letra = input("Letra:").lower()
                    # Chama a função "substituindo_letras" para atualizar a palavra oculta
                    retorno_funcao = substituindo_letras(palavra=palavra, palavra_oculta=palavra_oculta, letra=letra)
                    if letra in alfabeto:
                        # Mensagem informando que a letra já foi informada anteriormente
                        print(modificar_letra.letra_AMARELA + "Letra já informada: " + modificar_letra.limpar_cores)
                        print(alfabeto)
                        continue
                    elif letra in letras_certas:
                        # Mensagem informando que a letra já foi acertada anteriormente
                        print(modificar_letra.letra_CIANO + "Letra já acertada!" + modificar_letra.limpar_cores)
                        continue
                    elif letra in palavra:
                        # Tratamento do acerto de letras
                        forca_acertou(soma=soma, funcao=retorno_funcao, letra=letra, modificar_letra=modificar_letra)
                        letras_certas.append(letra)
                        if palavra == retorno_funcao:
                            # Caso a palavra tenha sido completamente adivinhada
                            print(
                                modificar_letra.letra_CIANO + "******   Palavra completa   ******" + modificar_letra.limpar_cores)
                            break
                    elif letra not in palavra and letra not in alfabeto:
                        # Tratamento do erro de letras
                        print(f"{modificar_letra.letra_VERMELHA}Letra incorreta {letra}{modificar_letra.limpar_cores}")
                        alfabeto.append(letra)
                        soma += 1
                        forca(funcao=retorno_funcao, soma=soma)

                    if soma == 8:
                        # Condição de derrota
                        print("Você perdeu o jogo!")
                        print(f'A palavra era: {palavra}')
                        break
    elif jogar == 2:
        print(modificar_letra.letra_VERDE + """
        Bem-vindo(a) ao Jogo da Forca!

Neste jogo, você terá 8 tentativas para adivinhar a palavra secreta. Cada palavra pertence a um dos 7 temas disponíveis,
e todas elas são compostas por letras sem acentos, diferenciando "ç" e "c".
 Vamos começar!

Temas Disponíveis:

Animais
Países
Frutas
Profissões
Cores
Esportes
Comidas
Escolha um número entre 1 e 7 para selecionar um tema e começar a jogar:

Instruções:

Digite apenas uma letra por tentativa.
A palavra secreta será exibida com "_", representando as letras não reveladas.
Caso você acerte uma letra, ela será mostrada na posição correta da palavra.
Se você errar uma letra, perderá uma tentativa.
Boa sorte!
Para sair do jogo, digite 0 a qualquer momento.

Escolha um tema (digite o número) ou 0 para encerrar o jogo""" + modificar_letra.limpar_cores)
    else:
        print("Opção invalída")
