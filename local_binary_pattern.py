def compare_neighborhood(img, center, x, y):
    '''
    Compara o valor do pixel central com outro ao redor.

    Parameters:
    img (numpy array): matriz 2D com valores de pixels
    center (int): valor do pixel central
    x (int): posição x do pixel vizinho
    y (int): posição y do pixel vizinho

    Returns:
    new_value (int): valor binário resultado da comparação
    '''

    new_value = 0
    try:
        if img[x][y] >= center:
            new_value = 1
    except:
        pass
    return new_value

def local_binary_pattern(img, x, y, radius=3):
    '''
    Função que retorna o valor do LBP em uma região 3x3 da imagem.
    
    Parameters:
    img (numpy array): matriz 2D com valores de pixels
    x (int): posição x do pixel central
    y (int): posição y do pixel central

    Returns:
    pixel (int): novo valor para o pixel central
    '''    

    center = img[x][y]
    min = -(radius//2)
    max = (radius//2) + 1

    bin = []
    for i in range(min, max):
        for j in range(min, max):
            if i != 0 and j != 0:
                bin.append(compare_neighborhood(img, center, x+i, y+i))

    weight = [1, 2, 4, 8, 16, 32, 64, 128]
    
    new_val = 0
    for i, _ in enumerate(bin):
        new_val += bin[i] * weight[i]
    
    return new_val
