def damerau_levenshtein(string1: str, string2: str) -> int:
    """
        Calculates distance between two words.

        Possible moves:
            - Deletion (one move)
            - Insertion (one move)
            - substitution (zero or one move)

    Args:
        string1 (str): First word what we want to compare
        string2 (str): Second word what we want to compare

    Returns:
        int: Distance between two words
    """
    matrix = {}

    string_1_length = len(string1)
    string_2_length = len(string2)

    for i in range(string_1_length + 1):
        matrix[i, 0] = i

    for i in range(string_2_length + 1):
        matrix[0, i] = i

    for y_coordinate in range(1, string_2_length + 1):
        for x_coordinate in range(1, string_1_length + 1):

            if string1[x_coordinate - 1] == string2[y_coordinate - 1]:
                move = 0
            else:
                move = 1

            matrix[x_coordinate, y_coordinate] = min(
                matrix[x_coordinate - 1, y_coordinate] + 1,
                matrix[x_coordinate, y_coordinate - 1] + 1,
                matrix[x_coordinate - 1, y_coordinate - 1] + move,
            )

    return matrix[string_1_length, string_2_length]
