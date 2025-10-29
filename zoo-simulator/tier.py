### Die Basisklasse Tier:

class Tier:

    def __init__(self, name: str, sex: int, age: int):
       self.name = name
       self.sex = sex
       self.age = age

    def show_info(self):
        print("Name des Tiers:", self.name)
        print(f"Geschlecht des Tiers: {'weiblich' if self.sex == 1 else 'männlich'}")
        print("Alter des Tiers:", self.age)

    def eat(self):
        print(f"{self.name} isst.")
    
    def sleep(self):
        print(f"{self.name} schläft.")

    def grow(self, years):
        print(f"{self.name} wurde {years} Jahre älter und ist jetzt {self.age + years} Jahre alt.")
        self.age = self.age + years