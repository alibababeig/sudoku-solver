class InputManager:
    def __init__(self):
        self._numbers = [f'{x}' for x in range(1, 10)]
        self._empty_sign = '-'

    def load(self, file_path):
        with open(file_path, 'r') as f:
            flat_arr = []
            for i in range(9):
                row = f.readline().split()

                if len(row) != 9:
                    raise ValueError()

                for i, x in enumerate(row):
                    if x in self._numbers:
                        row[i] = int(x)
                    elif x == self._empty_sign:
                        row[i] = 0
                    else:
                        raise ValueError()

                flat_arr += row
        return flat_arr
