# coding: utf-8
import itertools
import sys

def processar(qtd_amarelas, qtd_vermelhas, qtd_azuis, qtd_verdes):
	sys.setrecursionlimit(1000000)

	cores = ['Amarelo.png', 'Vermelho.png', 'Azul.png', 'Verde.png']

	quantidade = [qtd_amarelas, qtd_vermelhas, qtd_azuis, qtd_verdes]

	colecao_bolas = []
	for indice_cor in range(0,len(cores)):
		for mais_uma in range(0,int(quantidade[indice_cor])):
			colecao_bolas.append(cores[indice_cor])

	total_bolas = len(colecao_bolas)

	tubos = []
	for a in itertools.permutations(colecao_bolas):
	    tubos.append(a)

	tubos = tubos[0:len(tubos)/2]

	total_tubos = len(tubos)

	return total_bolas, total_tubos, tubos