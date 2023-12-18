from domain import Celda, TipoCelda
from domain.rejilla import Rejilla
from domain.constantes import Constantes


class Juego:
    def __init__(self):
        self.rejilla = Rejilla()
        self.rejilla.__set_grid__()
        self.rejilla.__set_alive__()

    def __start__(self) -> None:
        print(self.rejilla.__to_str__())
        self.next_turn_grid()

    def next_turn_grid(self)-> None:
        for turno in range(Constantes.DEFAULT_GAME_TURNS):
            for fila in range(Constantes.DEFAULT_CELL_HEIGHT):
                for columna in range(Constantes.DEFAULT_CELL_WIDTH):
                    celda: Celda = next(filter(lambda item: item.fila == fila and item.columna == columna, self.rejilla.celdas),
                                       None)
                    self.get_cell_living_neighbors(celda)

            print(self.rejilla.__to_str__())

    def get_cell_living_neighbors(self, celda:Celda):
        vecinas: list[Celda] = []

        arriba_izq = next(filter(lambda item: item.fila == celda.fila - 1 and item.columna == celda.columna - 1 and item.tipocelda == TipoCelda.Viva, self.rejilla.celdas),
                                   None)

        if arriba_izq is not None:
            vecinas.append(arriba_izq)

        arriba_cen = next(
            filter(lambda item: item.fila == celda.fila - 1 and item.columna == celda.columna and item.tipocelda == TipoCelda.Viva, self.rejilla.celdas),
            None)

        if arriba_cen is not None:
            vecinas.append(arriba_cen)

        arriba_der = next(
            filter(lambda item: item.fila == celda.fila - 1 and item.columna == celda.columna + 1 and item.tipocelda == TipoCelda.Viva, self.rejilla.celdas),
            None)

        if arriba_der is not None:
            vecinas.append(arriba_der)

        izq = next(filter(lambda item: item.fila == celda.fila and item.columna == celda.columna - 1 and item.tipocelda == TipoCelda.Viva, self.rejilla.celdas),
                                   None)

        if izq is not None:
            vecinas.append(izq)

        der = next(
            filter(lambda item: item.fila == celda.fila and item.columna == celda.columna + 1 and item.tipocelda == TipoCelda.Viva, self.rejilla.celdas),
            None)

        if der is not None:
            vecinas.append(der)

        abajo_izq = next(
            filter(lambda item: item.fila == celda.fila + 1 and item.columna == celda.columna - 1 and item.tipocelda == TipoCelda.Viva, self.rejilla.celdas),
            None)

        if abajo_izq is not None:
            vecinas.append(abajo_izq)

        abajo_cen = next(
            filter(lambda item: item.fila == celda.fila + 1 and item.columna == celda.columna and item.tipocelda == TipoCelda.Viva, self.rejilla.celdas),
            None)

        if abajo_cen is not None:
            vecinas.append(abajo_cen)

        abajo_der = next(
            filter(lambda item: item.fila == celda.fila + 1 and item.columna == celda.columna + 1, self.rejilla.celdas),
            None)

        if abajo_der is not None:
            vecinas.append(abajo_der)

        count:int = vecinas.__len__()

        if count < 2 or count > 3:
            celda.tipocelda = TipoCelda.Muerta
        elif count >= 2:
            celda.tipocelda = TipoCelda.Viva

        idx = list(map(lambda item: item.fila == celda.fila and item.columna == celda.columna, self.rejilla.celdas)).index(True)

        self.rejilla.celdas[idx].tipocelda = celda.tipocelda
