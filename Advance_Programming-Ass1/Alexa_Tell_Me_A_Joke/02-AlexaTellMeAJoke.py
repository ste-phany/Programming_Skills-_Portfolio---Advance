import random  # Import random module to select a joke randomly

# Function to load jokes from a text file
def load_jokes():
    # Open the joke.txt file in read mode with UTF-8 encoding
    with open("joke.txt", "r", encoding="utf-8") as f:
        # Read lines, strip whitespace, and ignore empty lines
        return [line.strip() for line in f if line.strip()]

# Function to tell a single joke
def tell_jokes(jokes):
    joke = random.choice(jokes)  # Pick a random joke from the list
    # Check if the joke has a question mark (i.e., it has a setup and punchline)
    if "?" in joke:
        setup, punchline = joke.split("?", 1)  # Split into setup and punchline
        print("Alexa: ", setup + "?")  # Display the setup part
        input("Press Enter for a punchline..")  # Pause until user presses Enter
        print(punchline)  # Display the punchline
    else:
        print("Alexa: ", joke)  # If no question mark, just display the whole joke

# Main function controlling the interaction
def main():
    Jokes = load_jokes()  # Load all jokes from the file
    print("Type 'alexa tell me a joke', or 'quit' to stop.")  # Instructions to user

    while True:  # Infinite loop for user input
        ask = input("\nYou: ").lower()  # Get user input and convert to lowercase
        if ask == "alexa tell me a joke":  # If user asks for a joke
            tell_jokes(Jokes)  # Tell a random joke
        elif ask == "quit":  # If user wants to exit
            print("ok.. byee no more joke then womp :(")
            break  # Exit the loop and program
        else:  # For any other input
            print("Alexa : I can only tell jokes :)")  # Inform user of valid commands

# Run the main function if the file is executed directly
main()

# ============== Alexa Tell Me A joke Vid Link - https://youtu.be/PWQ9muwKGWA ====================