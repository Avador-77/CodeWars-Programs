def filter_list(l):
    res = []
    for s in l:
        if isinstance(s, int):
            res.append(s)
    return res