from pathlib import Path

from parser_pdf import ler_pdf, extrair_pedido

PASTA_PEDIDOS = Path("pedidos")

pdfs = list(PASTA_PEDIDOS.glob("*.pdf"))

if not pdfs:
    print("Nenhum PDF encontrado.")
    exit()

texto = ler_pdf(pdfs[0])

pedido = extrair_pedido(texto)

print("===================================")
print("PEDIDO")
print("===================================")

print(f"Número........: {pedido.numero}")
print(f"Cliente.......: {pedido.nome_cliente}")
print(f"Código Cliente: {pedido.codigo_cliente}")
print(f"Prazo.........: {pedido.prazo_pgto}")
print(f"Entrega.......: {pedido.entrega}")
print(f"Vendedor......: {pedido.vendedor}")
print(f"Qtde Itens....: {pedido.qtde_itens}")

print("\n================ PRODUTOS ================\n")

for i, produto in enumerate(pedido.produtos, start=1):
    print(f"Produto {i}")
    print(f"Código......: {produto.codigo}")
    print(f"Descrição...: {produto.descricao}")
    print(f"CX em KG....: {produto.cx_kg}")
    print(f"Volume......: {produto.volume}")
    print(f"Venda.......: R$ {produto.venda:.2f}")
    print(f"Total.......: R$ {produto.venda_total:.2f}")
    print(f"Comissão....: R$ {produto.comissao:.2f}")
    print("-" * 40)