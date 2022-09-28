bill = float(input("enter amount of bill: $"))
amount_of_people = int(input("enter amount of people:"))
tip = float(input("amount of tips (%):"))

bill_per_person = bill / amount_of_people
print(f"amount of bill per person: {bill_per_person}")

tip_calc = bill * (tip/100) / amount_of_people
print(f"total amount of tip per person: {tip_calc}")

total_spent_per_person = bill_per_person + tip_calc
print(f"total spent per person {total_spent_per_person}")