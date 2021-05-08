def solution(A):
    max_ending_here = 1
    max_so_far = 1

    for n in A:
        if (temp := max_ending_here * n) > max_so_far:
            max_ending_here, max_so_far = temp, temp
        else:
            max_ending_here = n

    return max_so_far


def main():
    A = [1, 2, 3, 0.5, 2, 4, 5]
    print(solution(A))


if __name__ == '__main__':
    main()