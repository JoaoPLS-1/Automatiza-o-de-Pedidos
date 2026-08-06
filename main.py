from config import PASTA_PEDIDOS

from file_manager import FileManager
from logger import Logger

from processor import processar_pdf


logger = Logger()
files = FileManager()

logger.separador()
logger.info("AUTOMAÇÃO DE PEDIDOS")
logger.separador()

arquivos = files.listar_pdfs(PASTA_PEDIDOS)

logger.info(f"{len(arquivos)} PDF(s) encontrado(s).")

logger.separador()

for pdf in arquivos:

    processar_pdf(pdf)

logger.info("Processamento finalizado.")