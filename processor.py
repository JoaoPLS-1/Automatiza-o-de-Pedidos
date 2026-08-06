import time

from config import (
    PASTA_IMPORTADOS,
    PASTA_ERROS
)

from parser_pdf import (
    ler_pdf,
    extrair_pedido
)

from validator import Validator
from file_manager import FileManager
from excel_writer import ExcelWriter
from logger import Logger
from history import History


logger = Logger()
files = FileManager()
excel = ExcelWriter()
history = History()


def processar_pdf(pdf):

    inicio = time.perf_counter()

    logger.info(f"Lendo: {pdf.name}")

    texto = ler_pdf(pdf)

    pedido = extrair_pedido(texto)

    erros = Validator.validar(pedido)

    if erros:

        logger.info("ERRO(S):")

        for erro in erros:
            logger.info(f" • {erro}")

        files.mover(pdf, PASTA_ERROS)

        history.registrar(
            pedido,
            "ERRO",
            time.perf_counter() - inicio
        )

        logger.separador()

        return False

    logger.info(f"Pedido: {pedido.numero}")
    logger.info(f"Cliente: {pedido.nome_cliente}")
    logger.info(f"Produtos: {len(pedido.produtos)}")

    arquivo_excel = excel.gerar(pedido)

    logger.info(f"Planilha criada: {arquivo_excel.name}")

    files.mover(pdf, PASTA_IMPORTADOS)

    logger.info("PDF movido para Importados.")

    history.registrar(
        pedido,
        "OK",
        time.perf_counter() - inicio
    )

    logger.separador()

    return True