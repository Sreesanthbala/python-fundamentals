
# Set :
# A set is a collection of :
# - unique elements
# - unordered
# - no duplicate values
# - mutable
# - no indexing


# Creating a Set :

busStops = {"Madhapur", "Kukatpally", "Miyapur", "Madhapur", "Miyapur"}
print(busStops)

# Why sets :
# Removes duplicate values automatically
# Fast lookups
# Fast insertions and deletions



# Set Operations :
# Union :
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.union(set2)
print(set3)

# intersection :
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.intersection(set2)
print(set3)

# difference :
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.difference(set2)
set4 = set2.difference(set1)
print(set3)
print(set4)