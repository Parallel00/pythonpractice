def sum_up_diagonals(matrix):
    totl = 0
    
    for a in range(len(matrix)):
        totl += matrix[a][a]
        totl += matrix[a][-1 - a]
    return totl