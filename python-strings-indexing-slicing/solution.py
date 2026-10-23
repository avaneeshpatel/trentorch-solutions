def first_and_last(s: str) -> str:
    """
    Return a new string made of the first character of `s`
    followed by the last character of `s`.

    - If `s` is empty, return "".
    - If `s` has exactly one character, return that character twice.

    Example: first_and_last("python") -> "pn"
    """
    if s == "":
        return s
    return s[0]+s[-1]


def reverse_string(s: str) -> str:
    """
    Return a new string containing the characters of `s` in
    reverse order. Use a slice with a negative step.

    Example: reverse_string("python") -> "nohtyp"
    """
    current_index = -1
    count = 0
    res = ''
    while count < len(s) :
        res += s[current_index]
        count += 1
        current_index -= 1
    return res
    


def every_kth_from(s: str, start: int, k: int) -> str:
    """
    Return the characters of `s` at positions start, start + k,
    start + 2k, ... continuing to the end of the string.
    `start` may be negative (counted from the end). `k` is
    always >= 1. If `start` is out of range, return "".

    Example: every_kth_from("abcdefgh", 1, 3) -> "beh"
    """

    
    res = ''
    current_index = start
    while True:
        if start < 0:
            if current_index > -1:
                return res
        else:
            if current_index >= len(s):
                return res
        res += s[current_index]
        current_index += k
    return res
