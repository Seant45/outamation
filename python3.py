# Control Flow
# Refers to the order in which the statements or instructions in a program are executed.
# ============== Sequential Statements
# It goes in order
print("Sequential Statements: \n")
print("Wake up")
print("Have breakfast")
print("Attend Meetings")
# ============= Decision Making / Condtional Statements
print(" Decision-Making/Conditional Statements: \n")
weather = "cloudy"

if weather == "rainy":
    print("Don't forget to take an umbrella!")
elif weather == "sunny":
    print("It's a sunny day! Enjoy the sunshine!")
elif weather == "cloudy":
    print("It might rain later, keep an eye on the weather!")
else:
    print("Weather conditions unknown. Stay prepared!")
    
# If / else statements
# ==============  Loops/ Repetition
print("For loop:")
for i in range(10):
    print(i)
    
print("While loop")
sean = 0
while(sean < 10):
    sean+=1
    print(sean)
#========================
#========== Jump Statements

print("Break:")
inventory = ["good", "good", "damaged", "good"]

for item in inventory:
    if item == "damaged":
        print("Damaged item found. Stopping inspection.")
        break
    print("Item checked:", item)

print("Continue:")
inventory = ["reorder", "good", "reorder", "good"]

for item in inventory:
    if item == "reorder":
        continue  # skip this item
    print("Processing item:", item)

print("Pass:")
inventory = [0, 5, 12]

for stock in inventory:
    if stock == 0:
        pass  # nothing happens here
    elif stock < 10:
        print("Reorder item")
