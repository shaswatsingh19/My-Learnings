def hillorvalley(seq):
    is_dec, is_inc = False, False
    inflections = 0
    for i in range(len(seq)-1):
        if inflections > 1:
            # Early stop if more than 1 inflection
            return False
        right = seq[i+1]
        middle = seq[i]
        diff = right - middle
        if diff > 0:
            if is_dec:
                inflections += 1
            is_inc = True
            is_dec = False
        elif diff < 0:
            if is_inc:
                inflections += 1
            is_dec = True
            is_inc = False
    if inflections == 1:
        return True
    return False
