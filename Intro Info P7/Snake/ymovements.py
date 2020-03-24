from kbhit import KBHit
import os

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
i = 0
j = 1
k = -1

positionList = bigList[i]
positionList.insert(0, player)
del positionList[10]

kb = KBHit()

def show_game():
    for row in bigList:
        for elem in row:
            print(elem, end='')
        print(" ")

os.system('cls' if os.name == 'nt' else 'clear') # Clear terminal
show_game()
print('Appuyez sur Z pour aller vers le haut ou S pour aller vers le bas.\nAttention, si vous touchez un mur, c\'est perdu !')

while True:

    if kb.kbhit():
        c = kb.getch()
        c_ord = ord(c)
        lenGame = len(bigList)

        if c_ord ==  122 or c_ord == 90: # Haut = 1
            if i > 0 and k > -1:
                bigList[i], bigList[k] = bigList[k], bigList[i] # Swap
                os.system('cls' if os.name == 'nt' else 'clear') # Clear terminal
                show_game()
            else:
                print("Vous avez perdu !")
                break

            i -= 1
            j -= 1
            k -= 1
        if c_ord == 115 or c_ord == 83: # Bas = 2
            if j <= lenGame - 1:
                bigList[i], bigList[j] = bigList[j], bigList[i] # Swap
                os.system('cls' if os.name == 'nt' else 'clear') # Clear terminal
                show_game()

                i += 1
                j += 1
                k += 1
            else:
                print("Vous avez perdu !")
                break
        if c_ord == 27: # ESC
            break

kb.set_normal_term()
