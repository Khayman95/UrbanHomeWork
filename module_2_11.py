my_list = [42,69,322,13,0,99,-5,9,8,7,-6,5]
a = len(my_list)
b = 0
while b <= a:

    c = my_list[b]
    if c >= 0:
        b = b+1
    else:
        break
    print(c)