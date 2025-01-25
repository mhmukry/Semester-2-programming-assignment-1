import random

class MyGame_version3():
    
    
    print("Welcome to my game")
    Player1 = input("Enter the name for Player 1: ")
    Player2 = input("Enter the name for Player 2: ")
    Player3 = input("Enter the name for Player 3: ")



    input(f'Player1 ({Player1}): Please press enter to roll your dice')
    Player1_dicevalue1 = random.randint(1, 6)
    print(f'Player1 value: {Player1_dicevalue1}')

    input(f'Player2 ({Player2}): Please press enter to roll your dice')
    Player2_dicevalue1 = random.randint(1, 6)
    print(f'Player2 value: {Player2_dicevalue1}')

    input(f'Player3 ({Player3}): Please press enter to roll your dice')
    Player3_dicevalue1 = random.randint(1, 6)
    print(f'Player3 value: {Player3_dicevalue1}')

    input(f'Player1 ({Player1}): Please press enter to roll your dice')
    Player1_dicevalue2 = random.randint(1, 6)
    print(f'Player1 value: {Player1_dicevalue2}')

    input(f'Player2 ({Player2}): Please press enter to roll your dice')
    Player2_dicevalue2 = random.randint(1, 6)
    print(f'Player2 value: {Player2_dicevalue2}')

    input(f'Player3 ({Player3}): Please press enter to roll your dice')
    Player3_dicevalue2 = random.randint(1, 6)
    print(f'Player3 value: {Player3_dicevalue2}')

    Player1_total_dicevalue = Player1_dicevalue1 + Player1_dicevalue2
    Player2_total_dicevalue = Player2_dicevalue1 + Player2_dicevalue2
    Player3_total_dicevalue = Player3_dicevalue1 + Player3_dicevalue2

    average1 = (Player1_total_dicevalue + Player2_total_dicevalue + Player3_total_dicevalue)/3
    average2 = (Player1_total_dicevalue + Player2_total_dicevalue + Player3_total_dicevalue)//3
    print(f'average1 = (Player1_total_dicevalue + Player2_total_dicevalue + Player3_total_dicevalue)/3 is :{average1} ')
    print(f'average2 = (Player1_total_dicevalue + Player2_total_dicevalue + Player3_total_dicevalue)//3 is :{average2} ')


    if Player1_total_dicevalue > Player2_total_dicevalue and Player1_total_dicevalue > Player3_total_dicevalue:
        print(f'Player1 ({Player1}) with the total value of {Player1_total_dicevalue}: wins the game')
    

    elif Player2_total_dicevalue > Player1_total_dicevalue and Player2_total_dicevalue > Player3_total_dicevalue:
        print(f'Player2 ({Player2})  with the total value of {Player2_total_dicevalue}: wins the game')


    elif Player3_total_dicevalue > Player1_total_dicevalue and Player3_total_dicevalue > Player2_total_dicevalue:
        print(f'Player3 ({Player3})  with the total value of {Player3_total_dicevalue}: wins the game')


    elif (Player1_total_dicevalue == Player2_total_dicevalue) and (Player2_total_dicevalue > Player3_total_dicevalue):
        print(f'Tie between Player 1 ({Player1}) and Player 2 ({Player2}) with the total value of {Player1_total_dicevalue}: ')


    elif (Player1_total_dicevalue == Player3_total_dicevalue) and (Player3_total_dicevalue > Player2_total_dicevalue):
        print(f'Tie between Player 1 ({Player1}) and Player 3 ({Player3}) with the total value of {Player3_total_dicevalue}: ')


    elif (Player2_total_dicevalue == Player3_total_dicevalue) and (Player2_total_dicevalue > Player1_total_dicevalue):
        print(f'Tie between Player 2 ({Player2}) and Player 3 ({Player3}) with the total value of {Player3_total_dicevalue}: ') 


    elif (Player1_total_dicevalue == Player2_total_dicevalue) and (Player2_total_dicevalue == Player3_total_dicevalue):
        print(f'Tie between Player 1 ({Player1}), Player 2 ({Player2}) and Player 3 ({Player3}) with the total value of {Player3_total_dicevalue}: ')