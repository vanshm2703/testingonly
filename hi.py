import logging

logging.basicConfig(level=logging.INFO)

def hello(name):
    """
    Prints a greeting message to the console.

    Args:
        name (str): The name to be used in the greeting.

    Returns:
        None
    """
    logging.info(f"Hello, {name}!")

def main():
    name = input("Enter your name: ")
    if name:
        hello(name)
    else:
        logging.warning("Name cannot be empty.")

if __name__ == "__main__":
    main()