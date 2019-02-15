def allowed_dating_age(my_age):
    girls_age = my_age/2 +7
    return girls_age

x = int(input("Start of range: "))
y = int(input("End of range: ")) + 1

for i in range(x,y):
    print("Dude's age:", i, "Girl's Age", allowed_dating_age(i))