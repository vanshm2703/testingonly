print("Hello, World!\n")
try:
    pass
except SystemExit:
    pass
except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"An error occurred: {e}")