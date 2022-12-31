class QuizBrain:
    def __init__(self, q_list : list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self) -> bool:
        """Checks whether any more questions left. | Return boolean."""
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        """Print current question and asks user for answer. | Return string."""
        curr_question = self.question_list[self.question_number]
        self.question_number += 1
        user_screen = f"Q.{self.question_number}: {curr_question.text} (True/False)?: "
        user_ans = input(user_screen)
        return user_ans

    def check_answer(self, user_answer) -> None:
        """Check for correct answer. Print relevent messages and current score. | Return None."""
        correct_answer = self.question_list[self.question_number-1]
        if user_answer.lower() == correct_answer.answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The right answer is {correct_answer.answer}")
        print(f"Your score: {self.score}/{self.question_number}\n")


        