FILE_NOT_FOUND_ERROR_TEXT = "The file with the tests was not found."
JSON_DECODE_ERROR_TEXT = "The test file is incorrect."
KEY_ERROR_TEXT = "The construction of the JSON file with the test is incorrect."

GET_ANSWER_TEXT = "Enter an integer number"
NOT_CORRECT_ANSWER = "Please enter a valid integer number."

GET_RESPIRATION_TEXT = "Please, enter resperation (measured in BPM, normally around 12-16 breaths per minute): "
RESPERATION_MIN = 0
RESPERATION_MAX = 100

GET_HEART_RATE_TEXT = "Please, enter heart rate (normally around 60 to 100 beats per minute): "
HEART_RATE_MIN = 0
HEART_RATE_MAX = 200

GET_BLUSHING_LEVEL_TEXT = "Please, enter blushing level (categorical, 6 possible levels): "
BLUSHING_LEVEL_MIN = 0
BLUSHING_LEVEL_MAX = 6

GET_PUPILLARY_DILATION_TEXT = "Please, enter pupillary dilation (current pupil size, 2 to 8 mm): "
PUPILLARY_DILATION_MIN = 2
PUPILLARY_DILATION_MAX = 8

NOT_CORRECT_CONDITION_PARAMETR = "The number entered is incorrect. Please enter the correct value."

VALIDATORS_SCHEMA = {
    "type": "object",
    "required": [
        "Questions"
    ],
    "properties": {
        "Questions": {
            "type": "array",
            "items": {
                "type": "object",
                "required": [
                    "Question",
                    "Answers"
                ],
                "properties": {
                    "Question": {"type": "string"},
                    "Answers": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": [
                                "content",
                                "res"
                            ],
                            "properties": {
                                "content": {"type": "string"},
                                "res": {"type": "integer"}
                            }
                        }
                    }
                }
            }
        }
    }
}
