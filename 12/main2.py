def base_convert(i, b):
    result = []
    while i > 0:
            result.insert(0, i % b)
            i = i // b
    return result


total = 0
# remove double dots from file
with open("data.txt") as file:
    for i, line in enumerate(file.readlines()):
        chars = line.split(" ")[0]
        chars = chars + "?"

        nums = list(line.split(" ")[1].split(","))
        nums[-1] = nums[-1].strip("\n")
        #nums = nums * 3

        if chars[0] == ".":
            chars = chars[1:]

        if chars[-1] == ".":
            chars = chars[:-1]

        # build string from nums
        build = ".".join(["#"*int(num) for num in nums])

        new_chars = chars.replace("?", "#")

        chars_list = chars.split(".")
        new_chars_list = new_chars.split(".")
        build_list = build.split(".")

        new_chars = ".".join(chars_list)
        new_build = ".".join(build_list)
        dof = len(new_chars) - len(new_build)
        base = dof + 1
        hashes = len(build_list)
        count_to = dof * (dof+1) ** hashes

        counter = 0

        print(i, new_chars, " -> ", new_build)

        if len(new_build) == 0:
            counter = 1

        for j in range(dof, count_to+1):
            result = base_convert(j, base)
            if sum(result) == dof:
                while len(result) <= hashes:
                    result.insert(0, 0)

                for l in range(1, len(result)-1):
                    result[l] += 1

                final_build = ""
                for k, hash in enumerate(build_list):
                    final_build += "."*result[k] + hash
                final_build += "."*result[-1]

                passed = True
                for c in range(len(final_build)):
                    if final_build[c] == "#" and new_chars[c] == ".":
                        passed = False
                    elif final_build[c] == "." and new_chars[c] == "#":
                        passed = False

                if passed:
                    counter += 1


                #print(passed, final_build)
        print(counter, "\n")
        total += counter
print(total)

