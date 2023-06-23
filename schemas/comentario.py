from pydantic import BaseModel


class ComentarioSchema(BaseModel):
    """ Define como um novo comentário a ser inserido deve ser representado
    """
    produto_id: int = 1
    texto: str = "Compre somente se o preço estiver bom!"


class ComentarioBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca.
        Que será feita apenas com base no id do produto.
    """
    produto_id: int = 1


class ComentarioDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    produto_id: int
  