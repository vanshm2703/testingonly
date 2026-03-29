try:
    print("Hello, World!")
except TypeError as error_message:
    print(f"A TypeError occurred: {error_message}")
except ValueError as error_message:
    print(f"A ValueError occurred: {error_message}")
except ImportError as error_message:
    print(f"An ImportError occurred: {error_message}")
except Exception as error_message:
    print(f"An unexpected error occurred: {error_message}")