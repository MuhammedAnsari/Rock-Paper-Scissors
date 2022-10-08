from msvcrt import getch
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

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
user = int(input())

if user == 0:
    print(rock)
elif user == 1:
    print(paper)
else:
    print(scissors) 


computer = random.randint(0,2)

print("Computer Choose:")
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)        


if (user == 0 and computer == 1):
    print("You Lose")
elif (user == 1 and computer == 2):
    print("You Lose")
elif (user == 2 and computer == 0):
    print("You Lose")
elif(user == computer):
    print("Drawn")
else:
    print("You Won")
 

getch()