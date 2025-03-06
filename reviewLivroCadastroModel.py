class ReviewLivroCadastroModel:
    #todo adicionar uma data de inclusao
    def __init__(self, id:int = None, titulo:str = None, review:str = None):
        self.id = id
        self.titulo = titulo
        self.review = review

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            titulo=data.get("titulo"),
            review=data.get("review")
        )
