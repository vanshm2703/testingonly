try:
    print("Hello, World!")
except (TypeError, ValueError, ImportError, ModuleNotFoundError) as e:
    print(f"An error occurred: {e}")