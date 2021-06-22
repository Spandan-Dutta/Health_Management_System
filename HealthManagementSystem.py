# Health Management System
"""
So basically we have three clients - Spandan , Divyansh and Shravan. We have
to make 3 files for loging their food_diet and 3 files for loging their 
daily exercises. Total 6 files 

Pre-created function :
def getdate():
    import datetime
    return datetime.datetime.now()

One more function to retrieve exercise or food_diet for any client.
"""

# Function for date and time
import datetime
def getdate():
    return datetime.datetime.now()


# Function for logging data:
def log(k):
    if k == "Spandan":
        work = input("You want to access the data of food or exercises: ")
        if work == "food":
            data = input("Type here: ")
            with open("spandan_food.txt" , "a") as f:
                f.write(str([str(getdate())]) + " : " + data + "\n")
                print("Inputted Successfully")
        elif work == "exercises":
            data = input("Type here: ")
            with open("spandan_exercise.txt" , "a") as f:
                f.write(str([str(getdate())]) + " : " + data + "\n")
                print("Inputted Successfully")

    elif k == "Divyansh":
        work = input("You want to access the data of food or exercises: ")
        if work == "food":
            data = input("Type here: ")
            with open("Divyansh_food.txt" , "a") as f:
                f.write(str([str(getdate())]) + " : " + data + "\n")
                print("Inputted Successfully")
        elif work == "exercises":
            data = input("Type here: ")
            with open("Divyansh_exercise.txt" , "a") as f:
                f.write(str([str(getdate())]) + " : " + data + "\n")
                print("Inputted Successfully")

    elif k == "Shravan":
        work = input("You want to access the data of food or exercises: ")
        if work == "food":
            data = input("Type here: ")
            with open("shravan_food.txt" , "a") as f:
                f.write(str([str(getdate())]) + " : " + data + "\n")
                print("Inputted Successfully")
        elif work == "exercises":
            data = input("Type here: ")
            with open("shravan_exercise.txt" , "a") as f:
                f.write(str([str(getdate())]) + " : " + data + "\n")
                print("Inputted Successfully")

    else:
        print("Enter a valid input...Note: Clients are Spandan, Divyansh and Shravan")

# Function of Retrieving    
def retrieve(k):
    if k == "Spandan":
        work = input("You want to access the data of food or exercises: ")
        if work == "food":
            with open("spandan_food.txt" , "r") as f:
                for line in f:
                    print(line , end="")
        elif work == "exercises":
            with open("spandan_exercise.txt" , "r") as f:
                for line in f:
                    print(line , end="")

    elif k == "Divyansh":
        work = input("You want to access the data of food or exercises: ")
        if work == "food":
            with open("Divyansh_food.txt" , "r") as f:
                for line in f:
                    print(line , end="")
        elif work == "exercises":
            with open("Divyansh_exercise.txt" , "r") as f:
                for line in f:
                    print(line , end="")

    elif k == "Shravan":
        work = input("You want to access the data of food or exercises: ")
        if work == "food":
            with open("shravan_food.txt" , "r") as f:
                for line in f:
                    print(line , end="")
        elif work == "exercises":
            with open("shravan_exercise.txt" , "r") as f:
                for line in f:
                    print(line , end="")
    
    else:
        print("Enter a valid input...Note: Clients are Spandan, Divyansh and Shravan")



# Code for User to input
print("Welcome to my Health Management System")
print("Our Clients: Spandan , Divyansh , Shravan")
name = input("Enter the name of the client: ")
data = input("You want to retrieve or log the data: ")
if data == "retrieve":
    retrieve(name)
else:
    log(name)   



