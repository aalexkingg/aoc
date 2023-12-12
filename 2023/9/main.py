
def func(lst):
    # Get differences = new list
    new_list = []
    for i in range(len(lst)-1):
        new_list.append(lst[i+1]-lst[i])

    # if all same
    if len(set(new_list)) == 1:
        next_num = new_list[0]
        return next_num
    else:
        temp_new = func(new_list)
        temp_new += new_list[-1]
        return temp_new

    #return new_list
        # add next
        # return new list
    # else
        #


with open("data.txt") as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        sequence = [int(i) for i in line.split(" ")]
        print(sequence)

        diff = func(sequence)
        new_num = sequence[-1] + diff
        print(new_num)
        #exit()
        total += new_num

print(total)