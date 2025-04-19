#IMPORTING PET CLASS
import pet as p

#CREATING A PET
#1. GIVING IT A NAME
petName = input("Creating Pet: ")
myPet = p.Pet(petName, 10, 10, 10)

#2. GIVING IT TRICKS
answer = input ("Teach your pet some tricks! Type 'done' when you're finished ")

while True:
    trick = input("Enter a trick: ")
    if trick.lower() == "done":
        break
    myPet.train(trick) 

#PRINTING 
print(" ")
myPet.eat()
myPet.play()
myPet.sleep()
print(" ")
myPet.get_status()
myPet.show_tricks()