from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    q_text = q["text"]
    q_ans = q["answer"]
    question = Question(q_text, q_ans)
    question_bank.append(question)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    user_answer = quiz.next_question()
    quiz.check_answer(user_answer)