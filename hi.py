try:
    print("Hello, World!")
except TypeError as exception:
    print(f"A TypeError occurred: {exception}")
except ValueError as exception:
    print(f"A ValueError occurred: {exception}")
except ImportError as exception:
    print(f"An ImportError occurred: {exception}")
except Exception as exception:
    print(f"An unexpected error occurred: {exception}")