print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("The ticket is $5.")
    elif age <= 18:
        print("The ticket is $7.")
    else:
        print("The ticket is $12.")
else:
    print("Sorry you have to grow taller before you can ride.")
