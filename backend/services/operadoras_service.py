from ..models.operadoras_model import OperadorasModel

class OperadorasService:
    def __init__(self, csv_path):
        self.model = OperadorasModel(csv_path)

    def buscar_operadoras(self, termo):
        return self.model.buscar(termo)[:10]  # 0-10 result