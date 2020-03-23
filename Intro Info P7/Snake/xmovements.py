from kbhit import KBHit

kb = KBHit()

print('Appuyez sur Q pour aller à gauche ou D pour aller à droite.\nAttention, si vous touchez un mur, c\'est perdu !')

game = "----------"
l = list(game)
player = "O"

l.insert(0, player)
print(''.join(l))

i = 0
j = 1
k = -1

while True:

    if kb.kbhit():
        c = kb.getch()
        c_ord = ord(c)
        lenGame = len(l)


        if c_ord == 113 or c_ord == 81: # Gauche = 3
            if i > 0 and k > -1:
                l[i], l[k] = l[k], l[i] # Swap
                print(''.join(l))
            else:
                print("Vous avez perdu !")
                break

            i -= 1
            j -= 1
            k -= 1
        if c_ord == 100 or c_ord == 68: # Droite = 4
            if j <= lenGame - 1:
                l[i], l[j] = l[j], l[i] # Swap
                print(''.join(l))

                i += 1
                j += 1
                k += 1
            else:
                print("Vous avez perdu !")
                break
        if c_ord == 27: # ESC
            break

kb.set_normal_term()
