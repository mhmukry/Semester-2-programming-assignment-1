import random

class MyGame():
    
    
    print("Welcome to my game")
    Player1 = input("Enter the name for Player 1: ")
    Player2 = input("Enter the name for Player 2: ")
    Player3 = input("Enter the name for Player 3: ")



    input(f'Player1 ({Player1}): Please press enter to roll your dice')
    Player1_dicevalue = random.randint(1, 6)
    print(f'Player1 value: {Player1_dicevalue}')


    input(f'Player2 ({Player2}): Please press enter to roll your dice')
    Player2_dicevalue = random.randint(1, 6)
    print(f'Player2 value: {Player2_dicevalue}')

    input(f'Player3 ({Player3}): Please press enter to roll your dice')
    Player3_dicevalue = random.randint(1, 6)
    print(f'Player3 value: {Player3_dicevalue}')

    if Player1_dicevalue > Player2_dicevalue and Player1_dicevalue > Player3_dicevalue:
        print(f'Player1 ({Player1}) with the value of {Player1_dicevalue}: wins the game')
    

    elif Player2_dicevalue > Player1_dicevalue and Player2_dicevalue > Player3_dicevalue:
        print(f'Player2 ({Player2})  with the value of {Player2_dicevalue}: wins the game')


    elif Player3_dicevalue > Player1_dicevalue and Player3_dicevalue > Player2_dicevalue:
        print(f'Player3 ({Player3})  with the value of {Player3_dicevalue}: wins the game')


    elif (Player1_dicevalue == Player2_dicevalue) and (Player2_dicevalue > Player3_dicevalue):
        print(f'Tie between Player 1 ({Player1}) and Player 2 ({Player2}) with the value of {Player1_dicevalue}: ')


    elif (Player1_dicevalue == Player3_dicevalue) and (Player3_dicevalue > Player2_dicevalue):
        print(f'Tie between Player 1 ({Player1}) and Player 3 ({Player3}) with the value of {Player3_dicevalue}: ')


    elif (Player2_dicevalue == Player3_dicevalue) and (Player2_dicevalue > Player1_dicevalue):
        print(f'Tie between Player 2 ({Player2}) and Player 3 ({Player3}) with the value of {Player3_dicevalue}: ') 


    elif (Player1_dicevalue == Player2_dicevalue) and (Player2_dicevalue == Player3_dicevalue):
        print(f'Tie between Player 1 ({Player1}), Player 2 ({Player2}) and Player 3 ({Player3}) with the value of {Player3_dicevalue}: ')