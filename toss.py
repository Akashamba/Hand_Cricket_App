from random import randint


def binary(t):
    if t == "odd":
        return 1
    elif t == "even":
        return 0
    else:
        exit()


def oddoreven(x):
    if x % 2 != 0:
        return 1
    return 0


toss = input("Odd or Even: ")
toss = binary(toss)

man = int(input("Enter Number: "))
mach = randint(1, 6)
total = mach + man
print(mach)

if toss == oddoreven(total):
    print("You have won the toss")
else:
    print("You have lost the toss")
