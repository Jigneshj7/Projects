import random
print("Welcome to rock,paper,scissors!!")
user_input=int(input("Enter rock=0,paper=1,scissor=2: "))
reply = random.randint(0,2)
print(f"computer choo0ses {reply}")

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
      
 


  