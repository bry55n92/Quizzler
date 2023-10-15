from quiz_brain import QuizBrain
from tkinter import *

THEME_COLOR = "#375362"
Q_FONT = ("Arial", 20, "italic")


class QuizInterface:
    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.quiz=quiz_brain
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some Text", fill=THEME_COLOR,
                                                     font=Q_FONT, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        true_pic = PhotoImage(file="images/true.png")
        false_pic = PhotoImage(file="images/false.png")
        self.true_button = Button(self.window, image=true_pic, command=self.quiz.true_answer)
        self.false_button =Button(self.window, image=false_pic, command=self.quiz.false_answer)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

