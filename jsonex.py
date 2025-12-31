import json

# JSON data as a string
json_str = '{"name": "Alice", "age": 25, "email": "alice@example.com"}'

# Convert JSON string to Python dictionary
data = json.loads(json_str)

# Accessing values
print(data["name"])  # Alice
print(data["age"])   # 25

# This program shows you how to go from json to python

#Example of reading a JSON file
# Open a JSON file and load its content into a Python dictionary
with open("data.json", "r") as file:
    data = json.load(file)

print(data)

#Example of writing JSON file
# Data to be written into JSON
data = {
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com"
}

# Write JSON to a file
with open("output.json", "w") as file:
    json.dump(data, file, indent=4)
    
#Example of Python to JSON
python_dict = {"name": "Alice", "age": 25}

# Convert to JSON string
json_str = json.dumps(python_dict, indent=4)

print(json_str)