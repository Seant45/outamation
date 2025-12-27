#In Python, a function is a reusable block of code designed to perform a specific task. 
# Types of FunctionsBroadly, we can classify the combination of function parameters and their return types as follows:
# Nothing goes in, nothing comes out.
# Nothing goes in, something comes out.
# Something goes in, nothing comes out.
# Something goes in, something comes out.

# 1. Nothing goes in, nothing comes out
print("Nothing goes in, nothing comes out")

def say_hello():
    print("Hello, welcome to the program!")

say_hello()


# 2. Nothing goes in, something comes out
print("\nNothing goes in, something comes out")

def get_default_score():
    return 100

score = get_default_score()
print("Returned value:", score)


# 3. Something goes in, nothing comes out
print("\nSomething goes in, nothing comes out")

def print_square(num):
    print("Square:", num * num)

print_square(5)


# 4. Something goes in, something comes out
print("\nSomething goes in, something comes out")

def add_numbers(a, b):
    return a + b

result = add_numbers(3, 4)
print("Returned value:", result)
