def add_binary(a,b):
    sum = a + b
    active = True
    l1 = []
    while active:
        binry = sum % 2
        sum //= 2
        if sum != 0:
            l1.append(binry)
        else:
            l1.append(binry)
            active = False

    l2 = [str(nums) for nums in l1]
    return "".join(l2)

        
    

print(add_binary(7,8))
#add_binary(7,8)