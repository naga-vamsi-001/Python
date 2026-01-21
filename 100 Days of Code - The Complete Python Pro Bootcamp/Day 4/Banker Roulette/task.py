import random

#1st option
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
names = random.choice(friends) #used choice function
print(names)

#2nd option
rand_index = random.randint(0,4)
print(friends[rand_index])


