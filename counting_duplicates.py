def duplicate_count(text):
    d = dict()
    for s in list(text):
        if isinstance(s, str):
            s = s.lower()
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1
        else:
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1
    count = 0
    for value in d.values():
        if value >= 2:
            count += 1
    return count