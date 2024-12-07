name =input("Welcome to this adventure game enter ur name pls :")
print(f"u are welcome {name}")

answer = input("you are on a dirt road,it has come to an end and you can either go left or right pls enter ur choice").lower()

if answer == "right":
    answer = input("you've come near a bridge and its wobbly do you want o cross it or head back? enter (cross or back): ").lower()
    if answer =="back":
        print("!! you went back and lost !!")
    elif answer == "cross":
        answer = input("you crossed the bridg and saw a stranger do you greet or just move on ? Enter(yes OR no): ")
        if answer == "yes":
           print("u ! WON ! cause he gave u Gold")
        elif answer =="no":
            print("u lost caused, u missed the Gold")
        else:
         print(f"invalid option {answer} enter a valid choice")
    else:
         print(f"invalid option {answer} enter a valid choice")

elif answer == "left":
    answer = input("you've come to a river u can swim across it or walk around it enter walk to walk or swim to swim across it: ").lower()
    if answer =="swim":
        print("you swam across and was eaten by an alligator")
    elif answer == "walk":
        print("you walked for many miles,ran out of water and you lost the game!")
    else:
         print(f"invalid option {answer} enter a valid choice")
 
    
else:
    print(f"invalid option {answer} enter a valid choice")