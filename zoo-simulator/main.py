import zoo_interaktiv as zoo

def main():

    print(f"{'='*50}\n{'Willkommen im Zoo!':^50}\n{'='*50}")
    print("Zurzeit haben wir 6 verschiedene Tierarten\n")
    
    while True:

        wahl = input(f"Welches Tier möchtest du dir ansehen?\nWähle eine Option:\n1. Tiger \n2. Schlange \n3. Pinguin \n4. Gorilla \n5. Elefant \n6. Delfin \n7. Zoo verlassen ")
        if wahl == "7":
            print(f"{'='*50}\nDanke für deinen Besuch!")
            break
        else:
            zoo.choose_animal(wahl)
            print(f"{'='*50}")
            
main()
    
   
