Pymathrix
=======
Pymathrix is a python library for matrix objects creation and basic operations.


Installation
############
This library can be installed by the running the command:
pip install pymathrix


Usage
#####
Import the library to your python code:
>>> import pymathrix as px


Creation of a matrix object
###########################
>>> m = px.matrix(2, 3) # this creates a matrix with 2 rows and 3 columns and initialize them with zoros


Printing the matrix
###################
>>> print(m)
|    0     0     0     |
|    0     0     0     |


Storing values to the matrix
############################
>>> m.assign([[-2, 5.0, 9.2], [1, 7.2, -6.4]])
>>> print(m)
|   -2    5.0    9.2   |
|    1    7.2   -6.4   |


Printing a specified row or column
##################################
>>> m.print_row(1) # prints the first row
(-2, 5.0, 9.2)
>>> m.print_col(2) # prints the second column
(5.0, 7.2)


Filling the matrix with random values
#####################################
>>> m.randomize(-10, 10) # this stores random values between -10 and 10 in the matrix
>>> print(m)
|   8.0    7.4    9.8  |
|  -0.4    8.4    6.2  |


Filling the matrix with the same value
######################################
>>> m.set_all_to(6)
|     6      6      6  |
|     6      6      6  |


Transposing a matrix
####################
>>> m = px.matrix(2, 3)
>>> m.randomize(-1, 1)
>>> print("m:\n" + str(m))
>>> m.transpose() # this overrides the 'm' matrix object with its transpose
>>> print("m transposed:\n" + str(m))
m1:
|   0.9   -0.7   -0.2  |
|  -0.1   -0.7    0.9  |
m1 transposed:
|   0.9   -0.1  |
|  -0.7   -0.7  |
|  -0.2    0.9  |


Adding two matrices together
############################
>>> m3 = px.matrix.add(m1, m2) # adds the matrices m1 and m2 together and storing the result in m3
- example:
>>> m1 = px.matrix(2, 3)
>>> m2 = px.matrix(2, 3)
>>> m1.randomize(-1, 1)
>>> m2.randomize(-1, 1)
>>> print("m1:\n" + str(m1))
>>> print("m2:\n" + str(m2))
>>> print("m1 + m2:\n" + str(px.matrix.add(m1, m2)))
m1:
|  -0.1   -0.5   -0.6  |
|  -0.7    0.1    0.7  |
m2:
|   0.8   -1.0    0.2  |
|   0.7   -0.8    0.5  |
m1 + m2:
|   0.7   -1.5   -0.4  |
|   0.0   -0.7    1.2  |


Matrices multiplication
#######################
>>> m3 = matrix.dot(m1, m2) # multiplies the matrix m1 by m2 and storing the result in m3
- example:
>>> m1 = px.matrix(2, 3)
>>> m2 = px.matrix(3, 2)
>>> m1.randomize(-1, 1)
>>> m2.randomize(-1, 1)
>>> print("m1:\n" + str(m1))
>>> print("m2:\n" + str(m2))
>>> print("m1 * m2:\n" + str(px.matrix.dot(m1, m2)))
m1:
|   0.1   -0.5   -0.1  |
|  -0.5    0.8    0.1  |
m2:
|   0.9    0.4  |
|   0.8   -1.0  |
|  -0.3   -0.6  |
m1 * m2:
| -0.28    0.6  |
|  0.16  -1.06  |