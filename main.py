def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

user_input = input("Enter an integer: ")
n = int(user_input)
if n < 0:
    print("Please enter a non-negative integer.")
else:
    result = factorial(n)
    print(f"The factorial of {n} is {result}")

