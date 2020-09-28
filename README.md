# Pymathrix
Pymathrix is a python library for matrix objects creation and basic operations.

By using Pymathrix you can:

- Create matrices an assign values to them in python
- View a matrix object values in the command prompt
- Perform addition, subtraction and the Hadamard product to matrices
- Transpose matrices
- Multiply matrices (Dot product)

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pymathrix
```python
pip install pymathrix
```


## Usage
Import the library to your python code:
```python
>>> import pymathrix as px
```


## Creation of a matrix object
```python
>>> m = px.matrix(2, 3) # this creates a matrix with 2 rows and 3 columns and initialize them with zoros
```


Printing the matrix
-------------------
```python
>>> print(m)
|    0     0     0     |
|    0     0     0     |
```


## Storing values to the matrix
```python
>>> m.assign([[-2, 5.0, 9.2], [1, 7.2, -6.4]]) # storing 2 dimensional list
>>> print(m)
|   -2    5.0    9.2   |
|    1    7.2   -6.4   |

>>> m1 = px.matrix(1, 4)
>>> m1.assign([2.5, -4.9, 0.8, 5.6]) # storing 1 dimensional list (matrix with one row)
>>> print(m1)
|   2.5   -4.9    0.8    5.6  |

>>> m2 = px.matrix(1, 1)
>>> m2.assign(-6.1) # storing a numerical value (matrix with one row and one column)
>>> print(m2)
|  -6.1  |
```


## Printing a specified row or column
```python
>>> m.print_row(1) # prints the first row
(-2, 5.0, 9.2)
>>> m.print_col(2) # prints the second column
(5.0, 7.2)
```

## Storing a row or a column of a matrix into another matrix
```python
>>> m1 = px.matrix(3, 4)
>>> m1.randomize(-1, 1)
>>> print("Matrix m1:\n" + str(m1))
>>> m2 = m1.from_row(2) # storing the 2nd row as an individual matrix into m2
>>> print("Matrix m2:\n" + str(m2))
Matrix m1:
|  -0.6    0.0    0.3   -0.5  |
|   0.7   -0.8    0.4    0.2  |
|  -0.1   -1.0    0.2    0.1  |
Matrix m2:
|   0.7   -0.8    0.4    0.2  |

>>> m1 = px.matrix(3, 4)
>>> m1.randomize(-1, 1)
>>> print("Matrix m1:\n" + str(m1))
>>> m2 = m1.from_col(3) # storing the 3rd column as an individual matrix into m2
>>> print("Matrix m2:\n" + str(m2))
Matrix m1:
|   0.2    0.7    0.7    0.4  |
|   0.3   -0.9   -0.2    0.0  |
|  -0.4    0.6    0.6    0.8  |
Matrix m2:
|   0.7  |
|  -0.2  |
|   0.6  |
```


## Filling the matrix with random values
```python
>>> m.randomize(-10, 10) # this stores random values between -10 and 10 in the matrix
>>> print(m)
|   8.0    7.4    9.8  |
|  -0.4    8.4    6.2  |
```


## Filling the matrix with a specified value
```python
>>> m.all_to(6)
|    6      6      6   |
|    6      6      6   |
```


## Transposing a matrix
```python
>>> t = m.transpose() # this stores the transpose of the matrix 'm' into the matrix 't'
```
- example:
```python
>>> m = px.matrix(2, 3)
>>> m.randomize(-1, 1)
>>> print("Matrix m:\n" + str(m))
>>> print("Matrix m transposed:\n" + str(m.transpose()))
Matrix m:
|  -0.3   -0.9   -0.9  |
|  -0.7    0.5   -0.2  |
Matrix m transposed:
|  -0.3   -0.7  |
|  -0.9    0.5  |
|  -0.9   -0.2  |
```


## Adding two matrices together
```python
>>> m3 = px.matrix.add(m1, m2) # adding the matrices m1 and m2 together and storing the result in m3
```
- example:
```python
>>> m1 = px.matrix(2, 3).randomize(-1, 1) # creates the matrix object and randomize its values in one single line
>>> m2 = px.matrix(2, 3).randomize(-1, 1) # creates the matrix object and randomize its values in one single line
>>> print("Matrix m1:\n" + str(m1))
>>> print("Matrix m2:\n" + str(m2))
>>> print("Matrix m1 + Matrix m2:\n" + str(px.matrix.add(m1, m2)))
Matrix m1:
|  -0.1   -0.5   -0.6  |
|  -0.7    0.1    0.7  |
Matrix m2:
|   0.8   -1.0    0.2  |
|   0.7   -0.8    0.5  |
Matrix m1 + Matrix m2:
|   0.7   -1.5   -0.4  |
|   0.0   -0.7    1.2  |
```


## Subtracting a matrix from another
```python
>>> m3 = px.matrix.sub(m1, m2) # subtracts the matrices m2 from m1 and stores the result in m3
```
- example:
```python
>>> m1 = px.matrix(2, 3).randomize(-1, 1)
>>> m2 = px.matrix(2, 3).randomize(-1, 1)
>>> print("Matrix m1:\n" + str(m1))
>>> print("Matrix m2:\n" + str(m2))
>>> print("Matrix m1 - Matrix m2:\n" + str(px.matrix.sub(m1, m2)))
Matrix m1:
|  -0.1   -0.5   -0.6  |
|  -0.7    0.1    0.7  |
Matrix m2:
|   0.8   -1.0    0.2  |
|   0.7   -0.8    0.5  |
Matrix m1 - Matrix m2:
|  -0.9    0.5   -0.8  |
| -0.14    0.9    0.2  |
```


## Hadamard Product of two matrices
```python
>>> m3 = px.matrix.hadamard_prod(m1, m2) # performs the hadamard product
```
- example:
```python
>>> m1 = px.matrix(2, 3).randomize(-1, 1)
>>> m2 = px.matrix(2, 3).randomize(-1, 1)
>>> print("Matrix m1:\n" + str(m1))
>>> print("Matrix m2:\n" + str(m2))
>>> print("Matrix m1 * Matrix m2:\n" + str(px.matrix.hadamard_prod(m1, m2)))
Matrix m1:
|   0.2   -0.4   -1.0  |
|  -0.2    0.0   -0.1  |
Matrix m2:
|  -0.5    0.1   -1.0  |
|  -0.1    0.5    0.0  |
Matrix m1 * Matrix m2:
|  -0.1  -0.04    1.0  |
|  0.02    0.0   -0.0  |
```


## Matrices multiplication (dot product)
```python
>>> m3 = matrix.dot(m1, m2) # multiplying the matrix m1 by m2 and storing the result in m3
```
- example:
```python
>>> m1 = px.matrix(2, 3).randomize(-1, 1)
>>> m2 = px.matrix(3, 2).randomize(-1, 1)
>>> print("Matrix m1:\n" + str(m1))
>>> print("Matrix m2:\n" + str(m2))
>>> print("Matrix m1 o Matrix m2:\n" + str(px.matrix.dot(m1, m2)))
Matrix m1:
|   0.1   -0.5   -0.1  |
|  -0.5    0.8    0.1  |
Matrix m2:
|   0.9    0.4  |
|   0.8   -1.0  |
|  -0.3   -0.6  |
Matrix m1 o Matrix m2:
| -0.28    0.6  |
|  0.16  -1.06  |
```
