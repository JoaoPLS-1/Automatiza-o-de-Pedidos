from pathlib import Path

# ------------------------
# Versão do sistema
# ------------------------
VERSAO = "1.0.0"

# ------------------------
# Pastas
# ------------------------
BASE_DIR = Path(__file__).parent

PASTA_PEDIDOS = BASE_DIR / "pedidos"
PASTA_IMPORTADOS = BASE_DIR / "importados"
PASTA_PLANILHAS = BASE_DIR / "planilhas_geradas"
PASTA_ERROS = BASE_DIR / "erros"
PASTA_LOGS = BASE_DIR / "logs"
PASTA_MODELOS = BASE_DIR / "modelos"

# ------------------------
# Modelo Excel
# ------------------------
MODELO_EXCEL = PASTA_MODELOS / "MODELO.xlsx"

# ------------------------
# Dados Fixos
# ------------------------
FATURADO_POR = "FRIGORIFICO VISCONDE"

# Comissão
COMISSAO = 0.01

# Linha onde começam os produtos
LINHA_INICIAL = 2



# Limpeza de memória
LIMPAR_MEMORIA_CADA = 10

# Colunas
COL_LOJA = 1
COL_DESCRICAO = 2
COL_CXKG = 3
COL_VOLUME = 4
COL_VENDA = 6