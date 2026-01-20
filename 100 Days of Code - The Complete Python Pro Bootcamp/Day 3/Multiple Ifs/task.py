print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
        Ticket = 5
    elif age <= 18:
        print("Please pay $7.")
        Ticket = 7
    else:
        print("Please pay $12.")
        Ticket = 12
    photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
    if photo == "y":
        Ticket += 3

    print(f"Total bill is {Ticket}")
else:
    print("Sorry you have to grow taller before you can ride.")
