hi.py
```python
try:
    print("Hello, World!")
except (RuntimeError, TypeError, NameError) as e:
    print(f"An error occurred: {e}")
```