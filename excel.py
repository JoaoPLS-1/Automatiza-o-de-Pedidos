from copy import copy
from openpyxl import load_workbook


class ExcelWriter:

    def __init__(self, caminho_modelo):

        self.wb = load_workbook(caminho_modelo)

        self.ws = self.wb.active

    def copiar_estilo(self, origem, destino):

        for coluna in range(1, 13):

            origem_cell = self.ws.cell(origem, coluna)

            destino_cell = self.ws.cell(destino, coluna)

            destino_cell._style = copy(origem_cell._style)

            destino_cell.number_format = origem_cell.number_format

            destino_cell.font = copy(origem_cell.font)

            destino_cell.fill = copy(origem_cell.fill)

            destino_cell.border = copy(origem_cell.border)

            destino_cell.alignment = copy(origem_cell.alignment)

    def salvar(self, caminho):

        self.wb.save(caminho)

        self.wb.close()