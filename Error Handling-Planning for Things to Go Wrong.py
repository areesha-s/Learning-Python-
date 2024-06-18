# Handle a potential division by zero error.
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        result = None
    return result

# Test the function
print(divide(10, 2))  # Should print 5.0
print(divide(10, 0))  # Should print the error message
