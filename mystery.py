def mystery(num):
    if num == 10:
        num = num * 10
    elif num == 30:
        num = num * 30
    else:
        num = num
    return num

num = 10 * 3
print( mystery(num) )
