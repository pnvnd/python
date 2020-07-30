usernames = []

if usernames:
    for user in usernames:
        if user == "admin":
            print(f"Hello, {user}!  Would you like to see a status report?")
        else:
            print(f"Hello, {user}!  Thank you for logging in")
else:
    print("We need to find some users!")