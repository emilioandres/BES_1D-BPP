import numpy as np

#revisamos la restricción
def check_constraint(x, c, weight):
    bins = compute_fitness(x)
    # Verificar la validez de bins utilizando el algoritmo First-Fit
    bins_capacity = [0] * bins

    for w in weight:
        assigned = False
        for i in range(len(bins_capacity)):
            if bins_capacity[i] + w <= c:
                bins_capacity[i] += w
                assigned = True
                break
        if not assigned:
            return False

    return True
#computamos el fitness
def compute_fitness(bins):
    return np.sum(bins)   
#obtenemos el valor binario a partir del real
def real2bin(x):
    sigmoid_values = 1 / (1 + np.exp(-x))
    binary_values = np.where(sigmoid_values >= 0.5, 1, 0)
    return binary_values