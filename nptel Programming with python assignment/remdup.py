def remdup(l):
    res = []
    for i in l:
        if i  not in res:
            res.append(i)
    return res
