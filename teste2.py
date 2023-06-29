# Recomendações:
# - Não alterar os trechos de código que estejam entre os comentários # NÃO ALTERAR #
# - Desenvolver o código entre os trechos de comentário # DESENVOLVIMENTO - TESTE #
# - É recomendado realizar a verificação/teste/execução do código várias vezes, para garantir o funcionamento
# '------------------------------------------------------------------------------------------------------'

teste = ''' TESTE 2 - VERIFICAÇÃO DE ARQUIVOS (FÁCIL)
TESTE: Criar uma FUNÇÃO que lista os arquivos de um diretório e verifica se todos se algum ultrapassa o limite de 3 MB
Se algum arquivo ultrapassar o limite de 3MB retornar False, se todos os arquivos estiverem abaixo do limite retornar True
'''

# '---------------------------------------------------DESENVOLVIMENTO - TESTE 2---------------------------------------------------'
import os

def lista_de_arquivos(diretorio):
    for arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        tamanho = os.path.getsize(caminho_arquivo) / (1024 * 1024)
        if tamanho > 3:
            return False
    return True
print("Diretorio com arquivo menores que 3MB:")
print(lista_de_arquivos("diretorio_t2/diretoria_true"))
print("Diretorio com arquivo maiores que 3MB:")
print(lista_de_arquivos("diretorio_t2/diretorio_false"))
# '---------------------------------------------------DESENVOLVIMENTO - TESTE 2---------------------------------------------------'
