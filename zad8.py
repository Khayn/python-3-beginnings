#krotka - tuple, niemutowalna tablica bez narzuconego typu
print("\n--------------------------\n tuple")
myTuple = (1, 2, 43, 5, "car")

print(myTuple)
print(myTuple[1])
print()

#-------------------
#dictionary - mapa
print("\n--------------------------\n dictionary")
cars = {1 : "BMW", 2 : "Audi", 3 : "Skoda", 1 : "Volkswagen" }
print(cars)
cars[1] = "Renault"
cars.update({5 : "Volvo"})
del(cars[1])
#lub cars.pop[1] - przy okazji zwraca
print(cars)
print(len(cars))
cars.clear()

#-------------------
#set
print("\n--------------------------\n set")
numbers = {20, -1, 20, 5, 4, -3}
print(numbers)

numList = [2, 5, 3, 2, 1]
print("List with duplicates:", numList)
print("List coverted to set:", set(numList))

print("set intersection:",{1,2,3,4} & {3,2,6})
print("set sum:",{1,2,3,4} | {3,2,6})
print("set diff:",{1,2,3,4} - {3,2,6})
print("set xor:", {1,2,3,4} ^ {3,2,6}) #elementy, które nie są wspólne

numbers.discard(1)
# w przeciwieństwie do discard nie rzuca wyjątku gdy element nie istnieje

print("podzbiory:", {1,2,3,4}.issubset({1,2,3,4,5,6}))
