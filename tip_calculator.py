#printing welcome message with taking user input
print("Welcome to the tip calculator!.")
#type casting string to float
bill = float(input("What was the total bill?"))
#type casting string to int
tip = int(input("What % tip would you like to give?"))
people = int(input("How many people to split the bill?"))

#calculating tip value
tip_value= bill * (tip/100)
#adding tip value to variable final_bill
final_bill= (bill + tip_value)/people
#using round function to set the vakue at 2 decimal
final_amt = round(final_bill,2)
final_amt = "{:.2f}".format(final_bill)

#printing final result
print(f"Each person should pay: {final_amt}")