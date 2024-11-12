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


def evaluate_oppty(matrix, active_cells, TAILLE_GRILLE):
    if len(active_cells)> 12.5*TAILLE_GRILLE**2/100:
        matrix, active_cells = evaluate_all(matrix, active_cells)
    else:
        matrix, active_cells = evaluate_select(matrix, active_cells)
    return matrix, active_cells

def evaluate_all(matrix, active_cells):
    rows, cols = matrix.shape
    new_matrix = np.copy(matrix)

    for n in range(rows):
        for m in range(cols):
            cell = matrix[n, m]
            if cell == 1:
                new_matrix[n, m] = evaluate_alive(matrix, n, m)
                if(new_matrix[n, m]) == 0 : 
                    active_cells.remove((n,m))
            else:
                new_matrix[n, m] = evaluate_dead(matrix, n, m)
                if(new_matrix[n, m]) == 1 : 
                    active_cells.append((n,m))
    return new_matrix, active_cells

def evaluate_select(matrix, active_cells):
    new_matrix = np.copy(matrix)
    for active_cell in active_cells:
        print(active_cell)
        (active_n,active_m) = active_cell
        new_matrix[active_n][active_m] = evaluate_alive(matrix, active_n,active_m)
        print(new_matrix[active_n][active_m])
        neighbors = find_neighbors(matrix,active_n,active_m)
        for neighbor in neighbors:
            print(neighbor)
            (neighbor_n,neighbor_m) = neighbor
            if matrix[neighbor_n][neighbor_m] == 1:
                new_matrix[neighbor_n][neighbor_m] = evaluate_alive(matrix, neighbor_n,neighbor_m)
                if(new_matrix[neighbor_n][neighbor_m]) == 0 : 
                    active_cells.remove((neighbor_n,neighbor_m))
            else:
                new_matrix[neighbor_n][neighbor_m] = evaluate_dead(matrix, neighbor_n,neighbor_m)
                if(new_matrix[neighbor_n][neighbor_m]) == 1 : 
                    active_cells.append((neighbor_n,neighbor_m))
    return new_matrix, active_cells
