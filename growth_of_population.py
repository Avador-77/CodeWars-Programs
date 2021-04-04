def nb_year(p0, percent, aug, p):
    
    checking = 0
    count = 0
    active = True
    while active:
        if checking < p:
            checking = int(p0 + (p0 * (percent/100)) + aug)
            count += 1
            p0 = checking
        else:
            active = False
    print("years = ", count)
        
nb_year(1000, 2.0, 50, 1214)