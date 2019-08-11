print("------------------")
print("KALKULATOR")
print("------------------")

print()
print("Menu: ")
print("* - mnozenie")
print("/ - dzielenie")
print("+ - dodawanie")
print("- - odejmowanie")
print("^ - potegowanie")
print("% - modulo")

choice = input("Twoj wybor: ")
print()
first = int(input("Pierwsza wartosc: "))
second = int(input("Druga wartosc: "))
print()

wynik = 0
validInput = False

if(choice == "*"):
    validInput = True
    wynik = first*second

elif(choice == "/"):
    if(second == 0):
        print("Dzielenie przez 0 nie jest mozliwe")
    else:
        validInput = True
        wynik = first/second

elif(choice == "+"):
    validInput = True
    wynik = first+second

elif(choice == "-"):
    validInput = True
    wynik = first - second

elif(choice == "^"):
    validInput = True
    wynik = first ** second

elif(choice == "%"):
    validInput = True
    wynik = first % second


    
else:
    print("Nieznany wybor {} - sprobuj ponownie".format(choice))


if(validInput):
    print("Wynik dzialania: ", wynik)
