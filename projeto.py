# linha = ''
# for coluna in colunas:
#     linha = linha + f'{coluna},'
# print(linha[0:-1])

# nome
# titulo
# data_nasc
# mae
# pai
import os
import voto
from datetime import date, datetime


NOME = 0
MAE = 1
PAI = 2
NASCIMENTO = 3
TITULO = 4
VOTOU = 5
ANO_ATUAL = 2020

substituicoes = ['$NOME$',
    '$MAE$',
    '$PAI$',
    '$NASC$',
    '$TITULO$',
]

def solicitar_dados():
    nome = input('Nome: ')
    mae = input('Nome da mãe: ')
    pai = input('Nome do pai: ')
    nascimento = input('Data de Nascimento: ')
    titulo = input('Título de eleitor: ')
    votou = input('Votou na última eleição? (S/N)')
    dados = (nome, mae, pai, nascimento, titulo, votou)
    return dados

def solicitar_dados_busca():
    nome = input('Nome: ')
    titulo = input('Título de eleitor: ')
    dados = (nome, titulo)
    return dados

# TODO: zona;secao;municipio;uf;data_insc;
# nome;mae;pai;data_nasc;titulo;votou
def criar_base_dados(caminho):
    colunas = ['nome', 'mae', 'pai', 'data_nasc', 'titulo', 'votou']
    # primeira vez que abrir o arquivo
    arquivo = open(caminho, 'w')
    linha = ','.join(colunas)
    arquivo.write(linha + '\n')
    arquivo.writelines(linha)
    arquivo.close()

def cadastrar_eleitor(dados, caminho):
    # modo 'a' permite adicionar no arquivo
    arquivo = open(caminho, 'a')
    arquivo.write(','.join(dados) + '\n')
    arquivo.close()
    print('Eleitor cadastrado com Sucesso!')

def localizar_eleitor(dados, caminho):
    # abrir arquivo para leitura
    arquivo = open(caminho)
    linhas = arquivo.readlines()
    arquivo.close()
    for linha in linhas:
        dados_eleitor = linha.strip().split(',')
        # Se nome e o título forem iguais, assumimos que a linha é igual
        if (dados[0] == dados_eleitor[NOME] 
            and dados[1] == dados_eleitor[TITULO]):
            # encontramos o usuário na base
            return dados_eleitor
    # não encontramos o eleitor
    return []

caminho = os.path.join('dados', 'base_eleitores.csv')
# Se o arquivo não existe, cria
if not os.path.exists(caminho):
    criar_base_dados(caminho)

# dados_eleitor = solicitar_dados()
# cadastrar_eleitor(dados_eleitor, caminho)
# Solicitar dados para buscar na base

dados = solicitar_dados_busca()
dados_eleitor = localizar_eleitor(dados, caminho)

if dados_eleitor:
    print(dados_eleitor)
    # 'dd/mm/aaaa'
    data_nascimento = dados_eleitor[NASCIMENTO]
    # ['dd', 'mm', 'aaaa']
    partes = data_nascimento.split('/')
    # compreesão de listas - converter pra inteiro
    partes = [int(d) for d in partes]
    data = date(day=partes[0], month=partes[1], year=partes[2])
    # estima a idade do eleitor
    idade = int((date.today() - data).days/365)
    # usar programa é obrigado a votar
    if voto.situacao_voto(idade) == voto.PROIBIDO:
        print(f'Com {idade} anos, seu voto é proibido')
    elif (voto.situacao_voto(idade) == voto.OBRIGATORIO 
            and dados_eleitor[VOTOU] == 'N'):
        print('VOCÊ NÃO ESTÁ QUITE!!!!!')
    else:
        # emitir a certidão
        arquivo = open('certidao.html', 'r')
        conteudo = arquivo.read()
        arquivo.close()
        for i in range(len(substituicoes)):
            conteudo = conteudo.replace(substituicoes[i], 
                                    dados_eleitor[i])

        # Substituir data e hora:
        agora = datetime.now()
        conteudo = conteudo.replace('$DATA$', 
                    agora.date().strftime('%d/%m/%Y'))
        conteudo = conteudo.replace('$HORA$', 
                    str(agora.time().strftime('%H:%M:%S')))
        # datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        arquivo = open('certidao_emitida.html', 'w')
        arquivo.write(conteudo)
        arquivo.close()
        print("Certidão Emitida com Sucesso")
else:
    print('Eleitor(a) NÃO cadastrado(a)')
    


