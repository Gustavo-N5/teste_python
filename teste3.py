# Recomendações:
# - Não alterar os trechos de código que estejam entre os comentários # NÃO ALTERAR #
# - Desenvolver o código entre os trechos de comentário # DESENVOLVIMENTO - TESTE #
# - É recomendado realizar a verificação/teste/execução do código várias vezes, para garantir o funcionamento
# '------------------------------------------------------------------------------------------------------'

teste = ''' TESTE 3 - GESTÃO DE LOGS (MÉDIO)
TESTE: Criar uma classe LogTxt com método log;
O método log deve receber um valor inteiro de equivalência de sucesso e uma mensagem, anotando em um arquivo .txt, com data e hora da execução

Ex. de estrutura a ser anotada no log.txt
23/01/2023 09:16:15 > Sucesso > Mensagem recebida como parâmetro do método'''

# # CÓDIGO ESTÁTICO - NÃO ALTERAR #
EQUIVALENCIA_SUCESSO = {
    1: 'Sucesso',
    0: 'Sem Sucesso',
    -1: 'Erro'
}
# # CÓDIGO ESTÁTICO - NÃO ALTERAR #

# '---------------------------------------------------DESENVOLVIMENTO - TESTE 1---------------------------------------------------'


# '---------------------------------------------------DESENVOLVIMENTO - TESTE 1---------------------------------------------------'
# EXEMPLO DE MENSAGEM A SER PRINTADA/ANOTADA NO TXT:
# 2022-12-10 14:05:00 > Sucesso > Mensagem recebida pelo método log