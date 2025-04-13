 #DAY 4 Project
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


user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors"))

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)

print(user_choice)

choice_list = [rock,paper,scissors]
cpu_rand_choice = random.randint(0,2)

print(choice_list[cpu_rand_choice])

if user_choice == 0 and cpu_rand_choice == 2:
    print("You Won!")
elif user_choice == 2 and cpu_rand_choice == 1:
    print("You Won")
elif user_choice == 1 and cpu_rand_choice == 0:
    print("You Win")
elif user_choice == cpu_rand_choice:
    print("Tie, play again")
else:
    print("Computer Wins")

#Didn't account for user not typing a valid number
