guests = ["Peter", "Cathy", "Leon"]

for guest in guests:
    print(f"Hello, {guest}!  You are invited to a dinner party.")

print("\nWe have room for more guests at the dinner party.")

# Add guest to beginning of list
guests.insert(0, "Ella")

# Add guest to middle of list using floor divide // to get an int index
middle = len(guests)//2
guests.insert(middle, "Hayden")

# Add guest to end of list
guests.append("Bryan")

for guest in guests:
    print(f"Hello, {guest}!  You are invited to a dinner party.")

print("\nWe have no room for guests at the dinner party.")

# Remove guests from the end of the list until 2 guests are left

while len(guests) > 2:
    print(f"Sorry, {guests.pop()}!  We have no more room at the dinner party.")

# Message for remaining guests
for guest in guests:
    print(f"Hello, {guest}!  You are invited to a dinner party.")

# Remove guests from guestlist and print guestlist
while len(guests) > 0:
    del guests[0]
    print(guests)