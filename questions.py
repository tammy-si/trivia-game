import requests

# holds the questions
class QuestionBank:
    def __init__(self):
        request = requests.get('https://opentdb.com/api.php?amount=10&type=multiple')
        results = request.json()['results']
        self.questions = []
        for question in results:
            print(question)
            new_question = Question(question)
            self.questions.append(new_question)

        for question in self.questions:
            print(question.question)
            print(question.answer)
            print(question.type)
            print(question.wrong_answers)

class Question:
    def __init__(self, question):
        self.question = question['question']
        self.answer = question['correct_answer']
        self.type = question['type']
        self.wrong_answers = question['incorrect_answers']

questionsBank = QuestionBank()