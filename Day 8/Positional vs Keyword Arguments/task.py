# Functions with input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")


def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")

# Positional Arguments
greet_with('James', 'London')

# Keyord Arguments
greet_with(location='London', name= 'James')

