import random

random_int = random.randint(1,100)
print(random_int)

random_number_0_1 = random.random() * 10
print(random_number_0_1)

random_float = random.uniform(1,100)
print(random_float)

random_0_1 = random.randint(0,1)
print(random_0_1)

if(random_0_1 == 1):
    print("Heads")
else:
    print("Tails")