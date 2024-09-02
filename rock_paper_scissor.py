#import random function
import random
#printing welcome message and asking for user input
print("Welcome to rock,paper,scissors!!")
user_input=int(input("Enter rock=0,paper=1,scissor=2: "))
#using *randint function from random 
reply = random.randint(0,2)
#printing randint value
print(f"computer chooses {reply}")

#checking conditions with if/elif/else and printing final result
if reply == user_input:
    print("DRAW.PLAY AGIAN!")
elif user_input == 0 and reply == 1:
    print("You lose!")
elif user_input == 1 and reply == 2:
    print("You lose!")
elif user_input == 2 and reply == 0:
    print("You lose!")
else:
    print("You Win!")         
      
 


  