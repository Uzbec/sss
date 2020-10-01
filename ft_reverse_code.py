import ft_straight_code as pr


def ft_reverse_code(a):
    p = str(pr.ft_straight_code(a))
    otv = p[0]
    if a > 0:
        return p
    for i in range(1, len(p)):
        if p[i] == "0":
            otv += "1"
        else:
            otv += "0"
    return otv
