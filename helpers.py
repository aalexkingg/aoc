
def base_convert(num, base) -> list[int]:
    """
    Converts num to base number.
    :param num: Number to convert
    :param base: Base of conversion
    :return:
    """
    _result = []
    while num > 0:
        _result.insert(0, num % base)
        num = num // base
    return _result


def get_column(arr, idx, col) -> str:
    """
    Constructs column of 2D array.
    :param arr: 2D array
    :param idx: 1st index of 2D array
    :param col: Column to construct
    :return:
    """
    if col < 0:
        raise IndexError

    return "".join([bl[col] for bl in arr[idx]])


def find_differences(str1, str2) -> int:
    """
    Find number of differences between two strings
    :param str1: String 1
    :param str2: String 2
    :return:
    """
    if len(str1) != len(str2):
        raise IndexError

    return sum([1 if str1[d] != str2[d] else 0 for d in range(len(str1))])
