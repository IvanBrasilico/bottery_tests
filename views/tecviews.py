# -*- coding: utf-8 -*-
'''Views customizadas utilizadas neste projeto
São as funcões que comunicam com a API da Aplicação TEC
'''
import json
import urllib.request

ULRAPP = 'http://brasilico.pythonanywhere.com/'
ACTIONS = {'rank': '_rank?words=',
           'filtra': '_filter_documents?afilter=',
           'capitulo': '_document_content/'}

def consulta_tec(message):
    '''Acessa a API da Aplicação LACRE em pythonanywhere'''
    try:
        lista = message.text.split(' ')
        if (len(lista) == 1) or (lista[1].strip() == ""):
            return 'Informe o comando: ' + ' - '.join([key for key in ACTIONS]), True
        resource = ACTIONS.get(lista[1])
        if resource is None:
            return 'Comando não reconhecido, saindo... Digite tec para uma lista de comandos', False
        if (len(lista) == 2) or (lista[2].strip() == ""):
            return 'Informe a palavra do filtro: ', True
        params = '%20'.join(lista[2:])
        response_text = urllib.request.urlopen(ULRAPP + resource + params).read()
        resposta = response_text.decode('utf-8')
        json_resposta = json.loads(resposta)
        str_resposta = ""
        for linha_json in json_resposta:
            for key, value in linha_json.items():
                str_resposta = str_resposta + str(key) + ': ' + str(value) + ' \n '
    except Exception as err:
        print('Consulta_tec:', err)
    return str_resposta, False
