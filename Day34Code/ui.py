from tkinter import *
from quiz_brain import QuizBrain
import tkinter.messagebox

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brian: QuizBrain):
        self.quiz = quiz_brian
        self.window = Tk()
        self.window.title = "Quizzer"
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(height=250, width=300)
        self.canvas_word = self.canvas.create_text(150, 125, text="Question",
                                                   font=("Arial", 18, "italic"), width=250, fill=THEME_COLOR)
        self.canvas.config(bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, font=("Arial", 11, "normal"), fg="white")
        self.score.grid(row=0, column=1, pady=20)

        self.right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0, command=self.check_answer_true)
        self.right_button.grid(row=2, column=0, pady=20)

        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0, command=self.check_answer_false)
        self.wrong_button.grid(row=2, column=1, pady=20)


        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.canvas_word, text=q_text)

    def check_answer_true(self):
        user_answer = "True"
        self.score.config(text=f"Score:{self.quiz.check_answer(user_answer)}/ {self.quiz.question_number}")
        self.check_prompt()

    def check_answer_false(self):
        user_answer = "False"
        self.score.config(text=f"Score:{self.quiz.check_answer(user_answer)}/ {self.quiz.question_number}")
        self.check_prompt()

    def check_prompt(self):
        print(f"{len(self.quiz.question_list)}/{(self.quiz.question_number)}")
        if not(self.quiz.still_has_questions()):
            print(f"{self.quiz.question_list}/{self.quiz.question_number}")
            tkinter.messagebox.showinfo(title=None, message=f"your score was: {self.score.cget("text")}")
            choice = tkinter.messagebox.askquestion('Exit Application',
                                                         'Do you really want to exit \'Yes\' or Restart the Game \'No\'?')
            if choice == 'yes':
                self.window.destroy()
            else:
                tkinter.messagebox.showinfo('Return', 'Returning to main application')
        else:
            pass