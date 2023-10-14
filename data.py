import requests
import pprint

questions = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean").json()
questions = questions["results"]

question_data = {}
for num in range(0, len(questions)):
    question = questions[num]["question"]
    answer = questions[num]["correct_answer"]
    question_data["question"] = question
    question_data["correct_answer"] = answer
pprint.pprint(questions)
pprint.pprint(question_data)
print(len(questions))