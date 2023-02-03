#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("welcome to the tip calculator")
bill = int(input("What was your total bill?"))
tip = float(input("What is your tip percentage?"))
people = int(input("How many people would you like to split the bill by?"))
bill_per_person = bill *(1+tip/100) / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
final_amount = print(f"Each person should pay ${final_amount}")
print(final_amount)