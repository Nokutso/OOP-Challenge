class Pet:
    def __init__(self, name, hunger, energy, happiness):
        self.__name = name
        self.__hunger = hunger
        self.__energy = energy
        self.__happiness = happiness
        self.tricks = []

    def eat(self):
        self.__hunger = max (0, min(self.__hunger - 3, 10))
        self.__happiness = max (0, min(self.__happiness + 1, 10))
        print(f"{self.__name} is eating...🍔")

    def sleep(self):
        self.__energy = max (0, min(self.__energy + 5, 10))
        print(f"{self.__name} is playing...💤")
        
    def play(self):
        self.__energy = max (0, min(self.__energy - 2, 10))
        self.happiness = max (0, min(self.__happiness + 2, 10))
        self.__hunger = max (0, min(self.__hunger + 1, 10))
        print(f"{self.__name} is sleeping...🎏")

    def get_status(self):
        print(f"{self.__name}'s Current Status: ")
        print(f"Hunger: {self.__hunger}")
        print(f"Energy: {self.__energy}")
        print(f"Happiness: {self.__happiness}")
    
    def train(self, trick):
        self.tricks.append(trick)
        
    def show_tricks(self):
        print("Tricks:", self.tricks)

