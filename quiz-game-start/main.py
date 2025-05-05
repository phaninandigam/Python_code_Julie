from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    question = Question(question_text, question_answer)
    question_bank.append(question)


# print(question_bank)
# print(question_bank[3].text)
# print(question_bank[3].answer)
# print("---------------------")
quizbrain=QuizBrain(question_bank)
for items in question_bank:
    quizbrain.next_question()


print("\n You have completed the Quiz")
print(f"Your final score is {quizbrain.score}/{quizbrain.question_number}")