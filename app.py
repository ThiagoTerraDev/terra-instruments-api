from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Produto, Comentario
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Terra Instruments API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo as Tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
produto_tag = Tag(name="Produto", description="Adição, visualização ou remoção de produtos à base")
comentarios_tag = Tag(name="Comentário", description="Adição de um comentário à um produto cadastrado na base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/produto', tags=[produto_tag],
    responses={"200": ProdutoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_produto(form: ProdutoSchema):
    """Adiciona um novo Produto à base de dados

    Retorna uma representação dos produtos e comentários associados.
    """
    produto = Produto(
        nome=form.nome, 
        quantidade=form.quantidade, 
        valor=form.valor)
    logger.debug(f"Adicionando produto de nome: '{produto.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando produto
        session.add(produto)
        # efetivando o comando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionando produto de nome: '{produto.nome}'")
        return apresenta_produto(produto), 200
    
    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Produto de mesmo nome já salvo na base."
        logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"message": error_msg}, 409
    
    except Exception as e:
        # caso ocorra um erro fora do previsto
        error_msg = "Não foi possível salvar novo item."
        logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"message": error_msg}, 400
    

@app.get('/produtos', tags=[produto_tag], 
         responses={"200": ListagemProdutosSchema, "404": ErrorSchema})
def get_produtos():
    """ Faz a busca por todos os Produtos cadastrados
    
    Retorna uma representação da listagem de produtos.
    """
    logger.debug(f"Coletando produtos ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    produtos = session.query(Produto).all()
    
    if not produtos:
        # se não há produtos cadastrados
        return {"produtos": []}, 200
    else:
        logger.debug(f"%d produtos encontrados" % len(produtos))
        # retorna a representação de produto
        print(produtos)
        return apresenta_produtos(produtos), 200

