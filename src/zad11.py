#progam, który pozwala:
#a/ dodawać nowe definicje
#b/ szukać istniejących definicji
#c/ usuwać wybrane

CONST_KEY = "key"
CONST_VALUE = "value"

MSG_ALREADY_EXISTS = "Wartosc #{} juz istnieje, usun ja przed nadpisaniem"
MSG_DELETED_SUCCESSFULLY = "Usunieto #{} pomyslnie"
MSG_NO_KEY_TO_DELETE = "Brak wartosci do usuniecia"
MSG_INVALID_CHOICE = "Niepoprawny wybor"
MSG_ADDED_SUCCESSFULLY = "Dodano pomyslnie"
MSG_GOODBYE = "Do zobaczenia!"
MSG_SUBMIT_KEY = "Podaj klucz: "
MSG_SUBMIT_VALUE = "Podaj wartosc: "

definitions = [{CONST_KEY : "0", CONST_VALUE : "example"}]


print("--------------------------")
print("Definicjomator")
print("--------------------------")


choice = ""

while(not choice == "X"):
    print()
    print("Menu:")
    print("1 - przegladaj")
    print("2 - dodaj")
    print("3 - usun")
    choice = input("Twoj wybor (X: wyjscie): ")
    print()

    if(choice == "X" or choice == "x"):
        print(MSG_GOODBYE)
        break;
    
    elif(choice == "1"):
        print("Aktualne definicje:")
        for definition in definitions:
            print(definition[CONST_KEY], ":", definition[CONST_VALUE])

    elif(choice == "2"):
        exists = False
        key = input(MSG_SUBMIT_KEY)
        
        for definition in definitions:
            if(definition[CONST_KEY] == key):
                print(MSG_ALREADY_EXISTS.format(key))
                exists = True
                
        if( not exists):
            value = input(MSG_SUBMIT_VALUE)
            definitions.append({CONST_KEY : key, CONST_VALUE : value})
            print(MSG_ADDED_SUCCESSFULLY)

            
    elif(choice == "3"):
        deleted = False
        key = input(MSG_SUBMIT_KEY)
        
        for definition in definitions:
            if(definition[CONST_KEY] == key):
                definitions.remove(definition)
                print(MSG_DELETED_SUCCESSFULLY.format(key))
                deleted = True

        if(not deleted):
            print(MSG_NO_KEY_TO_DELETE)

    else:
        print(MSG_INVALID_CHOICE)


        

        
