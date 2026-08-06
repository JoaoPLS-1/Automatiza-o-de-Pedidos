from config import (
    PASTA_PEDIDOS,
    PASTA_IMPORTADOS,
    PASTA_ERROS
)

from parser_pdf import (
    ler_pdf,
    extrair_pedido
)

from validator import Validator
from logger import Logger
from file_manager import FileManager
from excel_writer import ExcelWriter


logger = Logger()
files = FileManager()
excel = ExcelWriter()


logger.separador()
logger.info("AUTOMAÇÃO DE PEDIDOS")
logger.separador()

arquivos = files.listar_pdfs(PASTA_PEDIDOS)

logger.info(f"{len(arquivos)} PDF(s) encontrado(s).\n")

for pdf in arquivos:

    logger.info(f"Lendo: {pdf.name}")

    texto = ler_pdf(pdf)

    pedido = extrair_pedido(texto)

    erros = Validator.validar(pedido)

    if erros:

        logger.info("ERRO(S):")

        for erro in erros:

            logger.info(f"  • {erro}")

        files.mover(pdf, PASTA_ERROS)

        logger.separador()

        continue

    logger.info(f"Pedido: {pedido.numero}")

    logger.info(f"Cliente: {pedido.nome_cliente}")

    logger.info(f"Produtos: {len(pedido.produtos)}")

    arquivo_excel = excel.gerar(pedido)

    logger.info(f"Planilha criada: {arquivo_excel.name}")

    files.mover(pdf, PASTA_IMPORTADOS)

    logger.info("PDF movido para Importados.")

    logger.separador()

logger.info("Processamento finalizado.")