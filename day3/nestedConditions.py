print("Welcome to the rollercoaster!")

height = float(input("What is your height in CM?\n"))
bill = 0

if height >= 120:
    print("You can't ride the rollercoaster\n")
    age = int(input("What is your age?\n"))
    if age <=12:
        bill = 5
        print("Please pay $5")
    elif age <= 18:
        bill = 7
        print("Please pay $7")
    else:
        print("Please pay $12.")
        bill = 12
    wants_photo = input("Would you like a photo taken? Y or N")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is {bill}")
else:
    print("Sorry you have to be taller before you can ride\n")
