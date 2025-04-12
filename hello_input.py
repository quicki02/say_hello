def say_hello(name):
    """Function that returns a greeting message."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Ask the user to input their name
    user_name = input("Enter your name: ")
    
    # Display the greeting message
    print(say_hello(user_name))
