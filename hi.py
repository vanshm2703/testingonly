try:
    print("Hello, World!")
except TypeError as exception_message:
    print(f"A type error occurred: {exception_message}")
except ValueError as exception_message:
    print(f"A value error occurred: {exception_message}")
except Exception as exception_message:
    print(f"An unexpected error occurred: {exception_message}")