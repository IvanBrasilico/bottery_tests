# -*- coding: utf-8 -*-
'''Views customizadas que poderão fazer parte do código-base do bottery
'''
import json
import urllib.request
import aiohttp


ULRAPP = 'http://brasilico.pythonanywhere.com/_lacre/'
STATUS = ['OK', 'Divergente', 'Sem Lacre']


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def http_async_get_read(url):
    '''Default function for assincronous http access'''
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
    return html

def two_tokens(text):
    '''Receives a text string, splits on first space, return
    first word of list/original sentence and the rest of the sentence
    '''
    lista = text.split(' ')
    return lista[0], " ".join(lista[1:])
