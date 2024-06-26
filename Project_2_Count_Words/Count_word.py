def count_words(text):
    """
    This function takes a string input and returns the number of words in it.
    """
    # Split the text by spaces to get a list of words
    words = text.split()
    # Return the length of the list
    return len(words)

def main():
    """
    Main function to run the word counter program.
    """
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Enter a sentence or paragraph: ").strip()

    # Check for empty input
    if not user_input:
        print("Error: No input provided. Please enter some text.")
        return

    # Get the word count
    word_count = count_words(user_input)

    # Display the word count
    print(f"The number of words in the given text is: {word_count}")

# Entry point of the program
if __name__ == "__main__":
    main()
