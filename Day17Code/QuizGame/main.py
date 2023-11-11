from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    i_text = i["text"]
    i_answer = i["answer"]
    new_question = Question(i_text, i_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print("congrats!! you have completed the quiz")
print(f"Your final score is: {quiz.score} out of {len(question_bank)}")