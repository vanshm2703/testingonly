def hello(name):
    """
    Prints a personalized greeting message.

    Args:
        name (str): The name to be used in the greeting.

    Returns:
        None
    """
    try:
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        print(f"hello {name}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

hello("John")