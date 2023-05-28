import random

options = ["rock","paper","scissors"]
winPerson = 0
winComputer = 0

while True:
    inputPerson = input("Choose from Rock/Paper/Scissors or Press Q to quit: ").lower()
    
    if inputPerson == 'q':
        break
    
    if inputPerson not in options:
        print(" Invalid option")
        continue
    
        #rock:0, paper:1, scissors:2
    Random_Num = random.randint(0,2)
    Computer_Rand = options[Random_Num]
    print("Computer choose:",Computer_Rand)
    
    
    if inputPerson=="rock" and Computer_Rand=="scissors":
        print("You won!")
        winPerson+=1
        
    elif inputPerson=="paper" and Computer_Rand=="rock":
        print("You won!")
        winPerson+=1
        
    elif inputPerson=="scissors" and Computer_Rand=="paper":
        print("You won!")
        winPerson+=1
        
    elif inputPerson==Computer_Rand:
        print("Tie!")
        
    else:
        print("You Lost!")
        winComputer+=1
        
print("Your score:",winPerson,"wins")
print("Computer's score:",winComputer,"wins")
print("Enjoy your day.")
        
        
            