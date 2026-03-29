# hi_script.py

try:
    print("Hello, World!")
except TypeError as e:
    print(f"An error occurred: {e}")
except ValueError as e:
    print(f"An error occurred: {e}")
except Exception as e:
    print(f"An unknown error occurred: {e}")