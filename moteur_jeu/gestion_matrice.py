import numpy as np

def init_matrix(taille):
    return np.zeros((taille, taille), dtype=int)

def generate_random(size):
    matrix = np.random.choice([0,1],(size,size),p=[0.5,0.5])
    return matrix
