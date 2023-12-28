from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from trivia_questions import question_data_trivia

# creating a question bank from a dictionary in question_data
ques_text = ""
ques_answer = ""
question_bank = []
for question in question_data_trivia:
    ques_text = question["question"]
    ques_answer = question["correct_answer"]
    new_question = Question(ques_text, ques_answer)
    question_bank.append(new_question)

print(len(question_bank))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():

    quiz.next_question()
print(f"You have completed the quiz \n Your final score is {quiz.score}/{quiz.question_no}" )









