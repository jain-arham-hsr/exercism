class Matrix:
    def __init__(self, matrix_string):
        self.rows = matrix_string.splitlines()

    def row(self, index):
        return list(map(int, self.rows[index-1].split()))

    def column(self, index):
        return list(map(int, [row.split()[index - 1] for row in self.rows]))
