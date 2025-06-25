import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#option 1
index_number = random.randint(0,len(friends)-1)
print(index_number)
pays_the_bill = friends[index_number]
print(pays_the_bill)

#option 2
print(random.choice(friends))