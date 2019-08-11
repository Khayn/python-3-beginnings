#zagnieżdżenia

guests = [
    ["Andrew", "Hopkins", 22],
    ["Kerry", "Johnson", 25],
    ["John", "Pierce", 43]
]

print("all:\n", guests)
print("first:\n", guests[1])
guests[1][2] = 26
print("after got older:", guests[1][2])

guests.append(["Albert", "Wesker", 42])
print("Wesker arrived:\n", guests)
print()

for name, surename, age in guests:
    print("name: \t\t", name)
    print("surename: \t", surename)
    print("age: \t\t", age)
    print()


print()
#można krotki i dodatkowe cechy set

tuples = {
    ("Volvo", 1972),
    ("Skoda", 1981)
    }

other = {
    ("Volvo", 1974),
    ("Fiat", 1995)
    }

print("intersection:\n", tuples & other)
print("sum:\n", tuples | other)


