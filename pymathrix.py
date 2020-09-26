from random import randrange

class matrix():
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.values = [[0 for x in range(self.num_cols)] for y in range(self.num_rows)]

    def assign(self, values):
        nr = 0
        nc = 0
        for i in range(len(values)):
            nr += 1
        for j in range(len(values[0])):
            nc += 1
        
        if nr == self.num_rows:
            if nr == self.num_rows:
                self.values = values
            else: print("Number of rows must be equal to " + str(self.num_rows) + ", you entered " + str(nr) + " rows!")
        else: print("Number of columns must be equal to " + str(self.num_cols) + ", you entered " + str(nc) + " columns!")

    def randomize(self, min, max):
        self.values = [[randrange(10 * min, 10 * max)/10 for x in range(self.num_cols)] for y in range(self.num_rows)] 

    def set_all_to(self, val):
        self.values = [[val for x in range(self.num_cols)] for y in range(self.num_rows)]

    def __str__(self):
        output = ""
        for i in range(self.num_rows):
            if len(str(self.values[i][0])) == 1: output += "|     "
            elif len(str(self.values[i][0])) == 2: output += "|    "
            elif len(str(self.values[i][0])) == 3: output += "|   "
            elif len(str(self.values[i][0])) == 4: output += "|  "
            elif len(str(self.values[i][0])) == 5: output += "| "
            else: output += "|"
            for j in range(self.num_cols):
                output += str(self.values[i][j])
                if j != self.num_cols - 1:
                    if len(str(self.values[i][j+1])) == 1: output += "      "
                    elif len(str(self.values[i][j+1])) == 2: output += "     "
                    elif len(str(self.values[i][j+1])) == 3: output += "    "
                    elif len(str(self.values[i][j+1])) == 4: output += "   "
                    elif len(str(self.values[i][j+1])) == 5: output += "  "
                    else: output += " "
            output += "  |"
            if i != self.num_rows - 1:
                output += "\n"
        return output

    def print_row(self, row_index):
        if row_index > self.num_rows: print("The matrix has " + str(self.num_rows) + " rows!")
        elif row_index <= 0: print("Row index must be greater than 0!")
        else:
            try:
                output = "("
                for i in range(self.num_cols):
                    output += str(self.values[row_index-1][i])
                    if i != self.num_cols - 1: output += ", "
                    else: output += ")"
                print(output)
            except TypeError:
                print("Row index must be an integer number!")

    def print_col(self, col_index):
        if col_index > self.num_cols: print("The matrix has " + str(self.num_rows) + " columns!")
        elif col_index <= 0: print("Column index must be greater than 0!")
        else:
            try:
                output = "("
                for i in range(self.num_rows):
                    output += str(self.values[i][col_index-1])
                    if i != self.num_rows - 1: output += ", "
                    else: output += ")"
                print(output)
            except TypeError:
                print("Column index must be an integer number!")

    def add(a, b):
        if a.num_cols == b.num_cols:
            if a.num_rows == b.num_rows:
                c = matrix(a.num_rows, a.num_cols)
                for i in range(c.num_rows):
                    for j in range(c.num_cols):
                        c.values[i][j] = round(a.values[i][j] + b.values[i][j], 3)
                return c
            else: print("Matrices must have the same number of rows in order to add them toghether!")
        else: print("Matrices must have the same number of columns in order to add them toghether!")

    def dot(a, b):
        if a.num_cols == b.num_rows:
            c = matrix(a.num_rows, b.num_cols)
            for i in range(c.num_rows):
                for j in range(c.num_cols):
                    sum = 0
                    for k in range(a.num_cols):
                        sum += a.values[i][k] * b.values[k][j]
                    c.values[i][j] = round(sum, 3)
            return c
        else: print("The number of rows of the first matrix must match the number of columns of the second matrix!")

    def transpose(self):
        c = matrix(self.num_cols, self.num_rows)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                c.values[j][i] = self.values[i][j]
        self.values = c.values
        self.num_cols = c.num_cols
        self.num_rows = c.num_rows