global_var = 10  # Global variable

def multiply_by_global(number):
    local_var = 5  # Local variable
    return number * global_var * local_var

result = multiply_by_global(2)
print("Result:", result)
