import functools


@functools.lru_cache(maxsize=None)  # Caches variables to speed up result
def solve(springs, nums):
    if springs == "":
        # if string is empty, only add to total if also no more nums left
        return 1 if not len(nums) else 0

    if not len(nums):
        # if no more numbers left, but a # is still in the string, then not valid possibility
        return 0 if "#" in springs else 1

    # Here the two cases of the ? being a # or . are handled
    result = 0
    if springs[0] in ".?":
        # if first char is . or ?, then treat ? as . as first case for ?
        # number of first occurrences where first char is operational spring, remove first spring and check rest of string
        result += solve(springs[1:], nums)

    if springs[0] in "#?":
        # in second case, if char is # or ?, treat ? as #
        # if valid:
        # there must be enough springs left, num <= springs, aka if spring of length 3 left, but only 2 chars left in string, then not valid
        # there must be no .'s in the first num springs
        # there are no springs left OR if there are springs left it must not be a #
        if (nums[0] <= len(springs) and
                "." not in springs[:nums[0]] and
                (nums[0] == len(springs) or springs[nums[0]] != "#")):
            #
            result += solve(springs[nums[0] + 1:], nums[1:])

    return result


total = 0
with open("data.txt") as file:
    for line in file.readlines():
        # part 1
        # s = line.split(" ")[0]
        # n = tuple(int(x) for x in line.split(" ")[1].split(","))

        # part 2
        s = "?".join([line.split(" ")[0]]*5)
        n = tuple(int(x) for x in line.split(" ")[1].split(","))*5

        total += solve(s, n)
    print(total)
