#wyciąganie wartości z zagnieżdżonej struktury

print("same slowniki")
people = [
    {"id" : "1", "name" : "John", "surename" : "Wayne", "age" : 32, "sex" : "male" },
    {"id" : "2", "name" : "Leah", "surename" : "Babe", "age" : 25, "sex" : "female" },
    {"id" : "3", "name" : "Vivi", "surename" : "Black", "age" : 16, "sex" : "yes, please" }
    ]


for dude in people:
    for key in dude:
        
        if(key == "id"):
            print("[{} #{}]:".format(key, dude[key]))
        else:
            print(key, ":", dude[key])

    print()

print("\n\n")  


print("slownik w slowniku")
people = {
    1 : {"name" : "John", "surename" : "Wayne", "age" : 32, "sex" : "male" },
    2 : {"name" : "Leah", "surename" : "Babe", "age" : 25, "sex" : "female" },
    3 : {"name" : "Vivi", "surename" : "Black", "age" : 16, "sex" : "female" }
    }

for identifier, dictionary in people.items():
    print("[id #{}]".format(identifier))

    for key in dictionary:
        print(key, ":", dictionary[key])

    print()

    
print("\n\n")


print("krotki ze zbiorami")
people = [
    (1, {"name" : "John", "surename" : "Wayne", "age" : 32, "sex" : "male" }),
    (2, {"name" : "Leah", "surename" : "Babe", "age" : 25, "sex" : "female" }),
    (3, {"name" : "Vivi", "surename" : "Black", "age" : 16, "sex" : "female" })
    ]

for row in people:

    print("[id #{}]:".format(row[0]))
    for key in row[1]:
        print(key, ":", row[1][key])

    print()


print("\n\n")


