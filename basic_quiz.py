class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def take_quiz(self):
        for i, question in enumerate(self.questions, start=1):
            print(f"\nQuestion {i}: {question['text']}")
            for j, option in enumerate(question['options'], start=1):
                print(f"{j}. {option}")

            try:
                user_answer = int(input("Your answer (enter the number): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if 1 <= user_answer <= len(question['options']):
                if question['correct_option'] == user_answer:
                    print("Correct! 🎉")
                    self.score += 1
                else:
                    print(f"Incorrect. The correct answer is {question['correct_option']}.")
            else:
                print("Invalid choice. Please enter a valid option.")

    def show_score(self):
        print(f"\nYour final score: {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    print("Welcome to the Basic Quiz!")

    quiz_questions = [
        {
            'text': 'What is the capital of France?',
            'options': ['Paris', 'London', 'Berlin', 'Madrid'],
            'correct_option': 1,
        },
        {
            'text': 'Which planet is known as the Red Planet?',
            'options': ['Earth', 'Mars', 'Jupiter', 'Venus'],
            'correct_option': 2,
        },
        {
            'text': 'What is the largest mammal?',
            'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
            'correct_option': 2,
        },
    ]

    quiz = Quiz(quiz_questions)
    quiz.take_quiz()
    quiz.show_score()
