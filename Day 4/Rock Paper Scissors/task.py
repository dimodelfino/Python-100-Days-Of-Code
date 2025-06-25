import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
options_str = ["rock", "paper", "scissors"]
go_again = ""

while go_again != "no":
    selection = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors. \n"))

    if 0 <= selection <= 2:
        print(f"you chose {options_str[selection]} \n {options[selection]}")
        computer = random.randint(0, 2)
        print(f"Computer chose: {options_str[computer]} \n {options[computer]} \n")

        if selection == 0 and computer == 2:
            print("You win!")
        elif computer == 0 and selection == 2:
            print("You lose!")
        elif selection < computer:
            print("You lose!")
        elif selection > computer:
            print("You win!")
        elif selection == computer:
            print("It's a tie!")
    else:
        print("You have to choose a number between 0 and 2!")

    go_again = input("Go again? \n")