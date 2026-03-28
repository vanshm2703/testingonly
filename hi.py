hi_script.py
```python
try:
    print("Hello, World!")
except TypeError as e:
    print(f"A type error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```