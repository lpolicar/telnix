import string
d_map = string.digits + string.ascii_uppercase


def int_to_base_i(n, base): # this function works too
    if n == 0:
        return [str(n)]
    out = []
    while n:
        n, mod = divmod(n, base)
        try:
            ch = d_map[mod]
        except:
            ch = str(mod)
        out.append(ch)
    out.reverse()
    return out


def int_to_base(n, base):
    if n == 0:
        return [str(n)]

    def _int_to_base(n, out=[]):
        if n == 0:
            return out
        n, mod = divmod(n, base)
        _int_to_base(n)
        try:
            ch = d_map[mod]
        except:
            ch = str(mod)
        out.append(ch)
        return out

    return _int_to_base(n)


def get_palindromic_min_base(n):
    MAX_BASE = 1000
    for base in range(2, MAX_BASE):
        based_n = int_to_base(n, base)  # int_to_base_i(n, base)
        # print("trace:", n, "to base", base, "-->", based_n)
        based_n_copy = based_n.copy()
        based_n_copy.reverse()
        if based_n_copy == based_n:
            return base
    else:
        return 0  # unable to get the palindromic base, the given max base is short


if __name__ == "__main__":
    for i in range(1, 1001):
        base = get_palindromic_min_base(i)
        if base:
            print("%s, %s" % (i, base))
        else:
            print("Error: missing base for:", i)



