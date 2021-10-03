import numpy as np

#input is an adjacent matrix
#with calc_lenght you get a matrix with number of paths of a particular given length the co-ord of matrix
#the start and end node
#with calc_path you can query the specific number of path between start node m and end node n

def calculate_length(matrix,length):
    k = np.linalg.matrix_power(matrix,length)
    return k

def calculate_paths(matrix,length,m,n):
    k = np.linalg.matrix_power(matrix,length)
    return k[m,n]
