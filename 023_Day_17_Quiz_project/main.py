from question_model import Question
from data import get_questions
from quiz_brain import QuizBrain

question_bank = []
question_data = get_questions()

for q in question_data:
    q_text = q["question"]
    q_ans = q["correct_answer"]
    question = Question(q_text, q_ans)
    question_bank.append(question)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    user_answer = quiz.next_question()
    quiz.check_answer(user_answer)

print("You have completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")