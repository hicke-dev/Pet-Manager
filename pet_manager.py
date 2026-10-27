def menu():
    print("--- PET MANAGER ---")
    print("1. Add a pet")
    print("2. Show all pets")
    print("3. Find a pet")
    print("4. Remove a pet")
    print("5. Quit")

def digits(question):
    choose = (input(question))
    while not choose.isdigit():
        print("Only digits")
        choose = (input(question))
    return int(choose)
 
pets = {
    "tandlöse": {"species":"dragon","age":"17"},
    "kaneki": {"species":"centipede","age":"7"}
}    

while True :
    menu()
    answer = digits("What do u want to do: ")
    if answer == 5:
        print("bye")
        break
    if answer == 2:
        for key,value in pets.items():
            print(f"we have {key} and they are a {value['species']}, {value['age']} years old")
        back = digits("5 to exit , anything digit else to go back: ")
        if back == 5:
                break
        else:
            print("_____________")
                
    if answer == 4:
        remove = input("Which pet would u like to remove, (type name): ")
        if remove.lower() in pets:
            print("removed")
            del(pets[remove.lower()])
            print("_____________")
        else :
            print("not found")
    if answer == 3:
        find = input("Which pet are u looking for: ")
        f_pet = find.lower()
        if f_pet in pets:
            print(f"{f_pet} is here and its a {pets[f_pet]['species']} its {pets[f_pet]['age']} years old")
        else :
            print("its not here")
        print("_____________")
    if answer == 1:
        new_pet_name = input("What is the name of the pet: ")
        new_pet_species = input("What is the species of the pet: ")
        new_pet_age = input("What is the age of the pet: ")
        if new_pet_name.lower() in pets:
            print("its already here")
        else:
            pets[new_pet_name.lower()] = {"species": new_pet_species, "age": new_pet_age}
            print("added")
    if answer < 1 or answer > 5:
        print("that option does not exist ")
    
