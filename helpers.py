import functools


if __name__ == "__main__":
    exit()


def base_convert(num, base, size=0) -> list[int]:
    """
    Converts num to base number.
    :param num: Number to convert
    :param base: Base of conversion
    :param size: size of returned list
    :return:
    """
    _result = []
    while num > 0:
        _result.insert(0, num % base)
        num = num // base
    if len(_result) < size and size:
        [_result.insert(0, 0) for _ in range(size-len(_result))]
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


def insert_column(arr, col, val):
    """
    Insert column into array
    :param arr:
    :param col:
    :param val:
    :return:
    """
    if 0 < len(arr.shape) < 3:
        # for 1d array
        for i in range(len(arr)):
            temp = str(arr[i])
            temp = temp[:col] + str(val) + temp[col+1:]
            arr[i] = temp
    else:
        raise "Array has too many dimensions"


def transpose(arr):
    """
    Returns the transpose (flip) of an array
    :param arr:
    :return:
    """
    return list(map("".join, zip(*arr)))


def rotate90a(arr):
    rows = len(arr)
    cols = len(arr[0])
    new_arr = []
    for c in range(cols-1, -1, -1):
        temp = ""
        for r in arr:
            temp += r[c]
        new_arr.append(temp)
    return new_arr


def rotate90c(arr):
    rows = len(arr)
    cols = len(arr[0])
    new_arr = []
    for c in range(cols):
        temp = ""
        for r in arr:
            temp = r[c] + temp
        new_arr.append(temp)
    return new_arr


def str_to_int(arr):
    """
    Converts list of strings to list of ints
    :param arr:
    :return:
    """
    if len(arr.asarray.shape) == 1:
        # 1d array
        return list(map(int, arr))
    elif len(arr.asarray.shape) == 2:
        # 2d array
        temp = []
        for i in range(len(arr)):
            temp.append(list(map(int, arr[i])))
        return temp
    else:
        raise "Array dimensions too large."


x, y = 0, 0
# up, down, left, right
for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    for distance in range(1, 4):
        nx = x + dx * distance
        ny = y + dy * distance


@functools.lru_cache(maxsize=None)
def t(): pass
