import random


def det(matrix):
    if len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    sum = 0
    for num in range(len(matrix[0])):
        small_matrix = [[matrix[i][j] for j in range(len(matrix)) if j != num] for i in range(1, len(matrix))]
        sign = (-1) ** num
        sum += (sign * (matrix[0][num]) * det(small_matrix))

    return sum


def build():
    return [[random.randint(1, 100) for i in range(10)] for i in range(10)]


# matrix = [[-2, 1, 1, 3],
#           [1, 3, 1, -1],
#           [2, 4, 1, 0],
#           [1, 3, -1, 1]]


matrix = [[44, 79, 21, 35, 18, 96, 82, 57, 3, 15], [52, 83, 87, 95, 57, 79, 41, 79, 11, 16], [54, 100, 61, 15, 28, 90, 36, 100, 53, 94], [91, 84, 79, 56, 41, 70, 49, 36, 40, 45], [34, 31, 52, 3, 10, 54, 82, 95, 17, 43], [10, 44, 33, 64, 39, 75, 8, 47, 28, 47], [30, 64, 73, 7, 75, 39, 1, 79, 71, 80], [90, 63, 13, 48, 66, 53, 12, 8, 16, 58], [2, 95, 33, 75, 30, 72, 98, 14, 75, 56], [70, 93, 20, 30, 83, 30, 17, 26, 22, 80]]
