class QuizBrain:
    def __init__(self,question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score =0

    def still_has_questions(self):
        total_question = len(self.question_list)
        while self.question_no < total_question:
            return True


    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f" Q.{self.question_no}:{current_question.text} Please Type your answer as True/False: ")
        self.correct_answer(user_answer,current_question.answer)


    def correct_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it right")

        else:
            print(f"You got it wrong")

        print(f"The correct answer is {correct_answer}")
        print(f"Your score is {self.score}/{self.question_no}")
        print("\n")