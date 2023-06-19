from pydantic import BaseModel


class ComentarioSchema(BaseModel):
    """ Define como um novo comentário a ser inserido deve ser representado
    """
    produto_id: int = 1
    texto: str = "Compre somente se o preço estiver bom!"
    