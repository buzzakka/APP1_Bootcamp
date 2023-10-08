from constants import *
from validator import is_correct_condition_parametr


class PersonCondition:
    """
    A class for tracking and measuring the condition of the test subject.

    Attributes
    __________
    condition_list : list
        List of states of the test subject. After each passing of the status survey, the result will be entered in this list.
    """

    def __init__(self):
        self.condition_list = []

    def get_condition(self) -> None:
        """
        Creates a dictionary with state parameters and writes it to self.condition_list.
        """
        condition = {
            "respiration": self.get_condition_parametr(GET_RESPIRATION_TEXT, RESPERATION_MIN, RESPERATION_MAX),
            "heart_rate": self.get_condition_parametr(GET_HEART_RATE_TEXT, HEART_RATE_MIN, HEART_RATE_MAX),
            "blushing_level": self.get_condition_parametr(GET_BLUSHING_LEVEL_TEXT, BLUSHING_LEVEL_MIN, BLUSHING_LEVEL_MAX),
            "pupillary_dilation": self.get_condition_parametr(GET_PUPILLARY_DILATION_TEXT, PUPILLARY_DILATION_MIN, PUPILLARY_DILATION_MAX)
        }
        self.condition_list.append(condition)

    def get_condition_parametr(self, input_text: str, min_value: int, max_value: int) -> str:
        """
        Allows the user to enter the value of the current state.

        Parameters
        ----------
        input_text : str
            The value entered by the user.
        min_value : int
            The minimum value of the parameter.
        max_value : int
            The maximum value of the parameter.
        
        Returns
        -------
        str
            The value of the condition parametr.
        """
        parametr = input(input_text)
        while not is_correct_condition_parametr(parametr, min_value, max_value):
            parametr = input(input_text)
        return parametr
