import ft_rev_bin_num as tss
import ft_bin_num as sss
import ft_reverse_code as rev


def ft_additional_code(a):
    r = str(rev.ft_reverse_code(a))
    n = int(r) % 10000000
    otv = r[0]
    return otv + str(sss.ft_bin_num(tss.ft_rev_bin_num(n) + 1))
