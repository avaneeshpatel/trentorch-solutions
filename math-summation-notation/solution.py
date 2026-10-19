def summation(f, lo, hi):
    """
    f:  a function taking a single integer and returning a number
    lo: the starting index (inclusive)
    hi: the ending index (inclusive)

    Returns:
        Sum_{i=lo}^{hi} f(i), the sum of f(i) for every integer i from
        lo to hi, both ends included. If hi < lo, the sum is empty (0).
    """
    # TODO: Implement the summation from Theory as an explicit loop.
    sum_integers = 0
    # we need inclusive "hi" that's why - "for" loop stop condition run throughs lo to hi+1
    for i in range(lo,hi+1):
        sum_integers +=  f(i)
    return sum_integers
