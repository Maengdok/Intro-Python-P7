def bubble_sorting(tab):
    n = len(tab)
    for i in range(n):
        for j in range(0, n-i-1): #n-i-1 sert à réduire la range de la loop à chaque fois qu'on fait un passage.
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j] #Swap tab[j] et tab[j+1] si tab[j] est plus grand que tab[j+1]
                print("{} #on échange {} et {}".format(tab, tab[j], tab[j+1]))
            else:
                print("{} #on n'échange pas {} et {}".format(tab, tab[j], tab[j+1]))

tab = [54, 25, 107, 12, 15, 34, 25, 68]

bubble_sorting(tab)
