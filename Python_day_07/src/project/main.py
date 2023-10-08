import json
from constants import *
from validator import Validator
from condition import PersonCondition


class VoightKampffTest:
    """
    A class for conducting Voight-Kampff test.
    
    Attributes
    __________
    filename : str
        the path to the test file
    validator: Validator
        Validator of input parameters.
    condition: PersonCondition
        Tracking and measuring the condition of the test subject.
    answer_result_list: list
        A list of answers entered by the user.
    
    """

    def __init__(self, filename):
        """
        Parameters
        ----------
        filename : str
            The path to the test file.
        """
        self.filename = filename
        self.validator = Validator(self.filename)
        self.condition = PersonCondition()
        self.answer_result_list = []

    def get_question_list(self) -> str:
        """
        Returns a list of questions from a file.
        
        Returns
        -------
        str
            List of the questions.
        """
        with open(self.filename) as file:
            return json.load(file)['Questions']

    def ask_question(self, question) -> None:
        """
        Displays a question to the user.
        """
        print(question['Question'])
        for count, answer in enumerate(question['Answers'], start=1):
            print(f"{count}) {answer['content']}")

    def get_answer(self, answers_list: list) -> str:
        """
        Gets the answer to the question from the user.
        
        Parameters
        ----------
        answers_list : list
            List of the answers.
        
        Returns
        -------
        int
            The value of the answer.
        """
        count_of_answers = len(answers_list)
        answer = input(f'{GET_ANSWER_TEXT} [1-{count_of_answers}]: ')
        while not self.validator.is_correct_answer(answer, count_of_answers):
            answer = input(f'{GET_ANSWER_TEXT} [1-{count_of_answers}]: ')
        return answers_list[int(answer) - 1]['res']
    
    def calculate_the_result(self, answers_result_list: list, condition_result_list: list) -> bool:
        """
        Outputs the test result.
        
        Parameters
        ----------
        answers_result_list : list
            List of the answers.
        condition_result_list: list
            List of condition values of person.
        
        Returns
        -------
        bool
            Result of the test.
        """
        for num, _ in enumerate(answers_result_list):
            if (
                int(condition_result_list[num]['respiration']) > 16 or
                int(condition_result_list[num]['heart_rate']) >= 85 or
                int(condition_result_list[num]['blushing_level']) >= 3 or
                int(condition_result_list[num]['pupillary_dilation']) >= 5
            ):
                answers_result_list[num] *= -1
            return answers_result_list.count(1) >= answers_result_list.count(-1)

    def run(self) -> bool:
        """
        Runs the test.
        
        Returns
        -------
        bool
            Result of the test.
        """
        if not self.validator.is_valided_file():
            return
        question_list = self.get_question_list()
        for question in question_list:
            self.ask_question(question)
            self.answer_result_list.append(self.get_answer(question['Answers']))
            self.condition.get_condition()
        return self.calculate_the_result(self.answer_result_list, self.condition.condition_list)
            

if __name__ == "__main__":
    test = VoightKampffTest('./files/questions.json')
    print(test.run())
