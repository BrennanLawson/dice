import random
import sys

def remove(string_input): 
    return string_input.replace(" ", "") 

def rolldice (sides, number, mod): #takes in the number of sides, number of dice, and modifier and returns the total
    total = 0
    for i in range(number):
        total += random.randint(1, sides)

    total += mod
    return total

def roll_interpreter(string_input): #takes in a string and returns the total of the roll
    string_input = remove(string_input)
    sides = int(string_input[0])
    number = int(string_input[1])
    mod = int(string_input[2:])
    return rolldice(sides, number, mod)

print ("Welcome to the dice roller!" "For help, type 'help', to quit, type 'quit'")

while True:

    count = 1
    sides = 0
    number = 0
    mod = 0

    userinput = input("Enter your dice roll: ")
    if userinput == "help": #if the user types help, the help menu is printed   
        print ("")
    elif userinput == "q": 
        print ("goodbye") 
        break   

    else: #formats for rolls follow "xdy+-z" but can also be written like w(xdy+-z) to return multiple results of the same roll, multiple rolls can also be input, separated by commas and spaces
        userinput = userinput.split(",") #splits the input into a list of strings if there are multiple rolls
        for i in range(len(userinput)):
            
            userinput[i] = 'r' + userinput[i] #adds the r to the beginning of the string to make it a raw string for regex 
            print(userinput[i])
            
            """""
            userinput[i] = remove(userinput[i]) #removes spaces from the input ##also need to have ) removed

            #detect and conditionally multisplit on +- and (), dump cut sections into variables in corrosponding lists, then do the same on d
            count_in_string = re.search(r'\d+', userinput[i])
            if count_in_string:
            
"""



