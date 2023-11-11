class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print(f"Your are correct! {user_answer} is right answer.")
            self.score += 1
        else:
            print(f"Your are wrong! {user_answer} is wrong answer.")
            print(f"Right answer is {correct_answer}")
        print(f"Your current score is: {self.score} out of {self.question_number}")
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q. {self.question_number} {current_question.text} (True/False) : ")
        self.check_answer(user_answer, current_question.answer)
