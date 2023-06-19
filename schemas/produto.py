from pydantic import BaseModel
from typing import Optional, List
from model.produto import Produto

from schemas import ComentarioSchema


class ProdutoSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    nome: str = "Guitarra Elétrica Gibson"
    quantidade: Optional[int] = 3
    valor: float = 5000.00


class ProdutoViewSchema(BaseModel):
    """ Define como um produto será retornado: produto + comentários
    """
    id: int = 1
    nome: str = "Guitarra Elétrica Gibson"
    quantidade: Optional[int] = 3
    valor: float = 5000.00
    total_comentarios: int = 1
    comentarios:List[ComentarioSchema]    
    

def apresenta_produto(produto: Produto):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": produto.id,
        "nome": produto.nome,
        "quantidade": produto.quantidade,
        "valor": produto.valor,
        "total_comentarios": len(produto.comentarios),
        "comentarios": [{"texto": c.texto} for c in produto.comentarios]
    }