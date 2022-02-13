def damerau_levenshtein(string1: str, string2: str) -> int:
    matrix = {}

    string_1_length = len(string1)
    string_2_length = len(string2)

    for i in range(string_1_length + 1):
        matrix[i, 0] = i

    for i in range(string_2_length + 1):
        matrix[0, i] = i

    for y in range(1, string_2_length + 1):
        for x in range(1, string_1_length + 1):

            if string1[x - 1] == string2[y - 1]:
                move = 0
            else:
                move = 1

            matrix[x, y] = min(
                matrix[x - 1, y] + 1,
                matrix[x, y - 1] + 1,
                matrix[x - 1, y - 1] + move,
            )

    # print('Koordinaatit:')
    # for y in range(string_2_length + 1):
    #     for x in range(string_1_length + 1):
    #         print(f'({x}, {y})', end='')
    #     print()
    # print()
    # print('Arvot:')
    # for y in range(string_2_length + 1):
    #     for x in range(string_1_length + 1):
    #         print(matrix[x, y], end=' ')
    #     print()

    return matrix[string_1_length, string_2_length]
