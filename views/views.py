# -*- coding: utf-8 -*-
'''Views customizadas utilizadas neste projeto
São as funcões que geram o conteúdo para a submissão à
API que o Usuário acessa.
'''
import json
import urllib.request
import aiohttp


ULRAPP = 'http://brasilico.pythonanywhere.com/_lacre/'
STATUS = ['OK', 'Divergente', 'Sem Lacre']
end_hook_list = ['fim', 'end', 'exit', 'sair']

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def http_async_get_read(url):
    ''' TODO Default function for assincronous http access 
    Needs to retrieve the actual bootery session / eventloop / tasks
    Actual implementation dont work'''
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
    return html

def two_tokens(text):
    '''Receives a text string, splits on first space, return
    first word of list/original sentence and the rest of the sentence
    '''
    lista = text.split(' ')
    return lista[0], " ".join(lista[1:])

def consulta_conteiner(message):
    return consulta_api(message, 'container')

def consulta_lacre(message):
    return consulta_api(message, 'lacre')

def consulta_lacre_hook(message):
    try:
        _, param = two_tokens(message.text)
        print('Hooked View Lacre', _, param)
        if param == "":
            return 'Prossiga informando o número do Lacre', True
        response_text = urllib.request.urlopen(ULRAPP + 'lacre/' + param).read()
        resposta = response_text.decode('utf-8')
        json_resposta = json.loads(resposta)
        str_resposta = ""
        for key, value in json_resposta[0].items():
            str_resposta = str_resposta + key + ': ' + value + ' \n '
    except Exception as err:
        print(err)
    return str_resposta, False

def consulta_api(message, resource):
    '''Acessa a API da Aplicação LACRE em pythonanywhere'''
    try:
        command, param = two_tokens(message.text)
        if param == "":
            if command == 'll':
                return 'Erro: informe o número do Lacre'
            return 'Erro: informe o número do Contêiner'

        response_text = urllib.request.urlopen(ULRAPP + resource + '/' + param).read()
        resposta = response_text.decode('utf-8')
        json_resposta = json.loads(resposta)
        str_resposta = ""
        for key, value in json_resposta[0].items():
            str_resposta = str_resposta + key + ': ' + value + ' \n '
    except Exception as err:
        print(err)
    return str_resposta

def report_api(message):
    '''Acessa a API da Aplicação LACR em pythonanywhere'''
    try:
        _, conteiner = two_tokens(message.text)
        conteiner, status = two_tokens(conteiner)
        lstatus = STATUS[int(status)]
        response_text = urllib.request.urlopen(
            ULRAPP + 'add/report?' +
            'container=' + conteiner +
            'status=' + lstatus).read()
        resposta = response_text.decode('utf-8')
        json_resposta = json.loads(resposta)
        str_resposta = ""
        if len(json_resposta) > 0:
            for key, value in json_resposta[0].items():
                str_resposta = str_resposta + key + ': ' + value + ' \n '
        else:
            str_resposta = conteiner + "Adicionado ao relatório."
    except Exception as err:
        print(err)
    return str_resposta

def list_log(message):
    '''Acessa a API da Aplicação LACRE em pythonanywhere'''
    try:
        response_text = urllib.request.urlopen(
            ULRAPP + 'list/log').read()
        resposta = response_text.decode('utf-8')
        json_resposta = json.loads(resposta)
        print(json_resposta)
        str_resposta = ""
        for line in json_resposta:
            for key, value in line.items():
                str_resposta = str_resposta + key + ': ' + value + ' \n '
    except Exception as err:
        print(err)
    return str_resposta

def help_text(message):
    '''Retorna a lista de Patterns/ disponíveis'''
    # TODO Fazer modo automatizado
    lstatus = [str(key) + ': ' + value + ' ' for key, value in list(enumerate(STATUS))]
    str_end_hooh = ', '.join(end_hook_list)
    return  ('log - retorna histórico de consultas \n'
             'cc <Nº contêiner> - pesquisa dados do contêiner\n'
             'll <nº lacre> - pesquisa lacre \n'
             'report <nº conteiner> <status> (status = ' + \
             " ".join(lstatus) + ') - Preenche relatório \n'
            'tec - entra na aplicação TEC \n'
            'moe - entra numa aplicação para conversar com Homer e seus amigos no bar do Moe \n' + \
            str_end_hooh + ' - Sai de uma aplicação \n')


def say_help(message):
    '''Se comando não reconhecido'''
    return 'Não entendi o pedido. \n Digite help para uma lista de comandos.'


def works(message):
    '''Mensagem simples para teste automático se
    a aplicação está no ar'''
    return 'works'
