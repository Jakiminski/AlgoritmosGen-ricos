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


'''
isPrime(n)

Indica se um número 'n' é primo ou não
ARGS: int n
	n >= 0
RETURN: bool
	Retorna 'True' caso n seja número primo, senão retorna 'False'

'''
def isPrime(n):
	# É divisível só por 1 e ele mesmo?
	assert()
	div = 0 # Quantidade de divisores desse número
	for i in range(1,n+1): # n+1 devido range(a,b) compreende [a..b-1]
		if n%i==0:
			div += 1
	#print(div)
	return True if div==2 else False