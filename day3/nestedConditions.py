print("Welcome to the rollercoaster!")

height = float(input("What is your height in CM?\n"))

if height >= 120:
    print("You can't ride the rollercoaster\n")
    age = int(input("What is your age?\n"))
    if age <=12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to be taller before you can ride\n")
