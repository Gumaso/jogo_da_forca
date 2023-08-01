import datetime
def draw_forca(palavra):
    print(F"    {len(palavra)} - LETRAS")
    print(f"""
      ________
    |/      |
    |
    |
    |
    |
    |
   _| {"_"*len(palavra)}
   """)
def draw_head(palavra):
    print(F"    {len(palavra)} - LETRAS")
    print(f"""
      ________
    |/      |
    |      ( )
    |
    |
    |
    |
   _|{"_"*len(palavra)}
   """)
def draw_mouth(palavra):
    print(F"    {len(palavra)} - LETRAS")
    print(f"""
      ________
    |/      |
    |      (_)
    |
    |
    |
    |
   _|{"_"*len(palavra)}
   """)
def draw_neck(palavra):
    print(F"    {len(palavra)} - LETRAS")
    print(f"""
      ________
    |/      |
    |      (_)
    |       |
    |
    |
    |
   _|{"_"*len(palavra)}
    """)
def draw_body(palavra):
    print(F"    {len(palavra)} - LETRAS")
    print(f"""
      ________
    |/      |
    |      (_)
    |       |
    |       |
    |
    |
   _|{"_"*len(palavra)}
   """)
def draw_right_arm(palavra):
    print(F"    {len(palavra)} - LETRAS")
    print(f"""
      ________
    |/      |
    |      (_)
    |      \|
    |       |
    |
    |
   _|{"_"*len(palavra)}
   """)
def draw_left_arm(palavra):
    print(F"    {len(palavra)} - LETRAS")
    print(f"""
      ________
    |/      |
    |      (_)
    |      \|/
    |       |
    |
    |
   _|{"_"*len(palavra)}
   """)
def draw_right_leg(palavra):
    print(F"    {len(palavra)} - LETRAS")
    print(f"""
      ________
    |/      |
    |      (_)
    |      \|/
    |       |
    |      /
    |
   _|{"_"*len(palavra)}
   """)
def draw_left_leg(palavra):
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y")
    print(F"    {len(palavra)} - LETRAS")
    print(f"""
      ________
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / \\
    |   MORTO ({data_atual})
   _|{"_"*len(palavra)}
""")
