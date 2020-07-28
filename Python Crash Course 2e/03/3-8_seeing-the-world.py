# Store locations in a list
places = ["Tokyo", "Sapporo", "Akihabara", "Guangzhou", "Xiamen"]

# Print original order
print(places)

# Sort list without modifying original list
print(sorted(places))

# Print original list to see original order
print(places)

# Sort list in reverse order without modifying original
print(sorted(places, reverse=True))

# Print original list to see original order
print(places)

# Reverse original list and print list to show changes
places.reverse()
print(places)

# Reverse list and print list to show original order
places.reverse()
print(places)

# Sort list permanantly
places.sort()
print(places)

# Sort list permanantly in reverse order
places.sort(reverse=True)
print(places)