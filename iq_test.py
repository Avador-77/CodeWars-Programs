def iq_test(numbers):
    numbers = numbers.split()
    ind = 1
    even_d = dict()
    odd_d = dict()
    for i in numbers:
        if int(i) % 2 == 0:
            even_d[ind] = i
            ind += 1
        else:
            odd_d[ind] = i
            ind += 1

    if len(even_d) == 1:
        for key in even_d:
            return key
    else:
        for key in odd_d:
            return key