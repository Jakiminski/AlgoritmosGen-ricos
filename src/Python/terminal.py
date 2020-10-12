#!/usr/bin/env python
# coding: utf-8

import os
'''
clear()

Limpa console/terminal, independente do Sistema Operacional utilizado
ARGS: None
RETURN: None
'''

def clear():
	os.system('cls' if os.name=='nt' else 'clear') # cls for Windows, clear for other OS
	pass
