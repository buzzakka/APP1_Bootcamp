import pytest
from sys import path
path.append('../')
from validator import Validator, is_correct_condition_parametr

@pytest.mark.parametrize("path", [
    ('none'),
    ("files_for_test/empty_file.json"),
    ("files_for_test/incorrect_file_1.json"),
    ("files_for_test/incorrect_file_2.json"),
    ("files_for_test/incorrect_file_3.json"),
    ("files_for_test/incorrect_file_4.json"),
    ("files_for_test/incorrect_file_5.json"),
    ("files_for_test/incorrect_file_6.json")
])
def test_validator_with_incorrect_file(path: str) -> None:
    """
    Testing validator.is_valided_file() function with incorrect files.

    Parameters
    ----------
    path : str
        Path to the file.
    """
    validator = Validator(path)
    assert not validator.is_valided_file()


def test_validator_with_correct_file() -> None:
    """
    Testing validator.is_valided_file() function with correct file.
    """
    validator = Validator('../files/questions.json')
    assert validator.is_valided_file()


@pytest.mark.parametrize("str_num, max_value", [("1", 3), ("3", 3)])
def test_validator_is_correct_answer_true(str_num: str, max_value: int) -> None:
    """
    Testing validator.is_correct_answer() function with correct answers.

    Parameters
    ----------
    str_num : str
        The user-entered answer to the test question.
    max_value: int
        The number of valid answers to the current question.
    """
    validator = Validator(path)
    assert validator.is_correct_answer(str_num, max_value)


@pytest.mark.parametrize("str_num, max_value", [
    ("0", 3), 
    ("4", 3), 
    ("-1", 3), 
    ("2.2", 3), 
    ("qwerty", 3), 
    ("", 3)])
def test_is_correct_answer_false(str_num, max_value):
    """
    Testing validator.is_correct_answer() function with incorrect answers.

    Parameters
    ----------
    str_num : str
        The user-entered answer to the test question.
    max_value: int
        The number of valid answers to the current question.
    """
    validator = Validator(path)
    assert not validator.is_correct_answer(str_num, max_value)


@pytest.mark.parametrize("str_num, min, max", [
    ("1", 1, 3),
    ("3", 1, 3)
])
def test_is_correct_condition_parametr_true(str_num, min, max):
    """
    Testing validator.is_correct_condition_parametr() function with correct answers.

    Parameters
    ----------
    str_num : str
        The value of the condition entered by the user.
    min : int
        The minimum allowed value of the parameter.
    max : int
        The maximum allowed value of the parameter.
    """
    assert is_correct_condition_parametr(str_num, min, max)


@pytest.mark.parametrize("str_num, min, max", [
    ("0", 1, 3), 
    ("4", 1, 3), 
    ("2.2", 1, 3), 
    ("qwerty", 1, 3), 
    ("", 1, 3)]
)
def test_is_correct_condition_parametr_false(str_num, min, max):
    """
    Testing validator.is_correct_condition_parametr() function with incorrect answers.

    Parameters
    ----------
    str_num : str
        The value of the condition entered by the user.
    min : int
        The minimum allowed value of the parameter.
    max : int
        The maximum allowed value of the parameter.
    """
    assert not is_correct_condition_parametr(str_num, min, max)
