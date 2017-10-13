#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 09:18:39 2017

@author: ivan
"""
from views import two_tokens


def test_duas_palavras():
    p1, p2 = two_tokens("duas palavras")
    assert p1 == 'duas'
    assert p2 == 'palavras'


def test_tres_palavras():
    p1, p2 = two_tokens("tres simples palavras")
    assert p1 == 'tres'
    assert p2 == 'simples palavras'
