class Matrix:
    def __init__(self, data):
        self.data = data

    def transpose(self):
        transposed_data = [list(row) for row in zip(*self.data)]
        return Matrix(transposed_data)
