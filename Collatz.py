def collatz(n):
    counter = 0
    while n != 1:
        if n % 2 is 0:
            n = n / 2
            counter += 1
        else:
            n = 3 * n + 1
            counter += 1
    return counter

n = int(input("Give me a number: "))
print "Steps taken: ", collatz(n), "\n"