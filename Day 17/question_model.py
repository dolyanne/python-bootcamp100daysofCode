# Modeling  a question and answer class
# Authored by dolyanne
# creating a question class


class Question:
    # creating a constructor class to initialize the objects attributes, text and answers
    def __init__(self, ques_text, ques_answer):
        self.text = ques_text
        self.answer = ques_answer


# question = input("what is the developers name?")
#
#
# new_question = Question(question, "dolyanne")


