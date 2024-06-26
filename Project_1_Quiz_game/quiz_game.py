# quiz_game.py

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "What is 10 * 25?",
        "options": ["A. 300", "B. 250", "C. 230", "D. 260"],
        "answer": "B"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["A. Elephant", "B. Blue whale", "C. Giraffe", "D. Shark"],
        "answer": "B"
    }
]

def ask_questions(questions):
    score = 0
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        while answer not in ["A", "B", "C", "D"]:
            answer = input("Invalid input. Please enter A, B, C, or D: ").strip().upper()
        if answer == q["answer"]:
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer is {q['answer']}.")
        print()
    return score

def main():
    while True:
        score = ask_questions(questions)
        print(f"Your final score is: {score}/{len(questions)}")
        replay = input("Do you want to play again? (yes/no) ").strip().lower()
        if replay != 'yes':
            break

if __name__ == "__main__":
    main()