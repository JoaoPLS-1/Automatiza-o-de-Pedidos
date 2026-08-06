from queue_manager import QueueManager

import time
from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from config import PASTA_PEDIDOS
from logger import Logger
from processor import processar_pdf


logger = Logger()

queue = QueueManager()

def aguardar_pdf_liberado(pdf: Path,
                          tentativas=20,
                          espera=0.5):

    """
    Aguarda o PDF terminar de ser gravado.
    """

    for _ in range(tentativas):

        try:

            with open(pdf, "rb"):
                return True

        except PermissionError:

            time.sleep(espera)

    return False


class MonitorPedidos(FileSystemEventHandler):

    def on_created(self, event):

        if event.is_directory:
            return

        caminho = Path(event.src_path)

        if caminho.suffix.lower() != ".pdf":
            return

        logger.separador()
        logger.info(f"Novo PDF detectado: {caminho.name}")

        if aguardar_pdf_liberado(caminho):

            queue.adicionar(caminho)

            logger.info(
            f"Fila: {queue.tamanho()} pedido(s)"
)

        else:

            logger.info("Arquivo ainda bloqueado.")
            logger.separador()


def iniciar_monitor():

    logger.separador()
    logger.info("AUTOMAÇÃO DE PEDIDOS")
    logger.info("Monitor em execução...")
    logger.info(f"Pasta monitorada: {PASTA_PEDIDOS}")
    logger.info("Pressione CTRL+C para encerrar.")
    logger.separador()

    observer = Observer()

    observer.schedule(
        MonitorPedidos(),
        str(PASTA_PEDIDOS),
        recursive=False
    )
    logger.info("Verificando pedidos pendentes...")

    for pdf in sorted(PASTA_PEDIDOS.glob("*.pdf")):

        logger.info(f"Adicionado à fila: {pdf.name}")

        queue.adicionar(pdf)

    observer.start()

    try:

        while True:

            time.sleep(1)

    except KeyboardInterrupt:

        logger.info("Encerrando monitor...")

        observer.stop()

    observer.join()


if __name__ == "__main__":

    iniciar_monitor()