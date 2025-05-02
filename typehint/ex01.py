# Tenha um dicionário com 3 produtos e seus respectivos preços.
produtos = {
    'geladeira': 3000,
    'armario': 200,
    'sofa': 700
}

print(produtos['geladeira'])


# Tenha uma função com type hint que receba o nome do produto e o dicionário e retorne o preço do produto.

def retorno_preco_produto(nome:str) -> int:
    return produtos[nome]

print(retorno_preco_produto('armario'))
