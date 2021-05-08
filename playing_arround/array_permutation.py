import random


def swap(array, i, j):
    a_i = array[i]
    a_j = array[j]
    array[i] = a_j
    array[j] = a_i


def get_random(k):
    return random.randint(1, k)


def get_randomized_array_permutation(array):
    n = len(array)
    randomized_array_permutation = array

    for k in range(n, 0, -1):
        index = k - 1
        random_index = get_random(k) - 1
        swap(randomized_array_permutation, index, random_index)

    return randomized_array_permutation


def main():
    n = 10
    array = [x for x in range(1, n + 1)]
    randomized_array_permutation = get_randomized_array_permutation(array)
    print(randomized_array_permutation)


if __name__ == "__main__":
    main()
