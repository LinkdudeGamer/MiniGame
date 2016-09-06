# Created by Nicholas Dominici at Very Good Softworks

# Imports delays
def wait_minute():
    import time
    time.sleep(60)

def wait_thirty():
    import time
    time.sleep(30)

def wait_five():
    import time
    time.sleep(5)

def wait_two():
    import time
    time.sleep(2)

# Imports press a key functionality on windows
import msvcrt as m
def wait():
    m.getch()

def scene0():  # Start of Game

    print("Welcome Citizen!  My name is J'Basa.")

    myname = input("What is your name?>>")
    age = input("How old are you?>>")
    gender = input("Are you a Male or a Female?>>")

    print("J'Basa: It's very nice to meet you, %s!  As I just told you my name is J'basa. Right now you are using a simple \
program made in Python.  I know that you are %s years old and a %s." % (myname, age, gender))

    print("Press a key to continue...")
    wait()
    citytour = input("J'Basa: Would you like to take a tour of the city?>>")

    if citytour == "yes":
        print("Ok then!  Just hop right in the car.")

    elif citytour == "no":
        print("OK then...")
        wait_five()
        print("*J'Basa pulls out a gun and shoots you in the head*")
        wait_two()
        print("GAME OVER")
        print
        print
        import gameover.py

    else:
        print("Unknown command")
        print
        print(citytour)

scene0()



