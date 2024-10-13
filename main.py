from zelva import *

def menu():
    while True: 
        try:
            moznost = input('''
            Vyber moznost:
[1] - Barevne Slunce
[2] - Spirala
[3] - Hvezdy
[4] - Vrtule
[0] - Konec

''')
            if moznost == '1':
                print("Barevne Slunce: ")
                barevne_slunce()
            elif moznost == '2':
                print("Spirala: ")
                spirala()
            elif moznost == '3':
                print("Hvezdy: ")
                hvezdy()
            elif moznost == '4':
                print("Vrtule: ")
                vrtule()
            elif moznost == '0':
                print("Program se vypl.")
                break 
            else:
                print('Neplatná volba, zkus to znovu.')
        except Exception :
            print(f"Nastala chyba.")

menu()
