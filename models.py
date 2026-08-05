from dataclasses import dataclass, field


@dataclass
class Produto:
    codigo: str
    descricao: str
    cx_kg: float
    volume: float
    venda: float
    venda_total: float

    @property
    def volume_kg(self):
        return self.cx_kg * self.volume

    @property
    def comissao(self):
        return self.venda_total * 0.01


@dataclass
class Pedido:
    numero: str
    codigo_cliente: str
    nome_cliente: str

    prazo_pgto: str
    entrega: str

    vendedor: str

    qtde_itens: int

    produtos: list[Produto] = field(default_factory=list)