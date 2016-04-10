#coding: utf-8
import os


def bix(ano):
	if ano <= 0:
		print('\nO ANO DEVE SER MAIOR QUE ZERO\n')
	elif ano % 4 == 0:
		if ano % 1000 == 0:
			print('\nO ANO '+str(ano)+' É BISSEXTO\n')
		elif ano % 400 == 0:
			print('\nO ANO '+str(ano)+' É BISSEXTO\n')
		elif ano % 100 != 0:
			print('\nO ANO '+str(ano)+' É BISSEXTO\n')
		else:
			if ano % 4 == 0 and ano % 100 == 0:
				print('\nO ANO '+str(ano)+' NÃO É BISSEXTO\n')
	else:
		print('\nO ANO '+str(ano)+' NÃO É BISSEXTO\n')

while True:
	anoo = int(input('DIGITE O ANO: '))
	os.system("cls")
	bix(anoo)

os.system("pause")