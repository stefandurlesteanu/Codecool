def count_negative(numbers):
    '''
    Count how many numbers in the given sequence are negative.

    >>> count_negative([])
    0
    >>> count_negative([1, 2, 3])
    0
    >>> count_negative([-1, -2, -3])
    3
    >>> count_negative([10, -10, -10, 10, 10, -20, -30, 0])
    4
    '''

    counter = 0
    for i in numbers:
        if i < 0:
            counter += 1
    return counter


