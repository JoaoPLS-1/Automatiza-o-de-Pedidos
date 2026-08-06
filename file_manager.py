from pathlib import Path
import shutil


class FileManager:

    def listar_pdfs(self, pasta):
        return sorted(Path(pasta).glob("*.pdf"))

    def mover(self, origem, destino):

        destino.mkdir(exist_ok=True)

        shutil.move(str(origem), str(destino / origem.name))