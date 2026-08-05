from dataclasses import dataclass, field


@dataclass
class Produto:
    codigo: str
    descricao: str
    cx_kg: float
    volume: float
    venda: float
    venda_total: float


@dataclass
class Pedido:
    cliente: str
    prazo_pgto: str
    entrega: str
    qtde_itens: int
    produtos: list[Produto] = field(default_factory=list)