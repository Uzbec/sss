def ft_straight_code(a):
    if a > 0:
        b = ''
        while a > 0:
            c = str(a % 2)
            b = c + b
            a = int(a / 2)
        while len(b) != 8:
            b = '0' + b
        return b
    else:
        a = -a
        n = ''
        while a > 0:
            c = str(a % 2)
            n = c + n
            a = int(a / 2)
        while len(n) != 7:
            n = '0' + n
        n = '1' + n
        return n
