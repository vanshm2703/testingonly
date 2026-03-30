try:
    print("Hello, World!")
except TypeError as e:
    print(f"A type error occurred: {e}")
except ValueError as e:
    print(f"A value error occurred: {e}")
except OSError as e:
    print(f"An OS error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")