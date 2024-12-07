import random

rand = input('input the toplevel of the random generator: \n')

if rand.isdigit():
    rand = int(rand)
    if rand <= 0:
        print("Invalid! pls Input A Larger Number!\n")
else:
    print("Invalid Only Nummber Required\n")

random_value = random.randint(0,rand)
TotalNum = 0
while True:
    TotalNum += 1

    guess = input("Determing the next random number : \n")

    if guess.isdigit():
        guess = int(guess)
    else:
        print("Invalid Answer pls Enter a Digit or a Int")
        break
    if guess == rand:
        print("Correct")
        break
    elif guess > rand:
        print("Pls Enter a Smaller Number Next time")
    else:
        print("Pls Enter a Smaller Number Next time")
        

print(f"u got it in {TotalNum} guesses")