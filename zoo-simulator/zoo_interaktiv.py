from tier import Tier
from delfin import Delfin
from elefant import Elefant
from gorilla import Gorilla
from pinguin import Pinguin
from schlange import Schlange
from tiger import Tiger


def choose_animal(choice):
    if choice == "1":
        return show_tiger()
    if choice == "2":
        return show_schlange()
    if choice == "3":
        return show_pinguin()
    if choice == "4":
        return show_gorilla()
    if choice == "5":
        return show_elefant()
    if choice == "6":
        return show_delfin()

def show_tiger():
    tiger1 = Tiger('Rajah', 1, 3)
    tiger2 = Tiger('Sibirien', 1, 5)
    tiger3 = Tiger('Shere Khan', 0, 10)
    print(f"{'='*50}")
    tiger1.general_infos()
    print("\nWir haben drei Exemplare:\n")
    tiger1.individual_infos()
    tiger1.eat()
    tiger2.grow(2)
    tiger2.lick_fur()
    tiger3.individual_infos()
    tiger3.roar()

def show_schlange():
    snake1 = Schlange('Zoro', 0, 11)
    snake2 = Schlange('Nagini', 1, 5)
    print(f"{'='*50}")
    snake1.general_infos()
    print("\nWir haben zwei Exemplare:\n")
    snake1.individual_infos()
    snake2.individual_infos()
    snake1.sleep()
    snake2.crawl() 

def show_pinguin():
    pinguin1 = Pinguin('Flocke', 1, 5)
    pinguin2 = Pinguin('Pingu', 0, 6)
    print(f"{'='*50}")
    pinguin1.general_infos()
    print("\nWir haben zwei Exemplare:\n")
    pinguin1.individual_infos()
    pinguin2.individual_infos()
    pinguin1.dive()
    pinguin2.eat() 

def show_gorilla():
    gorilla1 = Gorilla('Kong', 0, 26)
    gorilla2 = Gorilla('Bobo', 0, 12)
    print(f"{'='*50}")
    gorilla1.general_infos()
    print("\nWir haben zwei Exemplare:\n")
    gorilla1.individual_infos()
    gorilla2.individual_infos()
    gorilla2.climb()
    gorilla1.sleep() 
 
def show_elefant():
    elefant1 = Elefant('Dumbo', 0, 55)
    elefant2 = Elefant('Ella', 1, 30)
    elefant3 = Elefant('Sita', 1, 5)
    print(f"{'='*50}")
    elefant1.general_infos()
    print("\nWir haben drei Exemplare:\n")
    elefant1.individual_infos()
    elefant1.trumpet()
    elefant2.grow(3)
    elefant2.sleep()
    elefant3.individual_infos()
    elefant3.spray_water()

def show_delfin():
    delfin1 = Delfin('Lula', 1, 8)
    delfin2 = Delfin('Finn', 0, 5)
    print(f"{'='*50}")
    delfin1.general_infos()
    print("\nWir haben zwei Exemplare:\n")
    delfin1.individual_infos()
    delfin2.individual_infos()
    delfin2.jump()
    delfin1.eat()

