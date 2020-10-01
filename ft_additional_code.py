import ft_rev_bin_num as tss
import ft_bin_num as sss
import ft_reverse_code as rev


def ft_additional_code(a):
    r = str(rev.ft_reverse_code(a))
    n = r[1::]
    otv = r[0]
    po = str(sss.ft_bin_num(tss.ft_rev_bin_num(int(n)) + 1))
    if len(po) > 7:
        po = "0000000"
    if len(po) < 7:
        while len(po) != 7:
            po = "0" + po
    return otv + po
