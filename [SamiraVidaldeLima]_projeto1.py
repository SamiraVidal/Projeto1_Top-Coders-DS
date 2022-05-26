import json
import os.path
import sys


def obter_dados():
    
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados


def listar_categorias(dados: list):
    
    lista_de_categoria = []

    for elemento in dados:

        if elemento ['categoria'] not in lista_de_categoria:
            lista_de_categoria.append(elemento['categoria'])  
    
    return lista_de_categoria

    
def listar_por_categoria(dados: list, categoria: str):
    
    produto_por_categoria = []

    for elemento in dados:
        if elemento['categoria'] == categoria:
            produto_por_categoria.append(elemento)
    return produto_por_categoria
  
  
def produto_mais_caro(dados: list, categoria: str):
           
    maior_preco = float(dados[0]['preco'])

    for elemento in dados:
        
        if float(elemento['preco']) > maior_preco and elemento['categoria'] == categoria:
            maior_preco = float(elemento['preco'])
            produto_caro = elemento
    return produto_caro 
  

def produto_mais_barato(dados: list, categoria: str):
    
    menor_preco = float(dados[0]['preco'])

    for elemento in dados:

        if float(elemento['preco']) < menor_preco and elemento['categoria'] == categoria:
            menor_preco = float(elemento['preco'])
            produto_barato = elemento
    return produto_barato
  

def top_10_caros(dados: list):
        
    mais_caro = sorted(dados, key = lambda x: float(x['preco']), reverse = True)[0:10] 
    
    return mais_caro   
     

def top_10_baratos(dados: list):    

    mais_barato = sorted(dados, key = lambda x: [float(x['preco'])])[0:10]       
       
    return  mais_barato

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

    lista_opcoes = ['Sair', 'Listar categorias', 'Listar produtos de uma categoria', 'Produto mais caro por categoria',
    'Produto mais barato por categoria','Top 10 produtos mais caros','Top 10 produtos mais baratos']
    
    numero_opcao = 0
    cabecalho('MENU DE OPÇÕES')
    for item in lista_opcoes:
       print(f'{numero_opcao} - {item}')
       numero_opcao += 1
    print(linha())


def exibir_opcao_selecionada (lista: list, indice: int) -> str:

    opcao_selecionada = print(f'\n{lista[indice].center(80).upper()}')

    return opcao_selecionada


def valilar_categoria(lista):

    categoria = input('\nDigite a categoria desejada: ').lower().strip()    

    while categoria not in lista:
        
        categoria = input('\nCategoria inválida e/ou inexistente!\nDigite novamente a categoria desejada: ').lower().strip()    

    return categoria


def menu(dados) -> None:
    
    lista_opcoes = ['Sair', 'Listar categorias', 'Listar produtos de uma categoria', 'Produto mais caro por categoria',
    'Produto mais barato por categoria','Top 10 produtos mais caros','Top 10 produtos mais baratos']

    opcao_usuario = type(int)
    
    while opcao_usuario != 0:
        
        menu_opcoes()
        opcao_usuario = input('\nDigite a opção desejada: ').strip()
        if opcao_usuario.isdigit():
            opcao_usuario= int(opcao_usuario)
        linha()

        lista_categoria = listar_categorias(dados)       
           
        if opcao_usuario == 1:

            exibir_opcao_selecionada(lista_opcoes, opcao_usuario)                    
            categoria_ordenada = sorted(listar_categorias(dados))
            
            for i in range(1, len(categoria_ordenada)- 1):
                print(f'{i} - {str(categoria_ordenada[i].capitalize())}')
            
        elif opcao_usuario == 2:

            exibir_opcao_selecionada(lista_opcoes, opcao_usuario)  
            categoria = valilar_categoria(lista_categoria)              
            listagem_por_categoria = listar_por_categoria(dados, categoria)

            for i in range(0, len(listagem_por_categoria)):
                imprimir_dicionario(listagem_por_categoria[i])

        elif opcao_usuario == 3:   

            exibir_opcao_selecionada(lista_opcoes, opcao_usuario)
            categoria = valilar_categoria(lista_categoria)
            maior_preco = produto_mais_caro(dados, categoria)
            imprimir_dicionario(maior_preco)

        elif opcao_usuario == 4:

            exibir_opcao_selecionada(lista_opcoes, opcao_usuario)
            categoria = valilar_categoria(lista_categoria)   
            menor_preco = produto_mais_barato(dados, categoria)
            imprimir_dicionario(menor_preco)

        elif opcao_usuario == 5:

            exibir_opcao_selecionada(lista_opcoes, opcao_usuario)
            top_10 = top_10_caros(dados)
            
            for i in range(0, 10):            
                imprimir_dicionario(top_10[i])

        elif opcao_usuario == 6:

            exibir_opcao_selecionada(lista_opcoes, opcao_usuario)
            top_10 = top_10_baratos(dados) 
            
            for i in range(0, 10):               
                imprimir_dicionario(top_10[i])

        elif opcao_usuario == 0:

            print('\nSAINDO...\n\nPROGRAMA FINALIZADO COM SUCESSO!\n')

        else:

            print()
            print(f'OPÇÃO INVÁLIDA! TENTE NOVAMENTE..\n')

...

# Programa Principal - não modificar!
dados = obter_dados()
menu(dados)







