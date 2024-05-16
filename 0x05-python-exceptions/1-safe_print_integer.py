#!/usr/bin/python3

def safe_print_integer(value):
    try:
        
        formatted_value = "{:d}".format(value)
        # Print the formatted integer followed by a new line
        print(formatted_value)
        # Return True to indicate successful printing
        return True

    except Exception:
        print("Error: Value is not an integer")
        # Return False to indicate failure in printing
        return False
