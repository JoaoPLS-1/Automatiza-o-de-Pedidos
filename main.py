from pathlib import Path

from parser_pdf import ler_pdf, extrair_pedido

PASTA_PEDIDOS = Path("pedidos")

pdfs = list(PASTA_PEDIDOS.glob("*.pdf"))

if not pdfs:
    print("Nenhum PDF encontrado.")
    exit()

texto = ler_pdf(pdfs[0])

pedido = extrair_pedido(texto)

print("CLIENTE:", pedido.cliente)
print("PRAZO:", pedido.prazo_pgto)
print("ENTREGA:", pedido.entrega)
print("QTDE ITENS:", pedido.qtde_itens)