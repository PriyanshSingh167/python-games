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

x = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
arr = [rock , paper , scissors]
y = random.randint(0,2)
print("YOUR CHOICE :-")
print(arr[x])
print("COMPUTER CHOOSE :-")
print(arr[y])
if x>=3 or x<0:
    print("Invalid Choice")
if x==0 and y==0 or x==1 and y==1 or x==2 and y==2:
    print("Match Draw")
if x==0 and y==2 or x==1 and y==0 or x==2 and y==1:
    print("You Win")
if x==0 and y==2 or x==1 and y==2 or x==2 and y==0:
    print("You Lost")

