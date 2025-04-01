import pandas as pd

class OperadorasModel:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path, encoding='utf-8')

    def buscar(self, termo):
        if not termo:
            return []
        return self.df[
            self.df.apply(lambda row: row.astype(str).str.lower().str.contains(termo.lower()).any(), axis=1)
        ].to_dict('records')