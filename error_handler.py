from pathlib import Path
from datetime import datetime
import traceback

from config import PASTA_LOGS


class ErrorHandler:

    @staticmethod
    def registrar(erro):

        PASTA_LOGS.mkdir(exist_ok=True)

        arquivo = PASTA_LOGS / "errors.log"

        with open(
            arquivo,
            "a",
            encoding="utf-8"
        ) as f:

            f.write("=" * 70 + "\n")
            f.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            f.write("\n\n")
            f.write(str(erro))
            f.write("\n\n")
            f.write(traceback.format_exc())
            f.write("\n")