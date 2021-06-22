# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    index_of_a = []
    for index, c in enumerate(S):
        if c == 'a':
            index_of_a.append(index)

    num_a = len(index_of_a)
    if num_a % 3 != 0:
        # number of 'a' in S does not divide by 3
        return 0

    if num_a == 0:
        # S contains only 'b', so we need to return the number of
        # partitions of S into 3 sub-strings,:
        len_s = len(S)
        return (len_s - 1) * (len_s - 2) // 2

    num_a_in_substring = num_a // 3

    first_b_interval_start = index_of_a[num_a_in_substring - 1]
    first_b_interval_end = index_of_a[num_a_in_substring]
    len_first_b_interval = first_b_interval_end - first_b_interval_start

    second_b_interval_start = index_of_a[2 * num_a_in_substring - 1]
    second_b_interval_end = index_of_a[2 * num_a_in_substring]
    len_second_b_interval = second_b_interval_end - second_b_interval_start

    # number of ways to partition is the product of the lengths of the interval of 'b'
    # for example: in S = babbaba, first b interval is S[2]...S[3] and second b
    # interval is S[5]
    return len_first_b_interval * len_second_b_interval