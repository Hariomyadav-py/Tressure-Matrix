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
human_responce = int(input("What so you chose? 0 for Rock , 1 for paper , 2 for Scissors :-\n"))
list_inputs = [rock,paper,scissors]
print(list_inputs[human_responce])
print("Computer Chose:-")
comp_responce = random.randint(0,2)
print(list_inputs[comp_responce])
if human_responce == comp_responce:
    print("Its a tie")
elif human_responce == 0 and comp_responce == 2:
    print("you won")
elif human_responce == 0 and comp_responce == 1:
    print("you lost")
elif human_responce == 1 and comp_responce == 0:
    print("you won")
elif human_responce == 1 and comp_responce == 2:
    print("you lost")
elif human_responce == 2 and comp_responce == 0:
    print("you lost")
elif human_responce == 2 and comp_responce == 1:
    print("you won")

