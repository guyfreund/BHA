# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(A):
    # write your code in Python 3.6
    max_alternating_slice_so_far = 0
    max_alternating_slice_ending_here = 0
    last_sign = -1

    for number in A:
        if number == 0:
            number_sign = last_sign * -1
        else:
            number_sign = -1 if number < 0 else 1

        if number_sign != last_sign:
            max_alternating_slice_ending_here += 1
            if max_alternating_slice_so_far < max_alternating_slice_ending_here:
                max_alternating_slice_so_far = max_alternating_slice_ending_here
        else:
            max_alternating_slice_ending_here = 1

        last_sign = number_sign

    return max_alternating_slice_so_far


if __name__ == "__main__":
    A = [5, 4, -3, 2, 0, 1, -1, 0, 2, -3, 4, -5]
    print(solution(A))