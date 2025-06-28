try:
    age = int(input("How old are you?"))
    if age >= 18:
        print(f"You can drive at age {age}.")
except TypeError:
    print("You must enter an int")