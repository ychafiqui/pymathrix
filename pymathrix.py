from random import randrange

class matrix:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.values = [[0 for x in range(self.num_cols)] for y in range(self.num_rows)]

    def set_rows(self, num_rows):
        if num_rows <= 0:
            print("Number of rows must be greater than 0!")
            exit()
        elif self.num_rows < num_rows:
            l = []
            for _ in range(self.num_cols):
                l.append(0.0)
            for _ in range(num_rows - self.num_rows):
                self.values.append(l)
        elif self.num_rows > num_rows:
            m = matrix(num_rows, self.num_cols)
            for i in range(num_rows):
                for j in range(self.num_cols):
                    m.values[i][j] = self.values[i][j]
            self.values = m.values
        self.num_rows = num_rows

    def set_cols(self, num_cols):
        if num_cols <= 0:
            print("Number of columns must be greater than 0!")
            exit()
        elif self.num_cols < num_cols:
            for i in range(self.num_rows):
                for _ in range(num_cols - self.num_cols):
                    self.values[i].append(0.0)
        elif self.num_cols > num_cols:
            m = matrix(self.num_rows, num_cols)
            for i in range(self.num_rows):
                for j in range(num_cols):
                    m.values[i][j] = self.values[i][j]
            self.values = m.values
        self.num_cols = num_cols

    def set_dim(self, num_rows, num_cols):
        self.set_rows(num_rows)
        self.set_cols(num_cols)

    def assign(self, values):
        if isinstance(values, list):
            if isinstance(values[0], list):
                nr = nc = 0
                for _ in range(len(values)): nr += 1
                for _ in range(len(values[0])): nc += 1
                
                if nc == self.num_cols:
                    if nr == self.num_rows:
                        self.values = values
                    else:
                        print("Number of rows must be equal to " + str(self.num_rows) + ", you entered " + str(nr) + " rows!")
                        exit()
                else:
                    print("Number of columns must be equal to " + str(self.num_cols) + ", you entered " + str(nc) + " columns!")
                    exit()
            else:
                if self.num_rows == 1:
                    nc = 0
                    for _ in range(len(values)): nc += 1
                    
                    if nc == self.num_cols: self.values[0] = values
                    else:
                        print("The matrix was created with " + str(self.num_cols) + " columns, but you are trying to assign " + str(nc) + " columns to it!")
                        exit()
                else:
                    print("The matrix was created with " + str(self.num_rows) + " rows, but you are trying to assign 1 row to it!")
                    exit()
        elif isinstance(values, matrix):
            if self.num_cols == values.num_cols and self.num_rows == values.num_rows:
                self.values = values.values
            else:
                print("Cannot assign a matrix to another if they have different dimensions!")
                exit()
        elif isinstance(values, int) or isinstance(values, float):
            if self.num_rows == 1 and self.num_cols == 1:
                self.values[0][0] = values
            else:
                print("The matrix was created with " + str(self.num_rows) + " rows and " + str(self.num_cols) + " columns, but you are trying to assign 1 row and 1 column to it!")
                exit()
        else:
            print("You can only assign matrices, lists, integers and floating numbers to a matrix object!")
            exit()

    def randomize(self, min, max):
        self.values = [[randrange(10 * min, 10 * max)/10 for x in range(self.num_cols)] for y in range(self.num_rows)]
        return self

    def all_to(self, val):
        if isinstance(val, int) or isinstance(val, float):
            self.values = [[val for x in range(self.num_cols)] for y in range(self.num_rows)]
        else:
            print("Matrix can only have numerical values!")
            exit()

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
        if row_index > self.num_rows:
            print("The matrix has " + str(self.num_rows) + " rows only!")
            exit()
        elif row_index <= 0:
            print("Row index must be greater than 0!")
            exit()
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
                exit()

    def from_row(self, row_index):
        row = matrix(1, self.num_cols)
        if row_index > self.num_rows:
            print("The matrix has " + str(self.num_rows) + " rows only!")
            exit()
        elif row_index <= 0:
            print("Row index must be greater than 0!")
            exit()
        else:
            try:
                for i in range(self.num_cols):
                    row.values[0][i] = self.values[row_index-1][i]
                return row
            except TypeError:
                print("Row index must be an integer number!")
                exit()

    def print_col(self, col_index):
        if col_index > self.num_cols:
            print("The matrix has " + str(self.num_rows) + " columns only!")
            exit()
        elif col_index <= 0:
            print("Column index must be greater than 0!")
            exit()
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
                exit()

    def from_col(self, col_index):
        col = matrix(self.num_rows, 1)
        if col_index > self.num_cols:
            print("The matrix has " + str(self.num_cols) + " columns only!")
            exit()
        elif col_index <= 0:
            print("Column index must be greater than 0!")
            exit()
        else:
            try:
                for i in range(self.num_rows):
                    col.values[i][0] = self.values[i][col_index-1]
                return col
            except TypeError:
                print("Column index must be an integer number!")
                exit()

    def add(a, b):
        if a.num_cols == b.num_cols:
            if a.num_rows == b.num_rows:
                c = matrix(a.num_rows, a.num_cols)
                for i in range(c.num_rows):
                    for j in range(c.num_cols):
                        c.values[i][j] = round(a.values[i][j] + b.values[i][j], 3)
                return c
            else:
                print("Matrices must have the same number of rows in order to add them toghether!")
                exit()
        else:
            print("Matrices must have the same number of columns in order to add them toghether!")
            exit()

    def sub(a, b):
        if a.num_cols == b.num_cols:
            if a.num_rows == b.num_rows:
                c = matrix(a.num_rows, a.num_cols)
                for i in range(c.num_rows):
                    for j in range(c.num_cols):
                        c.values[i][j] = round(a.values[i][j] - b.values[i][j], 3)
                return c
            else:
                print("Matrices must have the same number of rows in order to subtract one from the other!")
                exit()
        else:
            print("Matrices must have the same number of columns in order to subtract one from the other!")
            exit()

    def hadamard_prod(a, b):
        if isinstance(a, matrix) and isinstance(b, matrix):
            if a.num_cols == b.num_cols:
                if a.num_rows == b.num_rows:
                    c = matrix(a.num_rows, a.num_cols)
                    for i in range(c.num_rows):
                        for j in range(c.num_cols):
                            c.values[i][j] = round(a.values[i][j] * b.values[i][j], 3)
                    return c
                else:
                    print("Matrices must have the same number of rows in order to perform the hadamard multiplication!")
                    exit()
            else:
                print("Matrices must have the same number of columns in order to perform the hadamard multiplication!")
                exit()
        elif isinstance(a, matrix) and (isinstance(b ,int) or isinstance(b ,float)):
            c = matrix(a.num_rows, a.num_cols)
            for i in range(c.num_rows):
                for j in range(c.num_cols):
                    c.values[i][j] = round(a.values[i][j] * b, 3)
            return c

        elif isinstance(b, matrix) and (isinstance(a ,int) or isinstance(a ,float)):
            c = matrix(b.num_rows, b.num_cols)
            for i in range(c.num_rows):
                for j in range(c.num_cols):
                    c.values[i][j] = round(a * b.values[i][j], 3)
            return c

        else: return a*b

    def dot(a, b):
        if isinstance(a, matrix) and isinstance(b, matrix):
            if a.num_cols == b.num_rows:
                c = matrix(a.num_rows, b.num_cols)
                for i in range(c.num_rows):
                    for j in range(c.num_cols):
                        sum = 0
                        for k in range(a.num_cols):
                            sum += a.values[i][k] * b.values[k][j]
                        c.values[i][j] = round(sum, 3)
                return c
            else:
                print("The number of rows of the first matrix must match the number of columns of the second matrix!")
                exit()
        else:
            print("The dot() function take two matrices as parameters, you gave it something else!")
            exit()

    def transpose(self):
        c = matrix(self.num_cols, self.num_rows)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                c.values[j][i] = self.values[i][j]
        return c

    def determinant(self):
        if self.num_cols == self.num_rows:
            if self.num_cols == 2:
                det = self.values[0][0] * self.values[1][1]
                det -= self.values[0][1] * self.values[1][0]
                return round(det, 2)
            elif self.num_cols == 3:
                m1 = matrix(2, 2)
                m2 = matrix(2, 2)
                m3 = matrix(2, 2)
                m1.assign([
                    [self.values[1][1], self.values[1][2]],
                    [self.values[2][1], self.values[2][2]]
                ])
                m2.assign([
                    [self.values[1][0], self.values[1][2]],
                    [self.values[2][0], self.values[2][2]]
                ])
                m3.assign([
                    [self.values[1][0], self.values[1][1]],
                    [self.values[2][0], self.values[2][1]]
                ])
                det = self.values[0][0] * m1.determinant()
                det -= self.values[0][1] * m2.determinant()
                det += self.values[0][2] * m3.determinant()
                return round(det, 2)
            else:
                print("The function can only calculate the determinant of matrices with dimensions 2x2 or 3x3 for the moment.")
                exit()
        else:
            print("Cannot calculate the determinant, the number of rows of the matrix must match its number of columns!")
            exit()
