def solution(S, L):
    s_map, l_map = {}, {}

    for item in S:
        if item in s_map:
            s_map[item] += 1
        else:
            s_map[item] = 1

    for item in L:
        if item in l_map:
            l_map[item] += 1
        else:
            l_map[item] = 1

    for k, v in s_map.items():
        if k not in l_map:
            return False
        if l_map[k] < v:
            return False

    return True


def main():
    S = [1, 2, 3]
    L = [6, 5, 4, 3, 2, 1]

    print(solution(S, L))


if __name__ == '__main__':
    main()
