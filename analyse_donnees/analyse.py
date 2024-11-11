import matplotlib.pyplot as plt

def save_data(temps, data, matrix):
    if(round(temps,0) > data[0][len(data[0]) - 1]):
        data[0].append(round(temps,0))
        data[1].append(int(count_matrix(matrix)))
    return data


def count_matrix(matrix):
    nombre_cellules = sum(sum(row) for row in matrix)
    return(nombre_cellules)

def creer_graph(data):
    plt.title("Nombre de cellules")
    plt.plot(data[0], data[1])
    plt.xlabel('Temps (en secondes)')
    plt.ylabel('Cellules')
    plt.show()