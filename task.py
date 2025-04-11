print("Welcome to the tip calculator!!!")
total_bill = input("What was the total bill?\n")
tip = input("How much tip would you like to give, 10, 12, 15\n")
tip_amount = (int(tip) / 100) + 1
party = input("How many people will split the bill?\n")
each_pay= (float(total_bill)/float(party)) * float(tip_amount)
new_total = round(each_pay,2)
bill_per_person = f"{new_total:.2f}"

print(f"Each person should pay  ${bill_per_person}")
