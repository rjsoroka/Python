# Currently broken, fix when get better
# http://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html
# https://www.reddit.com/r/dailyprogrammer/comments/17f3y2/012813_challenge_119_easy_change_calculator/

def change():
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    
    given = int(input("How much cash was given? "))
    price = int(input("How much did the item cost? "))
    change = given - price #int obj is not iterable?

   # change = "Change: " + str(given - price) + "\n"
   # print change

    for x in change:
        if x % 4 != 0.0:
            quarters += 1
        elif x % 10 != 0.0:
            dimes += 1
        elif x % 20 != 0:
            nickels += 1
        elif x % 100 != 0:
            pennies += 1
        else:
            print ("no change")
    return change
    print(quarters, dimes, nickels, pennies)

change()
