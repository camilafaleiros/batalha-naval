from random import randint

def inicializarGrid():
    M = [0]*10
    for i in range(10):
        M[i] = [0]*10
        for j in range(10):
            if M[i][j] == 0:
                M[i][j] = ' . '
    return M

def printMatriz(M):
    for i in range(10):
        for j in range(10):
            print(M[i][j],end="")
        print()
    

def aleatorio():
    linha = randint(0,9)
    coluna = randint(0,9)
    orientacao = randint(0,1)
    if orientacao == 0:
        orientacao = False #horizontal
    else:
        orientacao = True #vertical
    return linha, coluna, orientacao
    

def tipo(barco): #barco: portavioes, encouracado, cruzador, submarino
    #define o tamanho do barco a partir do seu tipo
    if barco == 'portavioes':
        t = 5
    elif barco == 'encouracado':
        t = 4
    elif barco == 'cruzador':
        t = 3
    elif barco == 'submarino':
        t = 2
    return t

'''
#não funciona

def verifica_disponibilidade(grid,barco): 
    linha,coluna,orientacao = aleatorio()

    #verifica se a posição escolhida está dentro do grid
    tamanho = len(grid)
    #for j in range(barco):
    flag = False
    while flag == False:
        if orientacao == True:
            if coluna  (barco - 1) > tamanho:
                flag = False
                linha, coluna, orientacao = aleatorio()
                verifica_disponibilidade(grid, barco)
            else:
                break

        elif orientacao == False:
            if linha + (barco - 1) > tamanho:
                flag = False
                linha, coluna, orientacao = aleatorio()
                verifica_disponibilidade(grid, barco)
            else:
                break

    #verifica se tem barcos na posição escolhida
    for i in range(barco):  
        if grid[linha][coluna] == ' . ':
            pass
        else:
            linha, coluna, orientacao = aleatorio()
            verifica_disponibilidade(grid, barco)

    return linha,coluna,orientacao 
'''

def verifica_disponibilidade(grid, barco, coluna, linha, orientacao):
    tamanho = len(grid)
    if orientacao == True: #vertical
        for i in range(barco):
            if linha >= tamanho or coluna + i >= tamanho:
                return False
            elif grid[linha][coluna + i] != ' . ':
                return False
    elif orientacao == False: 
        for i in range(barco):
            if linha + i >= tamanho or coluna >= tamanho:
                return False
            elif grid[linha + i][coluna] != ' . ':
                return False
    return True


def posicionar_porta_avioes(grid, linha, coluna, orientacao): 
    if orientacao == True:
        line = linha
        for i in range(5):
            grid[line][coluna] = ' P '
            line += 1
    elif orientacao == False:
        column = coluna
        for i in range(5):
            grid[linha][column] = ' P '
            column += 1
    else:
        return print("ocorreu um erro")
    return grid


def posicionar_encouracado(portavioes, linha, coluna, orientacao):
    if orientacao == True:
        line = linha
        for i in range(0,4):
            portavioes[line][coluna] = ' E '
            line += 1
    elif orientacao == False:
        column = coluna
        for i in range(0,4):
            portavioes[linha][column] = ' E '
            column += 1
    else:
        return print("ocorreu um erro")
    return portavioes


def posicionar_cruzador(encouracado, linha, coluna, orientacao): 
    if orientacao == True:
        line = linha
        for i in range(3):
            encouracado[line][coluna] = ' C '
            line += 1
    elif orientacao == False:
        column = coluna
        for i in range(3):
            encouracado[linha][column] = ' C '
            column += 1
    else:
        return print("ocorreu um erro")
    return encouracado


def posicionar_submarino(cruzador, linha, coluna, orientacao): 
    if orientacao == True:
        line = linha
        for i in range(2):
            cruzador[line][coluna] = ' S '
            line += 1   
    elif orientacao == False:
        column = coluna
        for i in range(2):
            cruzador[linha][column] = ' S '
            column += 1
    else:
        return print("ocorreu um erro")
    return cruzador


def facilita(matriz, kind):
    barco = tipo(kind)
    linha, coluna, orientacao = aleatorio()
    while verifica_disponibilidade(matriz, barco, coluna, linha, orientacao) == False:
        linha, coluna, orientacao = aleatorio()
    portavioes = posicionar_porta_avioes(matriz, linha, coluna, orientacao)
    return matriz


def main():
    M = inicializarGrid()
    portavioes = facilita(M, 'portavioes')
    encouracado = facilita(portavioes, 'encouracado')
    cruzador = facilita(encouracado, 'cruzador')
    submarino = facilita(cruzador, 'submarino')
    barcos_posicionados = submarino
    printMatriz(barcos_posicionados)


'''
#função facilitador faz isso tudo

    #porta aviões
    barco = tipo('portavioes')
    linha, coluna, orientacao = aleatorio()
    while verifica_disponibilidade(M, barco, coluna, linha, orientacao) == False:
        linha, coluna, orientacao = aleatorio()
        portavioes = posicionar_porta_avioes(M, linha, coluna, orientacao)

    #encouraçado
    barco = tipo('encouracado')
    linha, coluna, orientacao = aleatorio()
    while verifica_disponibilidade(M, barco, coluna, linha, orientacao) == False:
        linha, coluna, orientacao = aleatorio()
        encouracado = posicionar_encouracado(portavioes, linha, coluna, orientacao)

    #cruzador
    barco = tipo('cruzador')
    linha, coluna, orientacao = aleatorio()
    if verifica_disponibilidade(M, barco, coluna, linha, orientacao) == True:
        linha, coluna, orientacao = aleatorio()
        cruzador = posicionar_cruzador(encouracado, linha, coluna, orientacao)

    #submarino
    barco = tipo('submarino')
    linha, coluna, orientacao = aleatorio()
    if verifica_disponibilidade(M, barco, coluna, linha, orientacao) == True:
        linha, coluna, orientacao = aleatorio()
        submarino = posicionar_submarino(cruzador, linha, coluna, orientacao)

    barcos_posicionados = submarino
    printMatriz(barcos_posicionados)
'''

main()