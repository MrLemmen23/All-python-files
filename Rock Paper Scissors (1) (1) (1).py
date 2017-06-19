import random

a = 0
b = 0

print ("Welcome to Rock, Paper, Scissors!")
print ("First to 3 Wins!")
print ("---------------------------------")

done = False
while not done:
    
    x = 0
    y = 0
    
    answer = input ("Enter either (rock,paper,scissors): ")
    
    if answer.lower() == "rock":
        x = x+0
    
    elif answer.lower() == "paper":
        x = x+1
        
    elif answer.lower() == "scissors":
        x = x+2
        
    else:
        x = x+5
        
    my_list = ["rock", "paper", "scissors"]
    random_index = random.randrange(3)
    print(my_list[random_index])
    
    #print (x)
    
    y = (random_index)
    
    #print (y)
    
    if x == y:
        print ("//It's a Tie!//")
        
    elif answer == "rock":
        if random_index == 2:
            print ("//Player wins!//")
            a = a + 1
            
    elif answer == "paper":
        if random_index == 0:
            print ("//Player wins!//")
            a = a + 1
            
    elif answer == "scissors":
        if random_index == 1:
            print ("//Player wins!//")
            a = a + 1
            
    if answer == "rock":
        if random_index == 1:
            print ("//A.i wins!//")
            b = b + 1
                
    elif answer == "paper":
        if random_index == 2:
            print ("//A.i wins!//")
            b = b + 1
                
    elif answer == "scissors":
        if random_index == 0:
            print ("//A.i wins!//")
            b = b + 1
            
    print (a)
    print (b)
    print ()
    
    if a == 3:
        print ("Player has reached 3 wins")
        done = True
        
    if b == 3:
        print ("A.i has reached 3 wins")
        done = True
        
print ()
print ("You have completed the game!")
print ("Thanks For Playing!")