import random
# import my_module own module created

a = random.randint(1,10) #print from range of 0 to 9
print(a)

#float
# b = my_module.my_favourite_number
# print(b)


# rand_num_0_to_1 = random.random()
# print(rand_num_0_to_1)

# using random module able to print Heads(Even) and Tails(Odd)
a = random.randint(1,10)
if a%2 == 0:
    print("Heads")
else:
    print("Tails")