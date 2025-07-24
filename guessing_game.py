import random

first_name = input("Enter your name: ")
last_name = input("Enter your last name: ")

print(f"Welcome, glad to see you, {first_name} {last_name}")

def game():
    while True:
        a = int(input("Enter a number from 1 to 10"))
        x = random.randint(1, 10)
        print(f"Okay, you entered {a}, lets see if you were right...")
        if  0 != a < 10:
            if a == x:
                print(f"Good job guessing! You're right, it was {x}")
            else:
                print(f"Hmm, it seems to be wrong, It was actually {x}")
        else:
            print(f"{a} seems to be a wrong number")
        again = input("Wanna play once again?: ")
        if again.lower() not in ['yes', 'sure', "let's go"]:
            print(f'Good bye, {first_name}!')
            break
    
    
play = input(f"Want to play some games, {first_name}?")

if play.lower() == 'yes':
    game()
else:
    print(f"Okay, see you later, {first_name} {last_name}!")


