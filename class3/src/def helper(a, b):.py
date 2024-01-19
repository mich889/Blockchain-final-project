def helper(a, b):
    if a == 0:
        return 0
    if a % 2 == 0:
        return helper(a//2, b*2)+b
    else:
        return helper(a//2, b*2)-b


print(helper(20, 1))
