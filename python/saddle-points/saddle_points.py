def saddle_points(matrix):
    if min(matrix, key=len, default=None) != max(matrix, key=len, default=None):
        raise ValueError("Irregular Matrix.")
    res = []
    for ind_y, column in enumerate(zip(*matrix)):
        for ind_x, num in enumerate(column):
            if num == min(column) and max(matrix[ind_x]) == min(column):
                    res.append({"row": ind_x + 1, "column": ind_y + 1})
    return res