from question_model import Question
from data import question_data

question_bank = []

for q in question_data:
    q_text = q["text"]
    q_ans = q["answer"]
    question = Question(q_text, q_ans)
    question_bank.append(question)

    