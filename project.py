#................................game project.......................#
import random
target=random.randint(1,100)
while True:
    userChoice = int(input("guess the target or Quit(Q):"))
    if(userChoice == "Q"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("success : correct Guess!")
        break
    elif (userChoice<target):
        print("your number was too small. Take a bigges guess.....")
    else:
        print("your number was too big. Take a smaller guess.....") 
        
        print("--------GAME OVER---------")