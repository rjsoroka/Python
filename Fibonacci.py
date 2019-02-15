def fibo(n):
    lst = [1,1]

    if n <= 1:
        return 1
    else:
        for n in range(1, n-1):             #n = 10 > 1 ... 9
            lst.append(lst[-1]+lst[-2])
    return lst

print(fibo(int(input("Give me a #: "))))

# 1, 1, 2, 3, 5, 8, 13, 21
# 1, 2, 3, 4, 5, 6, 7