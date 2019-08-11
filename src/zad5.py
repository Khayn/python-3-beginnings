totalSum = 0

maxCount = 3
iterator = 0

while(iterator < maxCount):
    num = int(input("Podaj parzysta liczbe dodatnia ({}): ".format(iterator+1)))

    if not(num % 2 == 0 and num > 0):
        print("Podana liczba nie spelnia kryteriow, sprobuj ponownie.")
        continue

    else:
        iterator += 1
        totalSum += num


print("Suma:",totalSum)


