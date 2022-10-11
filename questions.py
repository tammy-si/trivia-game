import requests
import tkinter
from html import unescape
import random
import time

# actual question
class Question:
    def __init__(self, question):
        self.question = unescape(question['question'])
        self.answer = unescape(question['correct_answer'])
        self.type = unescape(question['type'])
        self.wrong_answers = unescape(question['incorrect_answers'])

# holds the questions
class QuestionBank:
    def __init__(self):
        request = requests.get('https://opentdb.com/api.php?amount=10&type=multiple')
        results = request.json()['results']
        self.questions = []
        self.question_num = -1
        for question in results:
            print(question)
            new_question = Question(question)
            self.questions.append(new_question)

        for question in self.questions:
            print(question.question)
            print(question.answer)
            print(question.type)
            print(question.wrong_answers)

    def get_current_question(self):
        self.question_num += 1
        return self.questions[self.question_num]

# quiz interface
class Interface:
    def __init__(self, questionsBank):
        self.window = tkinter.Tk()
        self.window.title("Trivia Game")
        self.window.minsize(height=400, width=500)
        self.window.resizable(False, False)
        self.all_questions = questionsBank
        
        self.question_box = tkinter.Label(self.window, text=questionsBank.questions[0].question, background='red')
        self.question_box.grid(columnspan=2)

        self.button1 = tkinter.Button(self.window, text='Button1')
        self.button2 = tkinter.Button(self.window, text='button2')
        self.button3 = tkinter.Button(self.window, text='button3')
        self.button4 = tkinter.Button(self.window, text='button4')
        self.button1.grid(row=1, column=0, padx=20, pady=20)
        self.button2.grid(row=1, column = 1, padx=20, pady=20)
        self.button3.grid(row=2, column=0, padx=20, pady=20)
        self.button4.grid(row=2, column=1, padx=20, pady=20)

        self.resultLabel = tkinter.Label(self.window, text='')
        self.resultLabel.grid(columnspan=2)

    def get_next_question(self):
        self.resultLabel.config(text=" ")
        current_question = self.all_questions.get_current_question()
        self.question_box.config(text=current_question.question)
        l = [self.button1, self.button2, self.button3, self.button4]
        # make the answer_button first
        answer_button = l.pop(random.randrange(len(l)))
        answer_button.config(text=current_question.answer, command= lambda: self.show_result(True))
        # now assign the wrong answers to the other buttons
        for i in range(len(l)):
            l[i].config(text=current_question.wrong_answers[i], command= lambda: self.show_result(False))

    def show_result(self, result):
        if result == True:
            self.resultLabel.config(text="Correct")
            self.get_next_question()
        else:
            self.resultLabel.config(text="Incorrect")
            self.get_next_question()

questionsBank = QuestionBank()
interface = Interface(questionsBank)
interface.get_next_question()

interface.window.mainloop()