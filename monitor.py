import time

from config import PASTA_PEDIDOS

from file_manager import FileManager
from logger import Logger

from processor import processar_pdf


logger = Logger()
files = FileManager()


def iniciar_monitor():

    logger.separador()
    logger.info("MONITOR AUTOMÁTICO")
    logger.separador()

    logger.info("Monitorando pasta de pedidos...")
    logger.info("Pressione CTRL+C para encerrar.\n")

    while True:

        arquivos = files.listar_pdfs(PASTA_PEDIDOS)

        for pdf in arquivos:

            processar_pdf(pdf)

        time.sleep(2)


if __name__ == "__main__":

    try:

        iniciar_monitor()

    except KeyboardInterrupt:

        logger.separador()
        logger.info("Monitor encerrado pelo usuário.")