import pdfplumber
import re

from models import Pedido, Produto


def ler_pdf(caminho_pdf):
    texto = ""

    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            conteudo = pagina.extract_text()
            if conteudo:
                texto += conteudo + "\n"

    return texto


def extrair_pedido(texto):

    cliente = re.search(r"Cliente:\s*(.+)", texto)
    entrega = re.search(r"Data Entrega:\s*(\d{2}/\d{2}/\d{4})", texto)
    prazo = re.search(r"Cond\. pagamento:\s*(.+)", texto)
    qtde_itens = re.search(r"Qtde itens:\s*(\d+)", texto)

    pedido = Pedido(
        cliente=cliente.group(1).strip() if cliente else "",
        prazo_pgto=prazo.group(1).strip() if prazo else "",
        entrega=entrega.group(1).strip() if entrega else "",
        qtde_itens=int(qtde_itens.group(1)) if qtde_itens else 0,
    )

    return pedido