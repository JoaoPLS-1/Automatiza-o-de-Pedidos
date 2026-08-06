class Validator:

    @staticmethod
    def validar(pedido):

        erros = []

        if not pedido.numero:
            erros.append("Número do pedido não encontrado.")

        if not pedido.nome_cliente:
            erros.append("Cliente não encontrado.")

        if len(pedido.produtos) == 0:
            erros.append("Nenhum produto encontrado.")

        if pedido.qtde_itens != len(pedido.produtos):
            erros.append(
                f"Qtde itens PDF = {pedido.qtde_itens} | Produtos encontrados = {len(pedido.produtos)}"
            )

        return erros