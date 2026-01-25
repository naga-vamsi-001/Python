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

game_images = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors\n"))
if user >= 0 and user <=2:
    print(game_images[user])
computer_choice = random.randint(0,2)
print(f"computer chose:")
print(game_images[computer_choice])
if user >= 3 or user<0:
    print("You typed on invalid number. You lose!")
elif user == 0 and computer_choice ==2:
    print("You win!")
elif computer_choice == 0 and user == 2:
    print("You lose!")
elif computer_choice > user:
    print("You lose!")
elif user > computer_choice:
    print("You win!")
elif computer_choice == user:
    print("It's a draw!")