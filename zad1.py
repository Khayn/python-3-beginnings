print("-------------------------")
name = input("Name: ")
age = input("Age: ")

print("Hello {}, age of {}.".format(name.capitalize(),age))
print("You will be",(int(age)+1),"in a year's time. Did you know that?") 

sex = "";
if(name[-1] == "a"):
    sex = "girl"
else:
    sex = "boy"

print("Congratulations! You're a {}!".format(sex))

goodbyeText="""I'm so happy for you!
Take care,"""

print(goodbyeText,name.capitalize())
