# coding: utf-8
import itertools
import sys

def processar(qtd_amarelas, qtd_vermelhas, qtd_azuis, qtd_verdes):
	sys.setrecursionlimit(1000000)

	#referencia as cores com suas respectivas quantidades
	cores = ['Amarelo.png', 'Vermelho.png', 'Azul.png', 'Verde.png']
	quantidade = [qtd_amarelas, qtd_vermelhas, qtd_azuis, qtd_verdes]

	#cria "fisicamente" as bolas de acordo com sua quantidade e cor
	colecao_bolas = []
	for indice_cor in range(0,len(cores)):
		for mais_uma in range(0,int(quantidade[indice_cor])):
			colecao_bolas.append(cores[indice_cor])

	total_bolas = len(colecao_bolas)

	#permutacao das bolas "fisicas" com auxilio da biblioteca ittertools
	tubos = sorted(list(set(itertools.permutations(colecao_bolas))))
	total_tubos = len(tubos)

	return total_bolas, total_tubos, tubos