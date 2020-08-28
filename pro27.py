#coding: utf-8
#----------------------------------------------------------------
#  Um programa que recebe um nome inteiro e retorna o primeiro 
#  e último nome separadamente.
#----------------------------------------------------------------
#  Primeiro e último nome - Exercício #027
#----------------------------------------------------------------

nome = str(input('Digite seu nome: ')).split()

print('Muito prazer em te conhecer!')
print(f'Se entendi bem seu primeiro nome é: {nome[0].title()}')
print(f'E seu último nome é: {nome[-1].title()}.. certo?')



