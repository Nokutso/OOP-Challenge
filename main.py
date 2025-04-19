#IMPORTING PET CLASS
import pet as p
import random

#RANDOMLY ASSIGNING HUNGER, ENERGY AND HAPPINESS LEVELS TO PET
hunger = random.randint(1, 10)
energy = random.randint(1, 10)
happiness = random.randint(1, 10)


#MAKING SURE THE OUTPUT LOOKS NICE ON THE OUTSIDE
print("*******************************************")
print("                My Pet")
print("*******************************************")
print(" ")

#CREATING A PET
#1. GIVING IT A NAME
petName = input("Creating Pet: ")
myPet = p.Pet(petName, hunger, energy, happiness)

#2. GIVING IT TRICKS
print("Teach your pet some tricks! Type 'done' when you're finished ")
print(" ")

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
myPet.take_care()
myPet.get_status()
print(" ")