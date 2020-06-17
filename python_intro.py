def hi():
    print("Hello")
    print("How are you?")

def hiv2(name):
    print("Hello " + name)

def area(side):
    return side * side

print("Hello World")
if 1 > 2:
    print("Yes")
    hi()

else:
    print("Wrong")
    hiv2("Becky")
    small_square = area(2)
    big_square = area(small_square)
    print(big_square)

girls = ["Rachel", "Lucy", "Jessica"]

for name in girls:
    hiv2(name)

person = {
    "Name": "Ola",
    "Height": 155,
    "Favourite_language": "Python",
}

for element in person.values():
    print(element)

for element in person.items():
    print(element)

for key, value in person.items():
    print("Person's " + str(key) + " is " + str(value))

for number in range(1,11):
    print(number)
#this is a comment
