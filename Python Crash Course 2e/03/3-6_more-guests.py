guests = ["Peter", "Cathy", "Leon"]

for guest in guests:
    print(f"Hello, {guest}!  You are invited to a dinner party.")

print(f"We have room for more guests at the dinner party.")

# Add guest to beginning of list
guests.insert(0, "Ella")

# Add guest to middle of list using floor divide // to get an int index
middle = len(guests)//2
guests.insert(middle, "Hayden")

# Add guest to end of list
guests.append("Bryan")

for guest in guests:
    print(f"Hello, {guest}!  You are invited to a dinner party.")
