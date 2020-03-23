import random as rand

nTry = 6
randnum = rand.randrange(0, 100)

while nTry > 0:
    answer = int(input("Essayez de deviner le chiffre aléatoire: "))
    if answer < randnum:
        print("Votre réponse est inférieure au chiffre à découvrir!")
        nTry -= 1
        print("Il vous reste: {} essai(s)".format(nTry))
    elif answer > randnum:
        print("Votre réponse est supérieure au chiffre à découvrir!")
        nTry -= 1
        print("Il vous reste: {} essai(s)".format(nTry))
    elif answer == randnum:
        print("Bravo vous avez trouvé le chiffre!\n{}".format(randnum))
        break

if nTry == 0:
    print("Vous n'avez plus d'essai...\nLe chiffre à trouver était: {}".format(randnum))
