def greet():
    print("Hello")
    print("python")
    print("World")


greet()  #calling a function it will execute the inside code block of function

print("************************")

def greet(Name):       #Name is parameter
    print(f"Hello {Name}")
    print(f"python {Name}")
    print(f"World {Name}")


greet("Toothless")      #Vamsi is argument that will replace Name parameter inside the function.
