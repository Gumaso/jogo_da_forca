import datetime
def draw_head():
    print("""
      ________
    |/      |
    |      (_)
    |
    |
    |
    |
   _|___
   """)
def draw_neck():
    print("""
      ________
    |/      |
    |      (_)
    |       |
    |
    |
    |
   _|___
    """)
def draw_body():
    print("""
      ________
    |/      |
    |      (_)
    |       |
    |       |
    |
    |
   _|___
   """)
def draw_right_arm():
    print("""
      ________
    |/      |
    |      (_)
    |      \|
    |       |
    |
    |
   _|___""")
def draw_left_arm():
    print("""
      ________
    |/      |
    |      (_)
    |      \|/
    |       |
    |
    |
   _|___""")
def draw_right_leg():
    print("""
      ________
    |/      |
    |      (_)
    |      \|/
    |       |
    |      /
    |
   _|___""")
def draw_left_leg():
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y")

    print(f"""
      ________
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / \\
    |   MORTO ({data_atual})
   _|___""")


