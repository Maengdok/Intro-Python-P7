# IMC = masse / taille²

weight = int(input("Veuillez entrer votre poids: "))
height = int(input("Veuillez entrer votre taille: "))
imc = weight / (height ** 2)
imc = imc * 10000 # exemple: 0.002469 -> 24.69

print("Votre IMC est de: {}".format(round(imc, 2))) # round(number, ndigits) permet d'arrondir le nombre de chiffres après la virgule
