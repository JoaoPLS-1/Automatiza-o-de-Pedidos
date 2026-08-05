from pathlib import Path
from parser_pdf import ler_pdf

PASTA_PEDIDOS = Path("pedidos")

pdfs = list(PASTA_PEDIDOS.glob("*.pdf"))

if len(pdfs) == 0:
    print("Nenhum PDF encontrado na pasta pedidos.")
    exit()

pdf = pdfs[0]

print(f"Lendo arquivo: {pdf.name}\n")

texto = ler_pdf(pdf)

print(texto)