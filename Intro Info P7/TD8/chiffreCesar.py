# Chiffre de César
# A = alphabet+3 -> A = D
# ASCII Table : A = 65, Z = 90

def messageToCode():
    answer = str(input("Veuillez entrer un texte à coder: "))
    answer = answer.upper()

    l = [(ord(c) + 3) for c in answer]
    for idx, num in enumerate(l):
        if num == 91:
            l[idx] = 65
        if num == 92:
            l[idx] = 66
        if num == 93:
            l[idx] = 67
        if num == 35:
            l[idx] = 32
    convertedList = [chr(c) for c in l]
    joinedList = ''.join(str(i) for i in convertedList)
    print(joinedList)

def messageToDecode():
    answer = str(input("Veuillez entrer un texte à décoder: "))
    answer = answer.upper()

    l = [(ord(c) - 3) for c in answer]
    for idx, num in enumerate(l):
        if num == 62:
            l[idx] = 88
        if num == 63:
            l[idx] = 89
        if num == 64:
            l[idx] = 90
        if num == 29:
            l[idx] = 32
    convertedList = [chr(c) for c in l]
    joinedList = ''.join(str(i) for i in convertedList)
    print(joinedList)

userChoice = input("Voulez-vous coder un texte ou décoder un texte ?\nVeuillez entrer C pour coder et D pour décoder: ")
if userChoice.upper() == "C":
    messageToCode()
elif userChoice.upper() == "D":
    messageToDecode()
else:
    print("Tant pis...")
