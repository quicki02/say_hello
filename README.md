# say_hello
Hello
# Navigate to your existing Git repository
cd path/to/your/repository

# Create the script file
echo 'def say_hello(name):\n    """Function that returns a greeting message."""\n    return f"Hello, {name}!"\n\nif __name__ == "__main__":\n    user_name = input("Enter your name: ")\n    print(say_hello(user_name))' > hello_input.py

# Add the new file to Git
git add hello_input.py

# Commit the changes with a message
git commit -m "Added interactive Hello World script"

# Push to GitHub
git push origin main
