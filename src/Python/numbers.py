#!/usr/bin/env python
# coding: utf-8

'''
isPrime(n)

Indica se um número 'n' é primo ou não

ARGS: int 'n'
	n >= 0
RETURN: bool
	Retorna 'True' caso n seja número primo, senão retorna 'False'

'''
def isPrime(n):
	# É divisível só por 1 e ele mesmo?
	assert(n>0)
	div = 0 # Quantidade de divisores desse número
	for i in range(1,n+1): # n+1 devido range(a,b) compreende [a..b-1]
		if n%i==0:
			div += 1
	#print(div)
	return True if div==2 else False

'''
log(a,b)

Calcula o piso do logarítmo, retornando sempre um valor inteiro

ARGS: int 'a', int 'b'
	'a' é o número que extraímos o logarítmo. 'b' é a base do logarítmo.
	a >0, b > 1
RETURN: int 'result'
	Retorna o resultado do logarítmo.

'''
def log(a,b):
	assert(a>0 and b>1)
    result = 0
    quo = a
    while (quo>b-1):
        
        quo = math.floor(quo/b)
        result += 1
     #print(quo)
        #print('log{} {} = {}'.format(b,a,result))
    return result
