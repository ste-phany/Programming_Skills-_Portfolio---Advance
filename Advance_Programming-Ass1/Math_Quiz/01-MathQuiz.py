import random  # Import random module for generating random numbers and choices

# Function to display the difficulty menu and get the user's choice
def displayMenu():
    print("\nDIFFICULTY LEVEL")
    print(" 1. Easy")
    print(" 2. Moderate")
    print(" 3. Advanced")
    while True:
        try:
            level = int(input("Choose difficulty level (1-3): "))  # Get input from user
            if level in [1, 2, 3]:  # Check if input is valid
                return level  # Return chosen difficulty level
            else:
                print("Invalid choice. Please select 1, 2, or 3.")  # Invalid input message
        except ValueError:
            print("Please enter a valid number (1-3).")  # Handle non-integer input

# Function to generate two random numbers based on difficulty level
def randomInt(level):
    """Generates two random numbers based on difficulty level."""
    if level == 1:
        return random.randint(1, 9), random.randint(1, 9)  # Easy: 1-9
    elif level == 2:
        return random.randint(10, 99), random.randint(10, 99)  # Moderate: 10-99
    else:
        return random.randint(1000, 9999), random.randint(1000, 9999)  # Advanced: 1000-9999

# Function to randomly choose the operation (addition or subtraction)
def decideOperation():
    """Randomly choose between addition or subtraction."""
    return random.choice(["+", "-"])

# Function to display the math problem and get the user's answer
def displayProblem(num1, num2, op):
    """Display the problem and get the user's answer."""
    while True:
        try:
            answer = int(input(f"{num1} {op} {num2} = "))  # Ask user for answer
            return answer  # Return the user's answer
        except ValueError:
            print("Please enter a valid integer.")  # Handle non-integer input

# Function to check if the user's answer is correct
def isCorrect(num1, num2, op, user_answer):
    """Check if the user's answer is correct."""
    correct_answer = num1 + num2 if op == "+" else num1 - num2  # Calculate correct answer
    return user_answer == correct_answer, correct_answer  # Return result and correct answer

# Function to display final results and grade
def displayResults(score):
    """Display the user's total score and grade."""
    print("\n--- QUIZ RESULTS ---")
    print(f"Your final score: {score}/100")  # Show total score

    # Determine grade based on score
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"Your grade: {grade}")  # Display grade
    print("---------------------\n")

# Function to play the quiz game
def playQuiz():
    level = displayMenu()  # Get difficulty level from user
    score = 0  # Initialize score
    total_questions = 10  # Set total number of questions

    print("\nLet's start the quiz!\n")

    # Loop through each question
    for q in range(1, total_questions + 1):
        num1, num2 = randomInt(level)  # Generate random numbers
        op = decideOperation()  # Decide operation (+ or -)

        print(f"Question {q}:")
        answer = displayProblem(num1, num2, op)  # Ask user for answer

        correct, correct_answer = isCorrect(num1, num2, op, answer)  # Check answer

        if correct:
            print("✅ Correct! You earned 10 points.\n")
            score += 10  # Add 10 points for first attempt correct
        else:
            print("❌ Incorrect. Try once more.")  # Ask second attempt
            answer = displayProblem(num1, num2, op)
            correct, _ = isCorrect(num1, num2, op, answer)
            if correct:
                print("✅ Correct! You earned 5 points.\n")
                score += 5  # Add 5 points for second attempt correct
            else:
                print(f"❌ Wrong again. The correct answer was {correct_answer}.\n")

    displayResults(score)  # Show final results after quiz

# Main function to start and control the game loop
def main():
    print("🎯 Welcome to the Maths Quiz!")  # Welcome message
    while True:
        playQuiz()  # Start the quiz
        again = input("Would you like to play again? (y/n): ").strip().lower()  # Ask if user wants to replay
        if again != "y":  # Exit if user says no
            print("\nThanks for playing! Goodbye 👋")
            break

# Run the main function only if this file is executed directly
if __name__ == "__main__":
    main()

# ========== MathQuiz Vid Link - https://youtu.be/IhpOZO7fhHA ===============
