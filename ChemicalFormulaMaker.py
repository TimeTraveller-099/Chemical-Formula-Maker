from Elements import *


# Function for REACTION
def reactChemical(first_element, second_element):
    metal_atoms_subs = str(metals[first_element.lower()]).translate(subs)
    non_metal_atoms_subs = str(non_metals[second_element.lower()]).translate(subs)

    metal_atoms_int = int(metal_atoms_subs.translate(reverse_sub))
    non_metal_atoms_int = int(non_metal_atoms_subs.translate(reverse_sub))

    if metal_atoms_int == non_metal_atoms_int:
        print(f"Formula {str(first_element.capitalize())}{str(second_element.capitalize())}\n")
    elif metal_atoms_int == 1:
        print(f"Formula {str(first_element.capitalize())}{non_metal_atoms_subs}{str(second_element.capitalize())}\n")
    elif non_metal_atoms_int == 1:
        print(f"Formula: {str(first_element.capitalize())}{str(second_element.capitalize())}{metal_atoms_subs}\n")
    elif (metal_atoms_int > 1) and (non_metal_atoms_int > 1):
        print(f"Formula: {str(first_element.capitalize())}{non_metal_atoms_subs}{str(second_element.capitalize())}"
            f"{metal_atoms_subs}\n")


# Adding Metal FUNCTION
def addMetal(add_met, met_val):
    metals[add_met.lower()] = met_val
    print("\nMetal has been added.\n")


# Adding Non-Metal FUNCTION
def addNonMetal(add_non_met, non_met_val):
    non_metals[add_non_met.lower()] = non_met_val
    print("\nNon-Metal has been added.\n")


# PROGRAM INTRO
print("_____CHEMICAL FORMULA MAKER_____\n")

# Password Checker
user_chances = 0
correct = False
password = "allow"

while user_chances < 3:
    user = input("Enter Password: ")
    if user == password:
        print("\n____Access Granted____\n")
        correct = True
        break
    elif user_chances == 2:
        print("Incorrect Password\n")
        print("Access Denied\n")
        break
    else:
        user_chances += 1
        print(f"Incorrect Password! {3 - user_chances} chances remaining.\n")

# ------------INTRO------------
if correct:
    print("-----------Commands-----------")
    print("> React - To Make Chemical Formula.")
    print("> All - To see all Elements you can make formula of.")
    print("> Add - To add an Element.")
    print("> 'E' - To Exit.\n")

# While LOOP
while correct:
    user_choice = input("Enter Command: \n>> ")
    uc = user_choice.lower()
    if uc == 'react':
        print("\nMaking Formula...\n")
        user_metal = input("Enter Metal Symbol: ")
        user_non_metal = input("Enter Non-Metal Symbol: ")
        chosen_metal = user_metal.lower()
        chosen_non_metal = user_non_metal.lower()
        print()

        if chosen_metal in metals and chosen_non_metal in non_metals:
            reactChemical(user_metal, user_non_metal)
        elif chosen_metal not in metals and chosen_non_metal in non_metals:
            print(f"{user_metal.capitalize()} is not available currently.")
        elif chosen_metal in metals and chosen_non_metal not in non_metals:
            print(f"{user_non_metal.capitalize()} is not available currently.")
        else:
            print(f"{user_metal} and {user_non_metal} are not Available, Enter Add Command to React them.\n")

    elif uc == 'all':
        metal_list = list(metals.keys())
        non_metal_list = list(non_metals.keys())
        print(f'\nMetals: {metal_list}\nNon Metals: {non_metal_list}\n')

    elif uc == "add":
        chooseElement = input("What you want to add: \nm- Metal\nn - Non-Metal\n>> ")
        if chooseElement == "m":
            print("\nAdding Metal...\n")
            add_your_metal = input("Enter Metal Symbol to Add: ")
            add_metal_valency = int(input("Enter Valency: "))

            # Calling Add Metal Function
            addMetal(add_your_metal, add_metal_valency)

        elif chooseElement == "n":
            print("\nAdding Non-Metal...\n")
            add_non_metal = input("Enter Non-Metal Symbol: ")
            add_non_metal_valency = int(input("Enter Valency: "))

            # Calling Add Non-Metal Function
            addNonMetal(add_non_metal, add_non_metal_valency)

    elif uc == 'e':
        break
    else:
        print(f"{user_choice.capitalize()} YOU GAVE ME WRONG WORD, TRY AGAIN\n")
