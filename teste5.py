# Recomendações:
# - Não alterar os trechos de código que estejam entre os comentários # NÃO ALTERAR #
# - Desenvolver o código entre os trechos de comentário # DESENVOLVIMENTO - TESTE #
# - É recomendado realizar a verificação/teste/execução do código várias vezes, para garantir o funcionamento
# '------------------------------------------------------------------------------------------------------'
# Exemplo da lista aleatória gerada e atribuída a variável lista_aleatoria
# lista_aleatoria = ['v', 'U', 'S', 'a', 'A', 'X', 'v', 'q', 'M', 'f', 'y', 'r', 'N', 'u', 'G', 'b', 'u', 'w', 'i', 'w', 's', 'V', 'l', 'Z', 'n', 'c', 'H', 'm', 'o', 'n', 'm', 'A', 'c', 'c', 'y', 'j', 'o', 'x', 'h', 'r', 'V', 'h', 'l', 'w', 'C', 'V', 'h', 'q', 'u', 'W', 'd', 'p', 'V', 't', 'w', 'd', 'I', 'R', 'R', 58, 'h', 'Q', 'm', 'S', 'J', 'g', 'X', 'P', 'e', 'S', 'H', 'D', 'h', 'U', 'v', 'R', 'W', 'L', 'j', 'Q', 'P', 'k', 'k', 'l', 'I', 'T', 'y', 'U', 'G', 'L', 'U', 'I', 'N', 'e', 'b', 'l', 'k', 'G', 'k', 'b', 'l']
# '------------------------------------------------------------------------------------------------------'

teste = ''' TESTE 5 - ESTRUTURA LÓGICA (DIFÍCIL)
Esse teste simula uma situação problema, que deve ser executada obrigatoriamente, mesmo em um cenário de erros múltiplos;
A situação problema abaixo é uma simulação, devendo se realizar a conversão de um elemento aleatório contido na lista em um número inteiro (ex.: colhemos vários conteúdos de um site, precisamos interagir apenas com o conteúdo numérico);

TESTE: Montar uma estrutura lógica que garanta a execução do print contido no trecho de desenvolvimento, sem alterar o seu conteúdo
Obs.: O print não pode ser mexido, apenas colocado dentro de estruturas lógicas tipo if/for/while/try/etc...'''

# # CÓDIGO ESTÁTICO - NÃO ALTERAR #
import string
import random
caracteres = string.ascii_lowercase+string.ascii_uppercase
lista_aleatoria = [random.choice(caracteres) for i in range(100)]
lista_aleatoria.insert(random.randint(0, 99), random.randint(0, 100))
# # CÓDIGO ESTÁTICO - NÃO ALTERAR #

# '---------------------------------------------------DESENVOLVIMENTO - TESTE 3---------------------------------------------------'

print(int(lista_aleatoria[random.randint(0, len(lista_aleatoria)-1)])) # NÃO ALTERAR O CÓDIGO, APENAS O SEU LOCAL!!! PRINTA UM ELEMENTO ALEATÓRIO DA LISTA CONVERTIDO PARA O TIPO INT()

# '---------------------------------------------------DESENVOLVIMENTO - TESTE 3---------------------------------------------------'