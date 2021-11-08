"""
    reverse a string
"""


def rev_str1(s):
    return s[::-1]


def rev_str2(s):
    ret_str = ''
    i = len(s) - 1
    while i >= 0:
        ret_str += s[i]
        i -= 1
    return ret_str


def rev_str3(s):
    l = list(s)
    l = l[::-1]
    ret_str = ''
    for e in l:
        ret_str += e
    return ret_str


def rev_str4(s):
    l = list(s)
    ret_str = ''
    i = len(l) - 1
    while i >= 0:
        ret_str += l[i]
        i -= 1
    return ret_str


s = '1234567890'
print(rev_str1(s))
print(rev_str2(s))
print(rev_str3(s))
print(rev_str4(s))

