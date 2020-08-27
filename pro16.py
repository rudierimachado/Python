#coding utf-8
#---------------------------------------------
#  Um programa que recebe um valor fracionado 
#  e retorna a sua porção inteira.
#---------------------------------------------
#  Ex: valor = 3.21
#  O valor inteiro de 3.21 é 3 
#---------------------------------------------
#  Quebrando um Número - Exercício #016
#---------------------------------------------
import math

num = float(input('Digite um valor fracionado: '))



print(f'O valor digitado foi {num}, e sua porção inteira é {math.trunc(num)}')



