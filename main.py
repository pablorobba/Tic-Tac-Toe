from random import randrange


def display_board(board):
    
    """La función acepta un parámetro el cual contiene el estado actual del tablero
    y lo muestra en la consola.
    """        
    print("+-------" * 3,"+",sep="")
    for i in range(3):
        print("|       " * 3,"|", sep="")
        for j in range(3):
            print("|   " + str(board[i][j]) + "   ", end = "")
        print("|")
        print("|       " * 3,"|", sep="")
        print("+-------" * 3,"+",sep="")

def enter_move(board):
    
    """ La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    verifica la entrada y actualiza el tablero acorde a la decisión del usuario. 
    """
    continuar = True
    while continuar:
        movimiento = int(input("haga su movimiento"))
        if movimiento > 9 or movimiento < 1:
            print("Ingrese un numero entre 1 y 9")
        else:
            posicion_ocupada = True
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == movimiento:  # Convierte movimiento a cadena para la comparación
                        board[i][j] = "O"
                        continuar = False
                        posicion_ocupada = False
                        break
            if  posicion_ocupada:
                print("Posición ya seleccionada, haga su movimiento otra vez")   
                
def make_list_of_free_fields(board):
    
    """ La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    """
    vacios = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != "O" and board[i][j] != "X":
                vacios.append((i,j))
    return vacios

def victory_for(board, sign):
                
        if sign == "X":
            who = "machine"
        if sign == "O":
            who = "me"
        diagonal1 = diagonal2 = True
        for i in range(3):
            if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign: #filas
                return who
            if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign: #columnas
                return who
            if board[i][2-i] != sign:
                diagonal2 = False
            if board [i][i] != sign:
                diagonal1 = False

        if diagonal1 or diagonal2:
            return who
        return None  
    
    
def draw_move(board):
    
    """ La función dibuja el movimiento de la máquina y actualiza el tablero. 
    """
    continuar = True 
            
    if board[1][1] == 5:
        board[1][1] = "X"
    else:
        while continuar:
            movimiento = randrange(10) 
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == movimiento:  # Convierte movimiento a cadena para la comparación
                        board[i][j] = "X"
                        continuar = False        
def main():
    board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]
    libres = make_list_of_free_fields(board)
    victoria = victoria2 = None
    while True:
        draw_move(board)
        libres = make_list_of_free_fields(board)
        display_board(board)
        victoria = victory_for(board, "X")        
        if victoria != None :
            print("perdiste")
            break
        if libres == []:
            print("juego terminado, no quedan más movimientos")
            break
        enter_move(board)
        victoria2 = victory_for(board, "O")
        if victoria2 != None :
            display_board(board)
            print("ganaste")
            break

if __name__ == "__main__":
    main()