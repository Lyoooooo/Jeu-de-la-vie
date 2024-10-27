import numpy as np

def find_neighbors(matrix, n, m):
    neighbors = []
    rows, cols = matrix.shape
    for i in range(max(0, n-1), min(n+2, rows)):
        for j in range(max(0, m-1), min(m+2, cols)):
            if i == n and j == m:
                continue
            neighbors.append(matrix[i][j])
    return neighbors

def evaluate_dead(matrix, n, m):
    neighbors = find_neighbors(matrix, n, m)
    return 1 if np.sum(neighbors) == 3 else 0

def evaluate_alive(matrix, n, m):
    neighbors = find_neighbors(matrix, n, m)
    return 1 if np.sum(neighbors) in [2, 3] else 0

def evaluate(matrix):
    rows, cols = matrix.shape
    new_matrix = np.copy(matrix)
    for n in range(rows):
        for m in range(cols):
            cell = matrix[n, m]
            if cell == 1:
                new_matrix[n, m] = evaluate_alive(matrix, n, m)
            else:
                new_matrix[n, m] = evaluate_dead(matrix, n, m)
    return new_matrix
