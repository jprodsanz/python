print("Welcome to the tip calculator!")

# Get the total bill amount

bill = float(input("What was the total bill? $\n"))
print(bill)

# Get the tip percentage and convert it to a float

tip_percentage = float(input("What percentage tip would you like to give? 10, 12, 15 or 20\n"))
print(tip_percentage)

# Calculate the tip amount
tip_amount = bill * (tip_percentage / 100)
print(tip_amount)

#Calculate the total bill including the tip
total_bill = bill + tip_amount
print(total_bill)

#Get the number of people splitting the bill
split = int(input("How many people are splitting it"))
print(split)

# Calculate how much each person should pay
amount_per_person = total_bill / split

#Print the result rounded to 2 decimal places
print(f"Each person should pay: ${amount_per_person:.2f}")