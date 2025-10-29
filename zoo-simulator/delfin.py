### Die Kindklasse Delfin:
from tier import Tier

class Delfin(Tier):
    num_appendages = 4
    is_cold_blooded = False
    is_mammal = True    
    
    def __init__(self, name: str, sex: int, age: int):
        super().__init__(name, sex, age)

    def general_infos(self):
        print(f"Der Delfin ist {'ein Säugetier' if self.is_mammal else 'kein Säugetier'}, ist {'kaltblütig' if self.is_cold_blooded else 'warmblütig'} und hat {self.num_appendages} Extremitäten: zwei Brustflossen, eine Rückenflosse und eine Schwanzflosse.")  

    def individual_infos(self):
        print(f"{self.name} ist {'weiblich' if self.sex == 1 else 'männlich'} und ist {self.age} Jahre alt.") 
        
    def eat(self):
        print(f"{self.name} frisst Fisch.")
    
    def sleep(self):
        print(f"{self.name} schläft im Wasser des Aquariums.")

    def grow(self, years):
        self.age += years
        print(f"{self.name} wurde {years} Jahre älter und ist jetzt {self.age} Jahre alt.")

    def jump(self):
        print(f"{self.name} springt aus dem Wasser.")
