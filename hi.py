def hello_world():
    try:
        print("hello")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    hello_world()
    return

if __name__ == "__main__":
    main()