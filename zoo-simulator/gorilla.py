### Die Kindklasse Gorilla:
from tier import Tier

class Gorilla(Tier):
    num_appendages = 4
    is_cold_blooded = False
    is_mammal = True    
    
    def __init__(self, name: str, sex: int, age: int):
        super().__init__(name, sex, age)

    def general_infos(self):
        print(f"Der Gorilla ist {'ein Säugetier' if self.is_mammal else 'kein Säugetier'}, ist {'kaltblütig' if self.is_cold_blooded else 'warmblütig'} und hat {self.num_appendages} Extremitäten.")  

    def individual_infos(self):
        print(f"{self.name} ist {'weiblich' if self.sex == 1 else 'männlich'} und ist {self.age} Jahre alt.") 
        
    def eat(self):
        print(f"{self.name} frisst Früchte.")
    
    def sleep(self):
        print(f"{self.name} schläft im Nest aus Blättern.")

    def grow(self, years):
        print(f"{self.name} wurde {years} Jahre älter und ist jetzt {self.age + years} Jahre alt.")
        self.age = self.age + years

    def climb(self):
        print(f"{self.name} klettert auf einen Baum.")