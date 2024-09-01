print("Welcome to the tip calculator!.")
bill = float(input("What was the total bill?"))
tip = int(input("What % tip would you like to give?"))
people = int(input("How many people to split the bill?"))
tip_value= bill * (tip/100)
final_bill= (bill + tip_value)/people
final_amt = round(final_bill,2)
final_amt = "{:.2f}".format(final_bill)
print(f"Each person should pay: {final_amt}")