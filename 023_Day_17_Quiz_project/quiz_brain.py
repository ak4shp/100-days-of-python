class QuizBrain:
    def __init__(self, q_list : list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number += 1
        user_screen = f"Q.{self.question_number}: {curr_question.text} (True/False)?: "
        user_ans = input(user_screen)
        return user_ans

    def check_answer(self, user_answer):
        correct_answer = self.question_list[self.question_number-1]
       
        if user_answer == correct_answer.answer:
            self.score += 1
        print(self.score)

        