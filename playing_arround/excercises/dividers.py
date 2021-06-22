def get_all_dividers(n):
    if n == 1:
        return [[1]]

    dividers = [[n]]

    for i in range(2, n):
        if n % i == 0:
            for divider in get_all_dividers(int(n / i)):
                divider.append(i)
                divider = sorted(divider)
                if divider not in dividers:
                    dividers.append(divider)

    return dividers


def main():
    n = 18
    dividers = sorted(get_all_dividers(n), key=lambda l: len(l))
    for divider in dividers:
        print(', '.join(str(number) for number in divider))


if __name__ == "__main__":
    main()
