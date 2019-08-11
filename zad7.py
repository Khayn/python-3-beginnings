#listy
names = ["Andrew", "Vicky", "Leah"]
numbers = [1, 43, -2]
multiType = [1, "aaa", -2]


print(names)
print()

for num in numbers:
    print(num)

print()
print(numbers[1])
print("Numbers times two:", 2* numbers)

print()
for var in multiType:
    print(type(var), var)

print()
print("Andrew in names:", "Andrew" in names)
print("John in names:", "John" in names)

print()
print("Names' length:", len(names))
names.append("Harry")
names.extend(["Chloe", "Becky"])
names.insert(1, "Claude")
print("Names after append, extend and insert: \n", names)
print("Harry's index:", names.index("Harry"))
names.sort()
names.sort(reverse=True)
print("Names after sorting: \n", names)

print("Leah's count:", names.count("Leah"))

print()
numbers.append([2, 3])
print(numbers) #dodaje JEDEN element bedacy lista!
