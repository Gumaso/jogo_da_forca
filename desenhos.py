import datetime
def forca_acertou(soma, funcao, letra):
    if soma == 0:
        print(f"""
                    Contém a letra ({letra})
                      ________
                    |/      |
                    |      
                    |
                    |
                    |
                    |
                   _|{funcao}
                   """)
    elif soma == 1:
        print(f"""
       ________
     |/      |
     |     (   )
     |
     |
     |
     |
    _|{funcao}
    """)
    elif soma == 2:
        print(f"""
      ________
    |/      |
    |     (o-o)
    |
    |
    |
    |
   _|{funcao}
   """)

    elif soma == 3:
        print(f"""
          ________
        |/      |
        |     (o-o)
        |       |
        |
       _|{funcao}
        """)
    elif soma == 4:
        print(f"""
              ________
            |/      |
            |     (o-o)
            |       |
            |       |
            |
            |
           _|{funcao}
           """)
    elif soma == 5:
        print(f"""
                  ________
                |/      |
                |     (o-o)
                |      \|
                |       |
                |
                |
               _|{funcao}
               """)
    elif soma == 6:
        print(f"""
                      ________
                    |/      |
                    |     (o-o)
                    |      \|/
                    |       |
                    |
                    |
                   _|{funcao}
                   """)
    elif soma == 7:
        print(f"""
                          ________
                        |/      |
                        |     (o-o)
                        |      \|/
                        |       |
                        |      /
                        |
                       _|{funcao}
                       """)

def substituindo_letras(palavra, palavra_oculta, letra):
    for x in range(len(palavra)):
        if letra == palavra[x]:
            item = {palavra[x]: x}
            palavra_oculta[item[palavra[x]]] = palavra[x]
    palavra_corrigida = ''.join(palavra_oculta)
    return palavra_corrigida






def forca(soma, funcao, letra):
    if soma == 1:
        print(f"""
                     LETRA INCORRETA {letra}
                       ________
                     |/      |
                     |      ( )
                     |
                     |
                     |
                     |
                    _|{funcao}
                    """)
    elif soma == 2:
        print(f"""
        LETRA INCORRETA {letra}
           ________
         |/      |
         |     (o-o)
         |
         |
         |
         |
        _|{funcao}
        """)

    elif soma == 3:
        print(f"""
        LETRA INCORRETA {letra}
           ________
         |/      |
         |     (o-o)
         |       |
         |
        _|{funcao}
         """)
    elif soma == 4:
        print(f"""
            LETRA INCORRETA {letra}
               ________
             |/      |
             |     (o-o)
             |       |
             |       |
             |
             |
            _|{funcao}
            """)
    elif soma == 5:
        print(f"""
                LETRA INCORRETA {letra}
                   ________
                 |/      |
                 |     (o-o)
                 |      \|
                 |       |
                 |
                 |
                _|{funcao}
                """)
    elif soma == 6:
        print(f"""
                    LETRA INCORRETA {letra}
                       ________
                     |/      |
                     |     (o-o)
                     |      \|/
                     |       |
                     |
                     |
                    _|{funcao}
                    """)
    elif soma == 7:
        print(f"""
                        LETRA INCORRETA {letra}
                           ________
                         |/      |
                         |     (o-o)
                         |      \|/
                         |       |
                         |      /
                         |
                        _|{funcao}
                        """)
    elif soma == 8:
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y")
        print(f"""
                    LETRA INCORRETA {letra}
                       ________
                     |/      |
                     |     (x-x)
                     |      \|/
                     |       |
                     |      / \\
                     |   MORTO ({data_atual})
                    _|{funcao}
                         """)
