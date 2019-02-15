def factorial(num):

    factorial = 1

    for i in range(1, num+1):
        factorial = factorial * i
        print(factorial, end = " ")

factorial(int(input("nth factorial: ")))