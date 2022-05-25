import json
import os.path
import sys


def obter_dados():
    
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados


def listar_categorias(dados: list):
    
    listaDeCategoria = []

    for elemento in dados:
        if elemento ['categoria'] not in listaDeCategoria:
            listaDeCategoria.append(elemento['categoria'])  
    return listaDeCategoria
    
  
def valilar_categoria(lista):

    categoria = input('\nDigite a categoria desejada: ').lower().strip()

    while categoria not in lista:
        if categoria in lista:
            pass
        else:
            categoria = input('\nDigite a categoria desejada: ').lower().strip()
            
    return categoria    

    
def listar_por_categoria(dados: list, categoria: str):
    
    produtoPorCategoria = []

    for elemento in dados:
        if elemento['categoria'] == categoria:
            produtoPorCategoria.append(elemento)
    return produtoPorCategoria
  
  
def produto_mais_caro(dados: list, categoria: str):
           
    maiorPreco = float(dados[0]['preco'])

    for elemento in dados:
        
        if float(elemento['preco']) > maiorPreco and elemento['categoria'] == categoria:
            maiorPreco = float(elemento['preco'])
            produtoMaisCaro = elemento
    return produtoMaisCaro 
  

def produto_mais_barato(dados: list, categoria: str):
    
    menorPreco = float(dados[0]['preco'])

    for elemento in dados:

        if float(elemento['preco']) < menorPreco and elemento['categoria'] == categoria:
            menorPreco = float(elemento['preco'])
            produtoMaisBarato = elemento
    return produtoMaisBarato
  

def top_10_caros(dados: list):
        
    maisCaro = sorted(dados, key = lambda x: float(x['preco']), reverse = True)  
    
    return maisCaro[0:10]     
     

def top_10_baratos(dados: list):    

    maisBarato = sorted(dados, key = lambda x: [float(x['preco'])])        
       
    return  maisBarato[0:10]

def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def imprimir_dicionario(dicionario: dict):


    print(f'\nID: {dicionario["id"]}')
    print(f'PREÇO: R$ {dicionario["preco"]}')
    print(f'CATEGORIA: {str(dicionario["categoria"]).capitalize()}')
      

def menu_opcoes():

    listaOpcoes = ['Sair', 'Listar categorias', 'Listar produtos de uma categoria', 'Produto mais caro por categoria',
    'Produto mais barato por categoria','Top 10 produtos mais caros','Top 10 produtos mais baratos']
    
    numero_opcao = 0
    cabecalho('MENU DE OPÇÕES')
    for item in listaOpcoes:
       print(f'{numero_opcao} - {item}')
       numero_opcao += 1
    print(linha())


def exibir_opcao_selecionada (lista: list, indice: int) -> str:

    opcaoSelecionada = print(f'\n{lista[indice].center(80).upper()}')

    return opcaoSelecionada


def valilar_categoria(lista):

    categoria = input('\nDigite a categoria desejada: ').lower().strip()    

    while categoria not in lista:

        categoria = input('\nCategoria inválida/Inexistente! Digite novamente a categoria desejada: ').lower().strip()    

    return categoria


def menu(dados) -> None:
    
    listaOpcoes = ['Sair', 'Listar categorias', 'Listar produtos de uma categoria', 'Produto mais caro por categoria',
    'Produto mais barato por categoria','Top 10 produtos mais caros','Top 10 produtos mais baratos']

    opcaoUsuario = type(int)
    
    while opcaoUsuario != 0:
        
        menu_opcoes()
        opcaoUsuario = input('\nDigite a opção desejada: ').strip()
        if opcaoUsuario.isdigit():
            opcaoUsuario= int(opcaoUsuario)
        linha()

        listaCategoria = listar_categorias(dados)       
           
        if opcaoUsuario == 1:

            exibir_opcao_selecionada(listaOpcoes, opcaoUsuario)                    
            categoriaOrdenada = sorted(listar_categorias(dados))
            
            for i in range(1, len(categoriaOrdenada)- 1):
                print(f'{i} - {str(categoriaOrdenada[i].capitalize())}')
            
        elif opcaoUsuario == 2:

            exibir_opcao_selecionada(listaOpcoes, opcaoUsuario)  
            categoria = valilar_categoria(listaCategoria)              
            listagemPorCategorias = listar_por_categoria(dados, categoria)

            for i in range(0, len(listagemPorCategorias)):
                imprimir_dicionario(listagemPorCategorias[i])

        elif opcaoUsuario == 3:   

            exibir_opcao_selecionada(listaOpcoes, opcaoUsuario) 

            categoria = valilar_categoria(listaCategoria)
            maior_preco = produto_mais_caro(dados, categoria)
            imprimir_dicionario(maior_preco)

        elif opcaoUsuario == 4:

            exibir_opcao_selecionada(listaOpcoes, opcaoUsuario)
            categoria = valilar_categoria(listaCategoria)   
            menor_preco = produto_mais_barato(dados, categoria)
            imprimir_dicionario(menor_preco)

        elif opcaoUsuario == 5:

            exibir_opcao_selecionada(listaOpcoes, opcaoUsuario)
            top_10 = top_10_caros(dados)
            for i in range(0, 10):            
                imprimir_dicionario(top_10[i])

        elif opcaoUsuario == 6:

            exibir_opcao_selecionada(listaOpcoes, opcaoUsuario)
            top_10 = top_10_baratos(dados) 
            for i in range(0, 10):               
                imprimir_dicionario(top_10[i])

        elif opcaoUsuario == 0:

            print('\nSAINDO...\n\nPROGRAMA FINALIZADO COM SUCESSO!\n')

        else:

            print()
            print(f'OPÇÃO INVÁLIDA! TENTE NOVAMENTE..\n')

...

# Programa Principal - não modificar!
dados = obter_dados()
menu(dados)







