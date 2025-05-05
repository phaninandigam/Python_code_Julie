class QuizBrain:
    def __init__(self, question_list):
        self.question_number=0
        self.question_list=question_list
        self.score=0


    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1 # we could have done this below the answer line,
        # but in the output we will get it as Q 0 which is not right
        answer =  input(f"\nQ.{self.question_number} : {current_question.text} (True/False):")
        self.check_answer(answer,current_question.answer)

    def check_answer(self, user_answer, actual_answer):
        if user_answer.lower() == actual_answer.lower():
            print("You're Right!!")
            self.score+=1
        else:
            print("Wrong Answer!!")
        print(f"The right answer is {actual_answer}")
        print(f"Your correct score is : {self.score}/{self.question_number}")


