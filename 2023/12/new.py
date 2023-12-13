import functools


def solve(perms, add):
    if add > -1:
        perms = perms + [add]
    dof_used = sum(perms)
    if len(perms) < dots-1:
        for i in range(dof - dof_used + 1):
            #global passed
            passed = solve(perms, i)
    else:
        perms = perms + [dof - dof_used]
        # evaluate
        print(perms)

        #passed += 1
        return None


dof = 20
hashes = 25
dots = hashes + 1
passed = 0


t = solve([], -1)
