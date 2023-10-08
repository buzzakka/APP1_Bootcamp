import pytest
from sys import path
path.append('../')
from main import VoightKampffTest


@pytest.mark.parametrize("answers_result_list, condition_result_list, result", [
    ([-1], [{'respiration': 12, 'heart_rate': 84, 'blushing_level': 2, 'pupillary_dilation': 4}], False),
    ([1], [{'respiration': 12, 'heart_rate': 84, 'blushing_level': 2, 'pupillary_dilation': 4}], True),
    ([1], [{'respiration': 17, 'heart_rate': 84, 'blushing_level': 2, 'pupillary_dilation': 4}], False),
    ([1], [{'respiration': 12, 'heart_rate': 85, 'blushing_level': 2, 'pupillary_dilation': 4}], False),
    ([1], [{'respiration': 12, 'heart_rate': 84, 'blushing_level': 3, 'pupillary_dilation': 4}], False),
    ([1], [{'respiration': 12, 'heart_rate': 84, 'blushing_level': 2, 'pupillary_dilation': 5}], False)
])
def test_calculate_the_result(answers_result_list: list, condition_result_list: list, result: bool) -> None:
    """
    Testing test.calculate_the_result() function.

    Parameters
    ----------
    answers_result_list : list
        List of answers to the test.
    condition_result_list : list
        List of conditions of the test subject.
    result : bool
        Result of test.
    """
    test = VoightKampffTest('../files/questions.json')
    assert test.calculate_the_result(answers_result_list, condition_result_list) is result
    