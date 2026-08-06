import re


def limpar_nome_arquivo(nome):

    proibidos = r'[\\/:*?"<>|]'

    return re.sub(proibidos, "", nome).strip()