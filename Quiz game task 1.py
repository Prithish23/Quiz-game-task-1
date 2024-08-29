import tkinter as tk
from random import shuffle

# Quiz Data with Choices
quiz_data = {
    "Science": {
        "easy": [
            {"question": "What planet is known as the Red Planet?", "choices": ["Mars", "Venus", "Earth", "Jupiter"], "answer": "Mars"},
            {"question": "What gas do plants absorb from the atmosphere?", "choices": ["Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen"], "answer": "Carbon Dioxide"},
            {"question": "What is the boiling point of water?", "choices": ["90°C", "100°C", "110°C", "120°C"], "answer": "100°C"}
        ],
        "medium": [
            {"question": "What is the chemical symbol for gold?", "choices": ["Ag", "Au", "Pb", "Fe"], "answer": "Au"},
            {"question": "Which planet has the most moons?", "choices": ["Mars", "Jupiter", "Saturn", "Earth"], "answer": "Jupiter"},
            {"question": "What is the atomic number of carbon?", "choices": ["12", "6", "8", "14"], "answer": "6"}
        ],
        "hard": [
            {"question": "What is the powerhouse of the cell?", "choices": ["Nucleus", "Ribosome", "Mitochondria", "Chloroplast"], "answer": "Mitochondria"},
            {"question": "What is the most abundant gas in Earth's atmosphere?", "choices": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Argon"], "answer": "Nitrogen"},
            {"question": "What is the acceleration due to gravity on Earth?", "choices": ["9.8 m/s²", "10 m/s²", "9 m/s²", "9.5 m/s²"], "answer": "9.8 m/s²"}
        ]
    },
    "Math": {
        "easy": [
            {"question": "What is 5 + 7?", "choices": ["10", "11", "12", "13"], "answer": "12"},
            {"question": "What is the square root of 16?", "choices": ["2", "4", "8", "16"], "answer": "4"},
            {"question": "What is 10 - 4?", "choices": ["5", "6", "7", "8"], "answer": "6"}
        ],
        "medium": [
            {"question": "What is 12 x 12?", "choices": ["144", "121", "132", "156"], "answer": "144"},
            {"question": "What is 25% of 200?", "choices": ["25", "50", "75", "100"], "answer": "50"},
            {"question": "What is 7 x 8?", "choices": ["54", "56", "58", "60"], "answer": "56"}
        ],
        "hard": [
            {"question": "Solve for x: 2x + 3 = 7", "choices": ["2", "1", "3", "4"], "answer": "2"},
            {"question": "What is the derivative of x^2?", "choices": ["x", "2x", "x^2", "2"], "answer": "2x"},
            {"question": "What is the integral of 1/x?", "choices": ["ln(x)", "1/x", "x", "e^x"], "answer": "ln(x)"}
        ]
    }
}

# Quiz Logic
class Quiz:
    def __init__(self, topic, difficulty):
        self.topic = topic
        self.difficulty = difficulty
        self.questions = quiz_data[topic][difficulty]
        self.score = 0
        self.current_question_index = 0

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            return self.questions[self.current_question_index]
        else:
            return None

    def check_answer(self, selected_choice):
        correct_answer = self.questions[self.current_question_index]["answer"]
        return selected_choice == correct_answer

    def next_question(self):
        self.current_question_index += 1

    def get_score(self):
        return self.score

# Graphical User Interface
class QuizGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")
        self.master.geometry("800x600")  # Even Larger size for better visibility

        self.topic_var = tk.StringVar(value="Science")
        self.difficulty_var = tk.StringVar(value="easy")
        
        # Topic selection
        tk.Label(master, text="Select Topic:", font=("Arial", 20)).pack(pady=10)
        tk.OptionMenu(master, self.topic_var, *quiz_data.keys()).pack(pady=5)
        
        # Difficulty selection
        tk.Label(master, text="Select Difficulty:", font=("Arial", 20)).pack(pady=10)
        tk.OptionMenu(master, self.difficulty_var, "easy", "medium", "hard").pack(pady=5)
        
        # Start button
        tk.Button(master, text="Start Quiz", font=("Arial", 20), command=self.start_quiz).pack(pady=10)
        
        # Question display
        self.question_label = tk.Label(master, text="", font=("Arial", 24))
        self.question_label.pack(pady=20)
        
        # Choices display with distinct colors
        self.choice_var = tk.StringVar(value="")
        self.choice_buttons = []
        colors = ["red", "blue", "green", "black"]
        for i in range(4):  # Assuming 4 choices per question
            button = tk.Radiobutton(master, text="", variable=self.choice_var, value="", font=("Arial", 18), indicatoron=0, width=20, bg=colors[i], fg="white", padx=20, pady=10)
            button.pack(pady=10)
            self.choice_buttons.append(button)
        
        # Submit button
        tk.Button(master, text="Submit", font=("Arial", 20), command=self.submit_answer).pack(pady=20)
        
        # Feedback display
        self.feedback_label = tk.Label(master, text="", font=("Arial", 20))
        self.feedback_label.pack(pady=10)
        
        # Score display
        self.score_label = tk.Label(master, text="", font=("Arial", 20))
        self.score_label.pack(pady=10)

    def start_quiz(self):
        topic = self.topic_var.get()
        difficulty = self.difficulty_var.get()
        self.quiz = Quiz(topic, difficulty)
        self.show_next_question()

    def show_next_question(self):
        question_data = self.quiz.get_next_question()
        if question_data:
            self.question_label.config(text=question_data["question"])
            choices = question_data["choices"]
            shuffle(choices)  # Shuffle the choices to make it more engaging
            for i, choice in enumerate(choices):
                self.choice_buttons[i].config(text=choice, value=choice)
            self.choice_var.set("")  # Reset the selected choice
            self.feedback_label.config(text="")
        else:
            self.question_label.config(text="Quiz Over!")
            self.feedback_label.config(text="")
            self.score_label.config(text=f"Your Score: {self.quiz.get_score()}")

    def submit_answer(self):
        selected_choice = self.choice_var.get()
        if selected_choice:
            if self.quiz.check_answer(selected_choice):
                self.feedback_label.config(text="Correct!", fg="green")
                self.quiz.score += 1  # Increment score on correct answer
            else:
                self.feedback_label.config(text="Incorrect!", fg="red")
            self.quiz.next_question()
            self.show_next_question()
        else:
            self.feedback_label.config(text="Please select an answer.", fg="orange")

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    quiz_gui = QuizGUI(root)
    root.mainloop()
