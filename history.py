import csv
from datetime import datetime

from config import PASTA_LOGS


class History:

    def __init__(self):

        PASTA_LOGS.mkdir(exist_ok=True)

        self.arquivo = PASTA_LOGS / "historico.csv"

        if not self.arquivo.exists():

            with open(self.arquivo, "w", newline="", encoding="utf-8-sig") as f:

                writer = csv.writer(f)

                writer.writerow([
                    "Data",
                    "Hora",
                    "Pedido",
                    "Cliente",
                    "Produtos",
                    "Status",
                    "Tempo(s)"
                ])

    def registrar(self,
                  pedido,
                  status,
                  tempo):

        agora = datetime.now()

        with open(self.arquivo,
                  "a",
                  newline="",
                  encoding="utf-8-sig") as f:

            writer = csv.writer(f)

            writer.writerow([
                agora.strftime("%d/%m/%Y"),
                agora.strftime("%H:%M:%S"),
                pedido.numero,
                pedido.nome_cliente,
                len(pedido.produtos),
                status,
                f"{tempo:.2f}"
            ])