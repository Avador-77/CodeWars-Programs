from math import pow as pw

def findNb(user):
    i = 1
    sum = 0
    active = True
    while active:
        if sum < user:
            sum += pw(i,3)
            num = i
            i += 1
            if sum == user:
                active = False
                return num
        else:
            active = False
            return -1

print(findNb(4183059834009))    


#the above code is lenghty and can get shorter:

'''def find_nb(m):
    n = 1
    volume = 0
    while volume < m:
        volume += n ** 3
        if volume == m:
            return n
        n += 1
    return -1
'''
