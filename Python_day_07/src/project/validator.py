from constants import *
import os
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import json
from json.decoder import JSONDecodeError


class Validator():
    """
    A class used to validate the data in the test.
    
    Attributes
    __________
    filename : str
        the path to the test file
    """
    
    def __init__(self, filename: str):
        """
        Parameters
        ----------
        filename : str
            The path to the test file.
        """
        self.filename: str = filename
    
    def is_valided_file(self) -> bool:
        """
        The main validation function that determines whether a file is valid or not.
        
        Returns
        -------
        bool
            Is the file correct or not.
        """
        if not self.is_file_exists():
            print(FILE_NOT_FOUND_ERROR_TEXT)
            return False
        with open(self.filename) as file:
            try:
                json_data = json.load(file)
                if not self.is_correct_file_content(json_data):
                    print(JSON_DECODE_ERROR_TEXT)
                    return False
            except JSONDecodeError:
                print(JSON_DECODE_ERROR_TEXT)
                return False
        return True
    
    def is_file_exists(self) -> bool:
        """
        Determines whether the selected file exists or not.
        
        Returns
        -------
        bool
            Whether there is a file with the test.
        """
        return os.path.isfile(self.filename)

    def is_correct_file_content(self, fcontent: str) -> bool:
        """
        Checks whether the contents of the test file are correct.

        Parameters
        ----------
        fcontent : str
            The contents of the test file.
        
        Returns
        -------
        bool
            Whether the contents of the file are correct.
        """
        try:
            validate(instance=fcontent, schema=VALIDATORS_SCHEMA)
            return True
        except ValidationError:
            return False
    
    def is_correct_answer(self, answer: str, count_of_answers: int) -> bool:
        """
        Checks the value entered when answering the question for correctness.

        Parameters
        ----------
        answer : str
            The user-entered answer to the test question.
        count_of_answers : int
            The number of valid answers to the current question.
        
        Returns
        -------
        bool
            Whether the answer entered by the user is correct.
        """
        try:
            if int(answer) in list(range(1, count_of_answers + 1)):
                return True
            else:
                print(NOT_CORRECT_ANSWER)
        except ValueError:
            print(NOT_CORRECT_ANSWER)
        return False


    
def is_correct_condition_parametr(parametr: str, min_value: int, max_value: int) -> bool:
    """
    Checks whether the condition value entered by the user is correct.

    Parameters
    ----------
    parametr : str
        The value of the condition entered by the user.
    min_value : int
        The minimum allowed value of the parameter.
    max_value : int
        The maximum allowed value of the parameter.
    
    Returns
    -------
    bool
        Whether the condition parametr entered by the user is correct.
    """
    try:
        if int(parametr) in list(range(min_value, max_value + 1)):
            return True
        else:
            print(NOT_CORRECT_CONDITION_PARAMETR)
    except ValueError:
        print(NOT_CORRECT_CONDITION_PARAMETR)
    return False
