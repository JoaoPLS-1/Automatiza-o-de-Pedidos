from queue import Queue
from threading import Thread

from processor import processar_pdf


class QueueManager:

    def __init__(self):

        self.fila = Queue()

        self.worker = Thread(
            target=self.processar_fila,
            daemon=True
        )

        self.worker.start()

    def adicionar(self, pdf):

        self.fila.put(pdf)

    def processar_fila(self):

        while True:

            pdf = self.fila.get()

            try:

                processar_pdf(pdf)

            except Exception as e:

                print(f"Erro ao processar {pdf.name}: {e}")

            finally:

                self.fila.task_done()

    def tamanho(self):

        return self.fila.qsize()