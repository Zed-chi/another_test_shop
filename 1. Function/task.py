import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="Программа выводит последовательность цифр,\
            при этом количество каждой цифры равно ее значению.\
            При аргументе 3 результат будет => 122333."
    )
    parser.add_argument(
        "-n",
        dest="number",
        type=int,
        default=1,
        help="Введите последнюю цифру последовательности от 1.. \
            которую хотите вывести на экран.\
            По-умолчанию 1",
    )
    return parser.parse_args()


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


def main():
    args = get_args()
    seq = get_num_sequence(args.number)
    print(seq)


if __name__ == "__main__":
    main()
