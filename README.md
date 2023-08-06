# Jogo da Forca

**Descrição**

Este é um simples jogo da forca implementado em Python. O jogador deve tentar adivinhar a palavra oculta, letra por letra, antes que suas chances acabem. O jogo possui um total de 8 tentativas e oferece 7 temas diferentes, cada um com 10 palavras.

# Requisitos
Python 3.x

## Como Jogar

1. Clone este repositório para o seu computador ou faça o download dos arquivos.

2. Certifique-se de ter o Python 3.x instalado em sua máquina.

3. Execute o arquivo jogo_da_forca.py para iniciar o jogo.

3. O jogo irá exibir um menu principal com opções:
* [0] - Sair do jogo
* [1] - Iniciar jogo
* [2] - Informações

4. Escolha a opção [1] para iniciar o jogo.

5. Em seguida, escolha o tema desejado digitando o número correspondente. 

6. Os temas disponíveis são:

* [1] - Frutas
* [2] - Verduras
* [3] - Países
* [4] - Partes do corpo
* [5] - Eletrodomésticos
* [6] - Cores
* [7] - Formas geométricas

7. O jogo irá selecionar aleatoriamente uma palavra do tema escolhido, e a palavra oculta será apresentada com "_", indicando as letras a serem adivinhadas.

8. O jogador deverá informar uma letra por vez, utilizando letras minúsculas (acentos são ignorados, mas "ç" é tratado como uma letra diferente de "c").

9. A cada letra informada, o jogo irá atualizar a exibição da palavra oculta, revelando letras corretas.

10. O jogador tem um total de 8 tentativas para adivinhar a palavra correta. Caso erre 8 vezes, o jogo termina e a palavra correta é revelada.

11. Se o jogador adivinhar a palavra correta antes de esgotar as tentativas, o jogo é vencido.

## Sobre o Código
O código foi desenvolvido em Python e utiliza funções para facilitar a implementação do jogo. Cada tema possui uma lista de palavras correspondentes. A função choice é utilizada para selecionar aleatoriamente uma palavra do tema escolhido. O jogo é apresentado em modo texto no terminal, com a forca sendo desenhada conforme o jogador erra as letras.