import random

user_wins = 0
computer_wins = 0
options =["Rock","paper","scissors"]

while True:
    user_input =input("Type Rock / Paper /Scissors or q to quit: ").lower()
    if user_input == "q":
        break

    if user_input  not in options:
        continue
    rand = random.randint(0,2)
    computer_pick =options[rand]
    print(f"computer picked {computer_pick} .")

    if user_input =="rock" and computer_pick == "scissors":
        print("you won!")
        user_wins +=1
    elif user_input =="paper" and computer_pick == "rock":
        print("you won!")
        user_wins +=1
    elif user_input =="scissors" and computer_pick == "paper":
        print("you won!")
        user_wins +=1
    else:
        print("you lost!")
        computer_wins +=1

print(f"you won {user_wins} times")
print(f"computer won {computer_wins} times")
print("Goodbye!")