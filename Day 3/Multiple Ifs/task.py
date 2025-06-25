print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("cost is $5.")
        bill = 5
    elif age <= 18:
        print("cost is $7.")
        bill = 7
    else:
        print("cost is $12.")
        bill = 12

    add_photo = input("Would you like to add a photo? ")
    if add_photo == "yes":
        print("That would be $3 extra")
        bill += 3

    print(f"Your total bill is ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
