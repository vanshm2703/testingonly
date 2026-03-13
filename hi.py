#!/usr/bin/env python3
"""
A simple hello world script.
"""

def hello():
    name = input("Please enter your name: ")
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, stranger!")

hello()