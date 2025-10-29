### Die Kindklasse Schlange:
from tier import Tier

class Schlange(Tier):
    num_appendages = 0
    is_cold_blooded = True
    is_mammal = False    
    
    def __init__(self, name: str, sex: int, age: int):
        super().__init__(name, sex, age)

    def general_infos(self):
        print(f"Die Schlange ist {'ein Säugetier' if self.is_mammal else 'kein Säugetier'}, ist {'kaltblütig' if self.is_cold_blooded else 'warmblütig'} und hat {self.num_appendages} Extremitäten.")  

    def individual_infos(self):
        print(f"{self.name} ist {'weiblich' if self.sex == 1 else 'männlich'} und ist {self.age} Jahre alt.") 
        
    def eat(self):
        print(f"{self.name} frisst kleine Nagetiere wie Mäuse und Ratten.")
    
    def sleep(self):
        print(f"{self.name} schläft auf einem Baumast.")

    def grow(self, years):
        print(f"{self.name} wurde {years} Jahre älter und ist jetzt {self.age + years} Jahre alt.")
        self.age = self.age + years

    def crawl(self):
        print(f"{self.name} kriecht durch das Gras.")