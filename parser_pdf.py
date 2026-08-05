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


def para_float(valor: str) -> float:
    valor = valor.replace("KG", "")
    valor = valor.replace("CX", "")
    valor = valor.replace(".", "")
    valor = valor.replace(",", ".")
    return float(valor)


def extrair_produtos(texto):

    produtos = []

    linhas = texto.splitlines()

    for linha in linhas:

        # Produto sempre começa com código, ex: 10903.0
        if re.match(r"^\d+\.\d", linha):

            numeros = re.findall(r"[\d,.]+(?:KG|CX)?", linha)

            if len(numeros) < 6:
                continue

            codigo = numeros[0]

            descricao = linha

            # Remove os números da descrição
            for numero in numeros:
                descricao = descricao.replace(numero, "")

            descricao = (
                descricao
                .replace("KG", "")
                .replace("CX", "")
                .strip()
            )

            produto = Produto(
                codigo=codigo,
                descricao=descricao,
                cx_kg=para_float(numeros[2]),
                volume=para_float(numeros[3]),
                venda=para_float(numeros[4]),
                venda_total=para_float(numeros[5])
            )

            produtos.append(produto)

    return produtos


def extrair_pedido(texto):

    numero = re.search(r"Documento:\s*100-PVE-001-(\d+)", texto)

    cliente = re.search(r"Cliente:\s*(\d+)\s*-\s*(.+)", texto)

    entrega = re.search(r"Data Entrega:\s*(\d{2}/\d{2}/\d{4})", texto)

    prazo = re.search(r"Cond\. pagamento:\s*(.+)", texto)

    vendedor = re.search(r"Vendedor:\s*\d+\s*-\s*(.+?)\s*Turno:", texto)

    qtde_itens = re.search(r"Qtde itens:\s*(\d+)", texto)

    pedido = Pedido(
        numero=numero.group(1) if numero else "",
        codigo_cliente=cliente.group(1) if cliente else "",
        nome_cliente=cliente.group(2).strip() if cliente else "",
        prazo_pgto=prazo.group(1).strip() if prazo else "",
        entrega=entrega.group(1).strip() if entrega else "",
        vendedor=vendedor.group(1).strip() if vendedor else "",
        qtde_itens=int(qtde_itens.group(1)) if qtde_itens else 0,
    )

    pedido.produtos = extrair_produtos(texto)

    return pedido