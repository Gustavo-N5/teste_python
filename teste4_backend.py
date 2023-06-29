# Recomendações:
# - Não alterar os trechos de código que estejam entre os comentários # NÃO ALTERAR #
# - Desenvolver o código entre os trechos de comentário # DESENVOLVIMENTO - TESTE #
# - É recomendado realizar a verificação/teste/execução do código várias vezes, para garantir o funcionamento
# - TODOS OS PROCESSOS SÃO DE ACESSO PÚBLICO E TIVERAM AUTORIZAÇÃO DE SUAS PARTES
# '------------------------------------------------------------------------------------------------------'

teste = ''' AUTOMAÇÃO SELENIUM - Consulta Pública ESAJ-SP (DIFÍCIL - BACKEND)
TESTE: Desenvolver uma automação selenium para realizar consultas públicas no portal ESAJ-SP
Cada consulta deve montar um dicionário final

Passo a passo da automação:
1. abrir o site
2. clicar no botão rádio Outros
3. Digitar o nº do processo listado abaixo na caixa input
4. Clicar no botão Consultar
5. Verificar se o processo foi ou não encontrado (há mensagem de erro)
6. Caso tenha sido encontrado, coletar as seguintes informações: (para localizar basta pesquisar por esse texto no site)
    - numero_processo
    - classe
    - assunto
    - foro
    - vara
    - Reqte 
    - Reqdo
7. Organizar os dados acima em um dicionário e printá-lo
'''

# # CÓDIGO ESTÁTICO - NÃO ALTERAR #
URL_PORTAL = 'https://esaj.tjsp.jus.br/cpopg/open.do'
LISTA_PROCESSOS = [
    '0000622-07.2022.8.26.0003',
    '1035157-25.2021.8.26.0602',
    '1093123-72.2021.8.26.0529',
    '1011882-72.2021.8.26.0529',
    '0806733-22.2016.8.15.0251',
    '1005551-62.2021.8.26.0048',
    '1000891-61.2021.8.26.0424'
]
# # CÓDIGO ESTÁTICO - NÃO ALTERAR #


# '---------------------------------------------------DESENVOLVIMENTO - TESTE 7---------------------------------------------------'
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Para facilitar coloquei os elementos Xpath em um dicionario 
elementos ={
    "botoes":{
        "consulta":{
            "xpath":"/html/body/div[2]/form/section/div[4]/div/input"
        },
        "busca_processo":{
            "xpath":"/html/body/div[2]/form/section/div[2]/div/div[1]/div[1]/span[2]/input"
        },
        "outros":{
            "xpath":"/html/body/div[2]/form/section/div[2]/div/div[1]/div[1]/div/fieldset/input[2]"
        },
        "numero_processo":{
            "xpath":"/html/body/div[1]/div[2]/div/div[1]/div/span[1]"
        },
        "classe":{
            "xpath":"/html/body/div[1]/div[2]/div/div[2]/div[1]/div/span"
        },
        "assunto":{
            "xpath":"/html/body/div[1]/div[2]/div/div[2]/div[2]/div/span"
        },
        "foro":{
            "xpath":"/html/body/div[1]/div[2]/div/div[2]/div[3]/div/span"
        },
        "vara":{
            "xpath":"/html/body/div[1]/div[2]/div/div[2]/div[4]/div/span"
        },
        "reqte":{
            "xpath":"/html/body/div[2]/table[1]/tbody/tr[1]/td[2]"
        },
        "reqdo":{
            "xpath":"/html/body/div[2]/table[1]/tbody/tr[2]/td[2]"
        }
    }
}

driver = webdriver.Chrome()
driver.maximize_window()

def buscar_processo(num_processo):
    
    try:   
        # Buscar a pagina no chrome
        driver.get(URL_PORTAL)

        # Clicar no botão outros
        driver.find_element(By.XPATH, elementos["botoes"]["outros"]["xpath"]).click()

        # Preencehendo campo para fazer a busca do processo
        driver.find_element(By.XPATH, elementos["botoes"]["busca_processo"]["xpath"]).send_keys(num_processo)

        # clicar mo botão consulta
        driver.find_element(By.XPATH,elementos["botoes"]["consulta"]["xpath"]).click()

        # buscar elesmentos 
        numero_processo = driver.find_element(By.XPATH, elementos["botoes"]["numero_processo"]["xpath"]).text
        classe = driver.find_element(By.XPATH, elementos["botoes"]["classe"]["xpath"]).text
        assunto = driver.find_element(By.XPATH, elementos["botoes"]["assunto"]["xpath"]).text
        foro = driver.find_element(By.XPATH, elementos["botoes"]["foro"]["xpath"]).text
        vara = driver.find_element(By.XPATH, elementos["botoes"]["vara"]["xpath"]).text
        reqte = driver.find_element(By.XPATH, elementos["botoes"]["reqte"]["xpath"]).text
        reqdo = driver.find_element(By.XPATH, elementos["botoes"]["reqdo"]["xpath"]).text
        
        # Armazenando o processo em um dicionario
        processo ={
            "numero_processo":numero_processo,
            "classe":classe,
            "assunto": assunto,
            "foro":foro,
            "vara":vara,
            "reqte":reqte,
            "reqdo":reqdo
        }

        # Printando o dicionario 
        print(processo)

        time.sleep(2)

    except:
        print("Processo não encontrado")
    

for processo in LISTA_PROCESSOS:
    print("-" * 20)
    buscar_processo(processo)
    print("-" * 20)

# '---------------------------------------------------DESENVOLVIMENTO - TESTE 7---------------------------------------------------'
