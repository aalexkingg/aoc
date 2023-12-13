

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



