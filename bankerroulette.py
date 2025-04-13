import random

person_paying = random.randint(0,4)

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#Option 1
#print(person_paying)

#if person_paying == 0:
    #print(friends[0])
#elif person_paying == 1:
    #print(friends[1])
#elif person_paying == 2:
    #print(friends[2])
#elif person_paying == 3:
    #print(friends[3])
#else:
    #print(friends[4])

#Option 2
#random_index = random.randint(0, 4)
#print(friends[random_index])

#Option 3
#print(random.choice(friends))