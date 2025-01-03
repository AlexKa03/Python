class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        total_questions = len(self.question_list)
        return total_questions > self.question_number

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.text} (True/ False)")
        self.check_answer(answer, question.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("You are right!")
        else:
            print("That is wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your score is: {self.score}/{self.question_number}")

