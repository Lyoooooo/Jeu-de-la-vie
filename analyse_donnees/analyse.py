import matplotlib.pyplot as plt

def save_data(temps, data, exec, matrix):
    if(round(temps,0) > data[0][len(data[0]) - 1]):
        data[0].append(round(temps,0))
        data[1].append(int(count_matrix(matrix)))
        data[2].append(exec)
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

def creer_graph_exec(data):
    plt.title("Temps d'execution")
    plt.plot(data[0], data[2])
    plt.xlabel('Temps (en secondes)')
    plt.ylabel('Durée de calculs')
    plt.show()