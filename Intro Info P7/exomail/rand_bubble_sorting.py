import random
import time
def bubble_sorting(tab):
    n = len(tab)
    for i in range(n):
        for j in range(0, n-i-1): #n-i-1 sert à réduire la range de la loop à chaque fois qu'on fait un passage.
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j] #Swap tab[j] et tab[j+1] si tab[j] est plus grand que tab[j+1]

tabSize = int(input("How many random integers to you want ? "))
rndInt = random.randint(0, 1000)
tab = []

for elem in range(tabSize):
    rndInt = random.randint(0, 1000)
    tab.append(rndInt)


print("initial tab =\n{}\n".format(tab))
t = time.process_time_ns()
bubble_sorting(tab)
countTime = (time.process_time_ns() - t) / (10**6)

t2 = time.process_time_ns()
tab.sort()
countTime2 = (time.process_time_ns() - t) / (10**6)

print("sorted tab =\n{}\nin {} ms".format(tab, countTime))
print("sort() function sorted in {}".format(countTime2))
