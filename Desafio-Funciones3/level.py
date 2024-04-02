def choose_level(n_pregunta, p_level):
    
    # Construir lógica para escoger el nivel
    ##################################################
    #Codigo correcto que indica el nivel de la pregunta
    
    if n_pregunta <= p_level:
        level = "basicas"
    elif n_pregunta <= 2 * p_level:
        level = "intermedias"
    else:
        level = "avanzadas"
    return level
"""
codigo anterior -> verificaba que las preguntans correspondieran a dicho nivel
    if p_level == 2:
        if 1 <= n_pregunta <=  2:
            return "básicas"
        elif 3 <= n_pregunta <= 4:
            return "intermedias"
        elif 5 <= n_pregunta <= 6:
            return "avanzadas"
    elif p_level == 3:
        if 1 <= n_pregunta <= 3:
            return "básicas"
        elif 4 <= n_pregunta <= 6:
            return "intermedias"
        elif  7 <= n_pregunta <= 9:
            return "avanzadas"    
    else:
        return "básicas"

        level = "avanzadas"
"""
    ##################################################

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(1, 1)) # básicas
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # -> None?
    print(choose_level(4, 3)) # intermedias