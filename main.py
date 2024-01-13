board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]
continuar = True
while continuar:
    movimiento = int(input("haga su movimiento"))
    if movimiento > 9 or movimiento < 1:
        print("Ingrese un numero entre 1 y 9")
    else:
        posicion_ocupada = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == movimiento:  # Convierte movimiento a cadena para la comparación
                    board[i][j] = "0"
                    continuar = False
                    posicion_ocupada = True
                    break
        if not posicion_ocupada:
            print("Posición ya seleccionada, haga su movimiento otra vez")
print(board)
