# Create a list with square brackets []
languages = ["english", "japanese", "mandarin", "cantonese", "vietnamese", "korean"]
print(languages)

# Accessing Elements in a List, position index starts at 0
print(languages[2])

# Using individual values from a list
print(f"My first language is {languages[4].title()}.")

# Swap items in a list
languages[5] = "thai"
print(languages)

# Add elements to end of list
languages.append("korean")
print(languages)

# Insert element at some index in a list
languages.insert(1, "khmer")
print(languages)

# Delete an element from the list
del languages[1]
print(languages)

# Pop last item from the list
languages.pop()
print(languages)

# Pop item from any position from list
languages.pop(5)
print(languages)

# Removing item by value
languages.remove("english")
print(languages)

# Sort list permanantly
languages.sort()
print(languages)

# Sort list permanantly in reverse order
languages.sort(reverse=True)
print(languages)

# Temp sort
print(sorted(languages))

# Temp sort in reverse order
print(sorted(languages, reverse=True))

# Reverse list permanantly
languages.reverse()
print(languages)

# Get length of list
print(len(languages))