# todo: work out how much they need to pay based on their size choice
# todo: work out how much to add to the bill based on their pepp choice
# todo: work out their final amount based on whether or not they want extra cheese

#interacting with the user
print("Welcome to Python Pizza Parlor")

#STEP 1: Prompt the user for the pizza size until a valid option is selected
size = ""
while size not in ["S", "M", "L"]:
    if size != "": #check if the user has already entered something
        print("Invalid size selected, please choose S, M or L")
    size = input("What size pizza would you like? S, M or L\n").upper()

#STEP 2: Set the base price for each pizza size
cost = 0 #set a default value to ensure it's always defined.

if size == "S":
    cost = 15
elif size == "M":
    cost = 20
elif size == "L":
    cost = 25
print(f"The base cost for your pizza is: ${cost}")

toppings = ""
while toppings not in ["Sausage", "Mushrooms", "Pepperoni"]:
    if toppings != "": #check if the user has already entered something
        print("Invalid topping selected, please choose Sausage, Mushrooms or Pepperoni")
    toppings = input("Which topping would you like Sausage, Mushrooms or Pepperoni\n").capitalize()

add_ons_price = 0

if toppings == "Sausage":
    add_ons_price = 3
elif toppings == "Mushrooms":
    add_ons_price = 5
elif toppings == "Pepperoni":
    add_ons_price = 6

# Calculate the Final Cost
final_cost = cost + add_ons_price

print(f"Your pizza with {toppings} topping costs ${final_cost}")


# extra_cheese = input("Do you want extra cheese? Y or N\n")




