#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# Greeting
print("Welcome to the tip calculator.")

# Three Inputs
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Vairable for bill with tip
bill_with_tip = tip / 100 * bill + bill

# Variable for bill with tip divided by people 
bill_per_person = bill_with_tip / people

# Variable for final bill round to two decimal places
final_bill = round(bill_per_person, 2)

# Print final bill for each person
print(f"Each person should pay ${final_bill}: ")
