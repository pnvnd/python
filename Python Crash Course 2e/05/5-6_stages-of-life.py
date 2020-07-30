age = 21

if age < 2:
    stage = "Baby"
elif age >= 2 and age < 4:
    stage = "Toddler"
elif age >= 4 and age < 13:
    stage = "Kid"
elif age >= 13 and age < 20:
    stage = "Teenager"
elif age >= 20 and age < 65:
    stage = "Adult"
elif age >= 65:
    stage = "Elder"

print(f"Age {age} is typically a(n) {stage}")