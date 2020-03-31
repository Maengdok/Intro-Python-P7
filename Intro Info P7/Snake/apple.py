from kbhit import KBHit
import os
import random

game0 = "----------"
game1 = "----------"
game2 = "----------"
game3 = "----------"
game4 = "----------"
game5 = "----------"
game6 = "----------"
game7 = "----------"
game8 = "----------"
game9 = "----------"

l0 = list(game0)
l1 = list(game1)
l2 = list(game2)
l3 = list(game3)
l4 = list(game4)
l5 = list(game5)
l6 = list(game6)
l7 = list(game7)
l8 = list(game8)
l9 = list(game9)

bigList = [l0, l1, l2, l3, l4, l5, l6, l7, l8, l9]

player = "O"
apple = "°"
yI = 0
xI = 0
yJ = 1
xJ = 1
yK = -1
xK = -1
foodEaten = 0

positionList = bigList[yI]
positionList.insert(0, player)
del positionList[10]

kb = KBHit()

def show_game():
    for row in bigList:
        for elem in row:
            print(elem, end='')
        print(" ")

def food(posPlayerX, posPlayerY):
    global posAppleX
    global posAppleY
    posAppleX = random.randint(0, 9) # Position horizontale
    posAppleY = random.randint(0, 9) # Position verticale

    if posAppleX != posPlayerX or posAppleY != posPlayerY:
        bigList[posAppleY][posAppleX] = apple
        show_game()
    else:
        return food(xI, yI)

os.system('cls' if os.name == 'nt' else 'clear')
food(xI, yI)
#show_game()
print('Utilisez ZQSD pour vous déplacer.\nAppuyez sur Echap pour quitter.\nAttention, si vous touchez le mur, c\'est perdu !')


while True:

    if kb.kbhit():
        c = kb.getch()
        c_ord = ord(c)
        lenGame = len(bigList)
        newChar = "-"

        print("Nourriture mangée : {}".format(foodEaten))
        print("yI = {}\n posAppleY = {}\n xI = {}\n posAppleX = {}".format(yI, posAppleY, xI, posAppleX))

        if c_ord ==  122 or c_ord == 90: # Haut = 1
            if yI > 0 and yK > -1:
                bigList[yI][xI], bigList[yK][xI] = bigList[yK][xI], bigList[yI][xI] # Swap
                os.system('cls' if os.name == 'nt' else 'clear') # Clear terminal
                if bigList[yI][xI] == bigList[posAppleY][posAppleX]: # A corriger...
                    foodEaten += 1
                    bigList[yI][xI] = newChar # Ne remplace pas le char au bon moment...
                    food(xI, yI)
                else:
                    show_game()
            else:
                print("Vous avez perdu !")
                break

            yI -= 1
            yJ -= 1
            yK -= 1
        if c_ord == 115 or c_ord == 83: # Bas = 2
            if yJ <= lenGame - 1:
                bigList[yI][xI], bigList[yJ][xI] = bigList[yJ][xI], bigList[yI][xI] # Swap
                os.system('cls' if os.name == 'nt' else 'clear') # Clear terminal

                yI += 1
                yJ += 1
                yK += 1
                if bigList[yI][xI] == bigList[posAppleY][posAppleX]:
                    foodEaten += 1
                    bigList[yI-1][xI] = newChar
                    food(xI, yI)
                else:
                    show_game()
            else:
                print("Vous avez perdu !")
                break
        if c_ord == 113 or c_ord == 81: # Gauche = 3
            if xI > 0 and xK > -1:
                bigList[yI][xI], bigList[yI][xK] = bigList[yI][xK], bigList[yI][xI]
                os.system('cls' if os.name == 'nt' else 'clear')
                if bigList[yI][xI] == bigList[posAppleY][posAppleX]: # A corriger...
                    foodEaten += 1
                    bigList[yI][xI+1] = newChar # Ne remplace pas le char au bon moment...
                    food(xI, yI)
                else:
                    show_game()
            else:
                print("Vous avez perdu !")
                break

            xI -= 1
            xJ -= 1
            xK -= 1
        if c_ord == 100 or c_ord == 68: # Droite = 4
            if xJ <= lenGame - 1:
                bigList[yI][xI], bigList[yI][xJ] = bigList[yI][xJ], bigList[yI][xI]
                os.system('cls' if os.name == 'nt' else 'clear')

                xI += 1
                xJ += 1
                xK += 1
                if bigList[yI][xI] == bigList[posAppleY][posAppleX]:
                    foodEaten += 1
                    bigList[yI][xI-1] = newChar
                    food(xI, yI)
                else:
                    show_game()
            else:
                print("Vous avez perdu !")
                break
        if c_ord == 27: # ESC
            break
