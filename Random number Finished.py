import random

print ("Number Guesser")
print ("Try to guess the chosen number from 0-100")
print ("---------------------------------------")
print ()

my_number = random.randrange(0, 100)

z = 0

done = False
while not done:

 answer = int(input ("Enter a number: "))

 y = answer

 x = my_number
    
 if x < y:
     z = z + 1
     print ("/Guess is too high/")
     print ()
    
 elif x > y:
     z = z + 1
     print ("/Guess is too low/")
     print ()
     
 elif x == y:
     print ()
     print ("You identified the number!")
     done = True
     
print ("//You Win Congrats!//")
print ("You got the answer in", z, "attempts")