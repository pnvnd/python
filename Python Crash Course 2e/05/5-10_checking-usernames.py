current_users = ["sikk", "admin", "Ruan", "bladez", "pen15", "gfui"]
new_users = ["sikky", "administrator", "ruan", "blades", "pen15", "gfui"]

users = [x.lower() for x in current_users]
print(users)

for user in new_users:
    if user.lower() in users:
        print(f"{user} has already been taken, please try again.")
    else:
        print(f"{user} is available.")