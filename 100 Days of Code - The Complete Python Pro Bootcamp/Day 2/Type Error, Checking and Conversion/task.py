#TypeError
# len(1234)

#Type checking
print(type("Hello"))
print(type(123))
print(type(123.45))
print(type(True))
print(type(False))

#Type Conversion
print(int("123") + int("456"))
print(float("123.5") + float("456.2"))



name_of_the_user = input("Enter your name:\n")
length_of_the_name = len(name_of_the_user)
print("Number of letters in your name: " + str(length_of_the_name)) #converting data type from int to str