class Pet:
    def __init__(self, name, hunger, energy, happiness):
        self.__name = name
        self.__hunger = hunger
        self.__energy = energy
        self.__happiness = happiness
        self.tricks = []

    #AN EAT FUNCTION, TO LET THE PET EAT
    def eat(self):
        self.__hunger = max (0, min(self.__hunger - 3, 10))
        self.__happiness = max (0, min(self.__happiness + 1, 10))
        print(f"{self.__name} is eating...🍔")

    #A SLEEP FUNCTION, TO LET THE PET SLEEP
    def sleep(self):
        self.__energy = max (0, min(self.__energy + 5, 10))
        print(f"{self.__name} is sleeping...💤")
    
    #A PLAY FUNCTION, TO LET THE PET PLAY
    def play(self):
        self.__energy = max (0, min(self.__energy - 2, 10))
        self.happiness = max (0, min(self.__happiness + 2, 10))
        self.__hunger = max (0, min(self.__hunger + 1, 10))
        print(f"{self.__name} is playing...🎾")

    #A FUNCTION TO GET THE PET'S CURRENT CONDITION
    def get_status(self):
        print(f"{self.__name}'s Current Status: ")
        print(f"Hunger: {self.__hunger}")
        print(f"Energy: {self.__energy}")
        print(f"Happiness: {self.__happiness}")

    #A FUNCTION TO KEEP THE PETS STATUS AT A RANGE OF 5-10
    def take_care(self):
        if self.__energy <= 4:
            print(f"{self.__name} is Tired. So:")
            self.sleep()
        if self.__happiness <= 4:
            print(f"{self.__name} is Unhappy. So:")
            for playing in range(1, 4):
                self.play()
                playing += 1
            self.eat()
            self.sleep()
        if self.__hunger <= 4:
            print(f"{self.__name} is Hungry. So:")
            for eating in range(1, 4):
                self.eat()

    #ADDED A PRINT FUNCTION TO PRINT WHATS RIGHT, DEPENDING ON WHAT THE STATUS IS
    def print_Status (self):
        if self.__energy <= 4 or self.__happiness <= 4 or self.__hunger <= 4:
            self.get_status()
            self.show_tricks()
            print(" ")
            self.take_care()
        else: 
            self.get_status()
            self.show_tricks()

    #A TRICK FUNCTION, THAT TEACHES THE PET NEW TRICKS
    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.__name} 🐾 learned a new trick:  {trick}✨ !")
    
    #A FUNCTION TO SHOW THE TRICKS THE PET HAS OBTAINED
    def show_tricks(self):
        print("Tricks:", self.tricks)

