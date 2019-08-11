secretNumber = 231


print("--------------------")
print("Biedanator 3000")
print("--------------------")

guessed = secretNumber+1; #aby nie wstrzelic sie za pierwszym razem
numOfTries = 0

while True:
    guessed = int(input("Podaj liczbe: "));
    numOfTries += 1

    if (guessed == secretNumber):
        print("BRAWO! Udalo Ci sie za", numOfTries, "podejsciem!")
        break

    elif (guessed > secretNumber):
        print("Za duzo...")

    else:
        print("Za malo...")

    print()
