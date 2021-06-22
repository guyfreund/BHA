from copy import deepcopy


def get_num_paths(points, start):
    if start == [1.0, 1.0]:
        return 1

    num_paths = 0

    for point in points:
        if point != start:
            if point[0] >= start[0] and point[1] >= start[1]:
                new_points = deepcopy(points)
                new_points.remove(point)
                num_paths += get_num_paths(points, point)

    return num_paths


def main():
    points = [[0.5, 0.5], [0.6, 0.7], [0.3, 0.9], [0.9, 0.4], [0.8, 0.8]]
    print(get_num_paths(points=points + [[1.0, 1.0]], start=[0.0, 0.0]) - 1)


if __name__ == "__main__":
    main()
