def hello_world():
    try:
        print("hello")
    except Exception as e:
        import logging
        logging.error(f"An error occurred: {e}")

def main():
    hello_world()

if __name__ == "__main__":
    main()