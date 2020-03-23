import time

game = "----------"
l = list(game)
player = "1"

l.insert(0, player)
print(''.join(l))

i = 0
j = 1

while len(game[i]) != -1:
    time.sleep(1)
    l[i], l[j] = l[j], l[i]
    print(''.join(l))
    i += 1
    j += 1
