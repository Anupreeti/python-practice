# Write a simple "Tip Calculator" program:
# Input: bill amount, tip %, number of people
# Output: total per person

amount = int(input("Eneter bill amount = "))
num_people = int(input("Eneter number of people = "))
tip = int(input("Enter tip value = "))
def totalBill(amount,tip):
    totalBill= ((amount*tip)/100) + amount
    return totalBill
bill= totalBill(amount,tip)
bill_per_person = bill/num_people
print(f"Bill per person = {bill_per_person}")
