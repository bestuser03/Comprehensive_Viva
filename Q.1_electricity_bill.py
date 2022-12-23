#electricity bill generator

unit = float(input("Enter electricity meter measurement in unit: "))

un = unit
Rs = 0
total = 0

if un <= 50:
    Rs = (un * 50/100)
    total = (Rs + (Rs * 2/100))

elif (un > 50) and (un <= 100):
    Rs = (un * 1)
    total = (Rs + (Rs * 2/100))

elif (un > 100) and (un <= 250):
    Rs = (un * 150/100)
    total = (Rs + (Rs * 2/100))

elif un > 250:
    Rs = (un * 2)
    total = (Rs + (Rs * 3/100))

print(f"Electricity Bill Without Charge is = {float(Rs)} ")
print(f"Electricity Bill With Charge is = {float(total)}")
