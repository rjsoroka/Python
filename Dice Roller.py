
import random

def roller(rolls, sides):
    rand_nums = []
    freq = [0] * sides
    sidelst = range(1, sides+1)

    for x in range(rolls):
        x = random.randint(1, sides)
        rand_nums.append(x)

    for elem in rand_nums:
        freq[elem-1] = rand_nums.count(elem)

    i = 0
    while i != sides:
        print(str(sidelst[i]) + ": " + str(freq[i]))
        i += 1    

roller((int(input("# of rolls: "))) ,(int(input("# of sides: "))))