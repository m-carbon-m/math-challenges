### Die Kindklasse Elefant:
from tier import Tier

class Elefant(Tier):
    num_appendages = 4
    is_cold_blooded = False
    is_mammal = True    
    
    def __init__(self, name: str, sex: int, age: int):
        super().__init__(name, sex, age)

    def general_infos(self):
        print(f"Der Elefant ist {'ein Säugetier' if self.is_mammal else 'kein Säugetier'}, ist {'kaltblütig' if self.is_cold_blooded else 'warmblütig'} und hat {self.num_appendages} Extremitäten.")  

    def individual_infos(self):
        print(f"{self.name} ist {'weiblich' if self.sex == 1 else 'männlich'} und ist {self.age} Jahre alt.") 

    def eat(self):
        print(f"{self.name} frisst Gras.")
    
    def sleep(self):
        print(f"{self.name} schläft unter einem Baum.")

    def grow(self, years):
        print(f"{self.name} wurde {years} Jahre älter und ist jetzt {self.age + years} Jahre alt.")
        self.age = self.age + years

    def trumpet(self):
        print(f"{self.name} trötet laut.")

    def spray_water(self):
        print(f"{self.name} spritzt mit seinem Rüssel Wasser.")


        