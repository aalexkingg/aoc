


def solve(perms):
    perms = perms + [add]
    print(perms)
    dof_used = sum(perms)
    if len(perms) < dots-1:
        for i in range(dof - dof_used + 1):

            global passed
            passed = solve(perms, i)
    else:
        perms.append(dof - dof_used)
        # evaluate
        print(perms)

        passed += 1
        return passed


dof = 3
hashes = 2
dots = hashes + 1
passed = 0

solve([], 0)
