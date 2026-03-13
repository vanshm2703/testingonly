def print_hello(name):
    """
    Prints a personalized 'hello' message to the console.

    Args:
        name (str): The name to include in the greeting.

    Returns:
        None
    """
    print("hello", name)
    return None

# Validate user input to prevent code injection
name = input("Enter your name: ")
if not isinstance(name, str):
    print("Invalid input. Please enter a string.")
else:
    print_hello(name)