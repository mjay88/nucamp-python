# creating a mock battle game
wizard = "Wizard"
wizard_hp = 70
wizard_damage = 150

elf = "Elf"
elf_hp = 100
elf_damage = 100

human = "Human"
human_hp = 150
human_damage = 20

dragon_hp = 300
dragon_damage = 50

while True:
    print("1) " + wizard + "\n2) " + elf + "\n3) " + human)
    user_choice = input("Choose your character: ")
    if user_choice == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif user_choice == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif user_choice == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Unknown Character")

print(
    "You have chosen the character: "
    + character
    + "\nHealth: "
    + str(my_hp)
    + "\nDamage: "
    + str(my_damage)
)

while True:
    dragon_hp = dragon_hp - my_damage
    print("The " + character + " damaged the Dragon!")
    print("The Dragon's hitpoints are now: " + str(dragon_hp))
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break
    my_hp = my_hp - dragon_damage
    print("The Dragon strikes back at the " + character)
    print("The " + character + "'s hitpoints are now: " + str(my_hp))
    if my_hp <= 0:
        print("The " + character + " has lost the battle")
        break
