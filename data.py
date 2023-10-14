import requests


parameters= {
    "amount": 10,
    "type": "boolean",
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
questions = data["results"]



question_data = []
for num in range(0, len(questions)):
    question = questions[num]["question"]
    answer = questions[num]["correct_answer"]
    d={"question": question, "answer": answer}
    question_data.append(d)



