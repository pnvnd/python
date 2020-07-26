guests = ["Peter", "Cathy", "Leon"]

for guest in guests:
    print(f"Hello, {guest}!  You are invited to a dinner party.")

print(f"Oh, no!  {guests[0]} can't make it to the dinner party.")

# Replace name of guest who can't attend.
guests[0] = "Ella"

for guest in guests:
    print(f"Hello, {guest}!  You are invited to a dinner party.")
