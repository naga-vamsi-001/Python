#IndexError
fruits = ["Cherry", "Apple", "Pear"]
# print(fruits[3]) #This will be an IndexError
print(fruits[2])

#Nested Lists
fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinach"]
fruits_and_veg = [fruits, veg]
print(fruits_and_veg) #Nested List
print(fruits_and_veg[0][1]) #where we are getting Apple