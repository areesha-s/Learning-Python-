active = True

while active:
    message = input("Enter a message (type 'quit' to end): ")
    if message == "quit":
        active = False
    else:
        print("You entered:", message)
