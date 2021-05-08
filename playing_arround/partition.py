from functools import reduce


def get_all_partitions(n):
    partitions = [[n]]

    for smaller_number in range(1, n):
        for partition in get_all_partitions(n - smaller_number):
            partition.append(smaller_number)
            partition = sorted(partition)
            if partition not in partitions:
                partitions.append(partition)

    return partitions


def get_partition_max(partitions):
    return max(reduce(lambda x, y: x * y, partition) for partition in partitions)


def main():
    n = 8
    partitions = sorted(get_all_partitions(n), key=lambda l: len(l))
    for partition in partitions:
        print(', '.join(str(number) for number in partition))
    print(get_partition_max(partitions))


if __name__ == "__main__":
    main()
