hi.py
```python
try:
    print("Hello, World!")
except (SystemExit, KeyboardInterrupt):
    pass
except Exception as e:
    print(f"An error occurred: {e}")
```