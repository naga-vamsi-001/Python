# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

print("****************************************")

#Function with Positional Arguments
def greet_with(name,location):
    print(f"My {name}")
    print(f"My {location}")


greet_with("Toothless", "USA")


print("****************************************")
#Key Word Arguments

def greet_with_key_word_agrs(name, location, city):
    print(f"My Name is {name}")
    print(f"My location is {location}")
    print(f"My location is {city}")


greet_with_key_word_agrs(location="USA", city="CA", name="Toothless")
