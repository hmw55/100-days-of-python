print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percent would you like to tip? 15, 20, 23? "))
people = int(input("How many people are splitting the bill? "))

# Angela uses "tip-as-percent", I am using "tip-rate" for a concise style
tip_rate = tip / 100

# Angela uses this line; however, I have removed its functionality with my changes to total_bill
## total_tip_amount = bill * tip_rate

# Angela usese "bill + total_tip_amount"; however, my change removes the need for an intermediate value
total_bill = bill * (1 + tip_rate)
bill_per_person = total_bill / people

# My change uses an f-string with .2f formatting, which is cleaner and avoids the floating point issues that round() sometimes causes.
# I will remove the need for this intermediate value in my print statement.
## final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${bill_per_person:.2f}")