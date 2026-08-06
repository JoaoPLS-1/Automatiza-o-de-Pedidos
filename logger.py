from datetime import datetime


class Logger:

    def __init__(self):

        self.inicio = datetime.now()

    def info(self, texto):

        hora = datetime.now().strftime("%H:%M:%S")

        print(f"[{hora}] {texto}")

    def separador(self):

        print("-" * 60)