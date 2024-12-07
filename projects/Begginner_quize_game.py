print("welcome to the Beginner quize game code")

answer = input(' do you want to play ')
score = 0
# print((2/4)*100)
if answer.lower() != 'yes':
    quit()

answer = input('what does ram stand for ? ')
if answer.lower() != 'random access memory':
    print("incorrect".capitalize())
else:
    print('correct'.capitalize())
    score +=1

answer = input('what does cpu stand for ? ')
if answer.lower() != 'central processing unit':
    print("incorrect".capitalize())
else:
    print('correct'.capitalize())
    score +=1

answer = input('what does psu stand for ? ')
if answer.lower() != 'power supply unit':
    print("incorrect".capitalize())
else:
    print('correct'.capitalize())
    score +=1

answer = input('what does Gpu stand for ? ')
if answer.lower() != 'graphic processing unit':
    print("incorrect".capitalize())
else:
    print('correct'.capitalize())
    score +=1

print('ur total score is '.capitalize()+ str(score))
print('ur total average score is '.capitalize()+ str((score /4)*100)+'%')