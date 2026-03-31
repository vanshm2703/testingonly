try:
    print("Hello, World!")
except TypeError as e:
    print(f"A TypeError occurred: {e}")
except ValueError as e:
    print(f"A ValueError occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")