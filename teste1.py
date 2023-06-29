# Recomendações:
# - Não alterar os trechos de código que estejam entre os comentários # NÃO ALTERAR #
# - Desenvolver o código entre os trechos de comentário # DESENVOLVIMENTO - TESTE #
# - É recomendado realizar a verificação/teste/execução do código várias vezes, para garantir o funcionamento
# '------------------------------------------------------------------------------------------------------'

teste = ''' TESTE 1 - TRATAMENTO DE DADOS DINÂMICOS (FÁCIL)
TESTE: Criar uma FUNÇÃO para tratar e converter datas para o formato americano AAAA-MM-DD.
A função deve estar apta a converter qualquer tipo de data exemplificados na lista_datas_outros_formatos
Pode/deve-se utilizar um FOR para realizar o teste da função com os valores contidos na lista_datas_outros_formatos '''


# #CÓDIGO ESTÁTICO - NÃO ALTERAR #
DATAS_PARA_TRATAR = [
    '30/11/2022',
    '01 dez 2022', 
    '25/12/2022', 
    '31 de dezembro de 2022'
]
# #CÓDIGO ESTÁTICO - NÃO ALTERAR #


# '---------------------------------------------------DESENVOLVIMENTO - TESTE 1---------------------------------------------------'
from datetime import datetime 

# Dicionario para buscar os meses abreviados
meses_abrv = {
    'jan': '01',
    'fev': '02',
    'mar': '03',
    'abr': '04',
    'mai': '05',
    'jun': '06',
    'jul': '07',
    'ago': '08',
    'set': '09',
    'out': '10',
    'nov': '11',
    'dez': '12'
}

# Dicionario para buscar os meses
meses = {
    'janeiro': '01',
    'fevereiro': '02',
    'março': '03',
    'abril': '04',
    'maio': '05',
    'junho': '06',
    'julho': '07',
    'agosto': '08',
    'setembro': '09',
    'outubro': '10',
    'novembro': '11',
    'dezembro': '12'
}

for data_i in DATAS_PARA_TRATAR:   
    # Identificar os meses inscritos com padrão de barra EX: 01/01/2023
    if '/' in data_i:
        data = datetime.strptime(data_i, "%d/%m/%Y")
        data_formatada = data.strftime("%Y/%m/%d")
        print(data_formatada)
    else:
       # Identificar os meses inscritos com meses abreviados
       if len(data_i.split()) == 3:
        partes = data_i.split()
        dia = partes[0]
        mes = meses_abrv.get(partes[1].lower())
        ano = partes[2]
        data = f"{ano}/{mes}/{dia}"
        print(data)
        # Identificar os meses inscritos com meses completo
       else:
        partes = data_i.split()
        dia = partes[0]
        mes = meses.get(partes[2].lower())
        ano = partes[4]
        data = f"{ano}/{mes}/{dia}"
        print(data)
   

# '---------------------------------------------------DESENVOLVIMENTO - TESTE 1---------------------------------------------------'
# EXEMPLO: 30/11/2022 DEVE SE TORNAR 2022-11-30