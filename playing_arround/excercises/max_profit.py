def max_profit_one_buy_one_sell(A):
    if len(A) < 2:
        return 0, (0, 0)

    local_minimum = A[0]
    local_minimum_index = 0
    max_profit = A[1] - A[0]
    max_profit_index = 1

    for index, n in enumerate(A):
        if n < local_minimum:
            local_minimum = n
            local_minimum_index = index
        if (current_profit := n - local_minimum) > max_profit:
            max_profit = current_profit
            max_profit_index = index

    return max_profit, (local_minimum_index, max_profit_index)


def max_profit_unlimited(A):
    max_profit = 0

    for i in range(0, len(A) - 1):
        if (temp_profit := A[i + 1] - A[i]) > 0:
            max_profit += temp_profit

    return max_profit


def main():
    A = [9, 2, 1, 4, 3, 8, 9, 5]
    B = [1, 7, 2, 3, 6, 7, 6, 7]
    print(max_profit_one_buy_one_sell(A))
    print(max_profit_unlimited(B))


if __name__ == '__main__':
    main()
