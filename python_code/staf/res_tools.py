def add_to_answer(answer: dict, values: list) -> dict:
    for value in values:
        answer.update({value[0]: value[1]})
    return answer


def cleanup_answer(answer: dict, values: list) -> dict:
    for value in values:
        answer.pop(value, None)
    return answer
