def get_num_sequence(end_num: int) -> str:
    """Returns string of nums starting from 1 to end_num
    each number will be multiplied by its value
    for example: get_num_sequence(3)
    will return '122333'
    """
    if end_num < 1:
        return ""
    result = map(lambda cur_num: str(cur_num) * cur_num, range(1, end_num + 1))
    return "".join(result)
