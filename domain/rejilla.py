from random import randrange

from domain import TipoCelda
from domain.celda import Celda
from domain.constantes import Constantes
import os

class Rejilla:
    def __init__(self):
        self.celdas:list[Celda]=[]

    def __str__(self):
        rst :str= ""

        for fila in range(Constantes.DEFAULT_CELL_HEIGHT):
            for columna in range(Constantes.DEFAULT_CELL_WIDTH):
                cell: Celda = next(filter(lambda item: item.fila == fila and item.columna == columna, self.celdas),
                                   None)

                rst = rst + cell.__str__()

                if columna == range(Constantes.DEFAULT_CELL_WIDTH)[-1]:
                    rst = f"{rst}{os.linesep}"

        return rst

    def __set_grid__(self) -> None:
        for fila in range(Constantes.DEFAULT_CELL_HEIGHT):
            for columna in range(Constantes.DEFAULT_CELL_WIDTH):
                self.celdas.append(Celda(columna, fila))

    def __set_alive__(self) -> None:
        vivas: int = round(Constantes.DEFAULT_CELL_WIDTH * Constantes.DEFAULT_CELL_HEIGHT * (Constantes.DEFAULT_INIT_ALIVE_CELLS_NUM / 100) / 2)

        for viva in range(vivas):
            rand_col: int = randrange(Constantes.DEFAULT_CELL_WIDTH)
            rand_fila: int = randrange(Constantes.DEFAULT_CELL_HEIGHT)

            idx = list(map(lambda item: item.fila == rand_fila and item.columna == rand_col, self.celdas)).index(True)

            self.celdas[idx].tipocelda = TipoCelda.Viva

