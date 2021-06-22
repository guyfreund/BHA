def num_ways(n):
    if n in (0, 1):
        return 1

    return num_ways(n - 2) + num_ways(n - 1)


def main():
    n = 5
    print(num_ways(n))


if __name__ == "__main__":
    main()
