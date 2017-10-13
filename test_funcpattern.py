#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 09:18:39 2017

@author: ivan
"""
from bottery.message import Message
from patterns import FuncPattern


def test_pattern_instance():
    def view(): return 'Hello world'

    def pre_process(message): return 'Hello', 'World'
    pattern = FuncPattern('cc', view, pre_process)
    assert pattern.pattern == 'cc'
    assert pattern.view == view
    assert pattern.pre_process == pre_process


def test_pattern_check_right_message():
    '''
    Check if Pattern class return the view when message checks with
    pattern.
    '''
    def view(message): return 'Hello World'

    def pre_process(message): return 'cc', 'MM'
    pattern = FuncPattern('cc', view, pre_process)
    message = type('Message', (object,), {'text': 'cc MM'})
    result = pattern.check(message)
    assert result == 'Hello World'


def test_pattern_check_wrong_message():
    '''
    Check if Pattern class returns False when message doesn't
    check with pattern.
    '''
    def view(): return 'Hello world'

    def pre_process(message): return 'ping', 'pong'
    pattern = FuncPattern('cc', view, pre_process)
    message = type('Message', (object,), {'text': 'ping pong'})
    assert not pattern.check(message)
