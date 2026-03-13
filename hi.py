hello_script.py
```python
def greet(name):
    try:
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        print(f"hello {name}")
        return "Hello, " + name + "!"
    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

greet("John")
```