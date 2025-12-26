# Lists are ordered
# Tuples are immutable(can't be changed after creation)
# Sets don't allow duplciates, everything is listed only once
# Dictionaries allow easy lookup

#Btw mutable means you can add, remove, or rearrange

#---List---
# Ordered, mutable, heterogenous(can hold different types of data)
# Creating a list of fruits
# Syntax = []
print("List:\n")
fruits = ["apple", "banana", "cherry"]

# Adding an item
fruits.append("orange")  # Now the list is ["apple", "banana", "cherry", "orange"]
# Removing an item
fruits.remove("banana")  # Now the list is ["apple", "cherry", "orange"]
# Accessing an item
print(fruits[0])  # This will print "apple”
# Used for Easy organization, flexibility, and accessibility
#======================

#----Tuples----
# Ordered, immutable, heterogenous
# Creating a tuple of fruits
#Syntax = ()
print("Tuple:\n")
fruits_tuple = ("apple", "banana", "cherry")
# Accessing an item
print(fruits_tuple[0])  # This will print "apple"
# Trying to change a value (this will raise an error because tuples are immutable)
# fruits_tuple[1] = "orange"
# Used for data integrty(good for fixed sets of data), Performance(faster),Protection
#=======================

#----Sets----
# Unordered, unique items(removes duplicates), Mutable, Immutable items(can't mix different data types)
# Creating a set of grocery items
# Syntax = {}
print("Set:\n")
grocery_set = {"apples", "bananas", "milk"}

# Adding an item
grocery_set.add("bread")  # Now the set is {"apples", "bananas", "milk", "bread"}

# Removing an item
grocery_set.remove("bananas")  # Now the set is {"apples", "milk", "bread"}

# Trying to add a duplicate item (it won’t be added)
grocery_set.add("milk")  # Set remains {"apples", "milk", "bread"}

# Accessing items in a set (sets don’t have indexes)
for item in grocery_set:
    print(item)  # This will print the items, but in any order
#=========================

#----Dictionaries----
# Key value pairs, each item has a key (item name and the quantity), Mutable, no duplicates for keys, unordered
# Initial dictionary with grocery items and their quantities
print("Dictionary:\n")
grocery_list = {"apples": 4, "bananas": 6, "milk": 2}

# Adding a new item to the dictionary
grocery_list["bread"] = 1
print(f"Updated list after adding bread: {grocery_list}")

# Updating the quantity of an existing item (bananas)
grocery_list["bananas"] = 8
print(f"Updated list after changing banana quantity: {grocery_list}")

# Removing an item from the dictionary (milk)
grocery_list.pop("milk")
print(f"Updated list after removing milk: {grocery_list}")

# Accessing the quantity of a specific item (apples)
print(f"Number of apples: {grocery_list['apples']}")