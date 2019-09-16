"""
=========================================
EP1 - Sudoku - MAC122
2o Semestre de 2019
@author: Pedro Bloss Braga

Solucionador de Sudoku
=========================================

"""
print(__doc__) #printa o cabecalho
'''
Algoritmo do Sudoku:

- a partir de uma posicao:
	- procure a proxima posicao vazia
		- se nao houver mais casas vazias, chegamos num solucao
		- mostre a solucao e retorne desta chamada
	- preencha com um algarismo dentre os possiveis candidatos
		- se nao houver mais  candidatos, zere essa casa e retorne desta chamada. Assim, 
		novas possibilidades serao testadas nas chamadas anteriores
	- retornar o processo, chamando novamente a funcao Sudoku agora com uma casa a mais ja preenchida.

'''
# Funcao recursiva. recebe matriz, linha e coluna

# Primeira chamada: Sudoku(MatrizSudoku, 0, 0)

''' O programa deve:

1 -Ler o nome do arquivo de texto: <arquivo>.txt.

2 - Ler a matriz Sudoku (9x9). Como a matriz e grande (9x9=81 elementos), em vez de digita-la.
deve ser lida de um arquivo de texto <arquivo>.txt

3 - Fazer as consistencias necessarias na matriz lida:
	- Verificar se cada linha tem 9 elementos, todos int entre 0 e 9
	- verficar se os valores nao zero da matriz nao estao repetidos na linha, coluna e quadrado interno

4 - chamar a funcao Sudoku para efetuar o preenchimento da matriz de acordo com as regras do jogo,
indicando todas as possiveis solucoes

5 - a cada solucao encontrada, verificar se a matriz foi preenchida corretamente. Faca o teste completo na 
matriz final verficando se cada linha, cada coluna e cada quadrado interno estao preenchidos corretamente.

6 - repetir a partir do passo 1 ate que seja digitado "fim".

'''
###########################################################################################################
import time

# Acesso local

def LeiaMatrizLocal(NomeArquivo):
	# retrna a matriz lida se ok ou uma lista vazia senao

	# abrir o arquivo para leitura
	try:
		arq = open(NomeArquivo, "r")
	except:
		return [] # se der erro

	# inicia matriz sudoku a ser lida
	mat = [9 * [0] for k in range(9)]

	# ler cada uma das linhas do arquivo

	try:
		i=0
		for linha in arq:
			v = linha.split()
			# verifica se tem 9 elementos e se sao todos entre 1 e 9			
			
			# transforma de texto para int

			for j in range(len(v)):
				mat[i][j] = int(v[j])
				if int(v[j]) < 0 or int(v[j]) >9: #checa valores invalidos e os expoe se houverem
					print(' ', '\n', 'Elemento inconsistente: ', v[j], '\n', ' ')
					print('Matriz Inconsistente! Valores invalidos.')
					return []
			i = i + 1
		#print(consist(mat))
		
		if consist(mat) == False:
			print('Matriz inconsistente!')
			return []
	except:
		print('Inconsistencia.')
	arq.close()
	return mat

'''
Funcoes do Programa:

- def Sudoku(Mat, lin, col) : principal, preenche MatrizSudokku, verificando se chegou ao final de uma solucao e retrocedendo se necessario
 
- def ImprimaMatriz(mat) : imprime a matriz sudoku

- def ProcuraElementoLinha (mat, lin, col): produra digito d na linha L da matriz (0 <= d <= 8). 
devolve -1 se nao encontrou ou  indice da coluna onde foi encontrado

- def ProcuraElementoColuna(mat, lin, col): procura digito d na coluna C da matriz (0 <= d <= 8).
devolve -1 se nao encontrou ou indice da coluna onde foi encontrado 

- def ProcuraElementoQuadrado (mat, lin, col, ind d): procura digito d no quadrado interno onde esta o elemento mat[lin][col] (1<=d<=9).
devolve dupla (k1,k2) se d esta na posicao mat[k1][k2] ou (-1,1) caso contrario

'''
# Ao inves de usar 1 e -1 nos retornos de defs, preferi utilizar True e False

def consist(mat):
	for j in range(len(mat)):
		for i in range(len(mat[0])):
			print(mat[j][i])
			if int(mat[j][i]) < 0 or int(mat[j][i]) > 9:
				print('Existencia do elemento ', mat[j][i], ' impossibilita consistencia da matriz.')
				return False
			else: return True

path = r'/home/pedro/Downloads/sudoku/'
nome = 'sudoku'
arqt = '.txt'

def ImprimaMatriz(mat):
	for i in range(len(mat)):
		print(mat[i])

############################################################


def procura_vazio(mat, verbose=False):
	""" Ao inves de utilizar 3 defs para procurar vazios, utilizo somente esta
	e aplico as linhas, colunas e quadrados"""

	for i in range(len(mat)):
		for j in range(len(mat)):
			if mat[i][j] == 0:
				if verbose == True:
					print('Encontrou casa vazia na posicao (', i, ',', j, ')')
				return(i,j)
				
	return None
#print(procura_vazio(s1, v))

def ProcuraElementoQuadrado(mat, d):
	Q = Quadrados(mat)
	k=0
	for k in range(9):
		for i in range(k,(len(mat)//3)+k):
			for j in range(k,(len(mat[0])//3)+k):
				if mat[i][j] == d:
					return (i,j)
		k+=3
	return None

def ProcuraElementoQuadrado(mat, d):
	Q = Quadrados(mat)
	k=0
	for k in range(9):
		for i in range(k,(len(mat)//3)+k):
			for j in range(k,(len(mat[0])//3)+k):
				if mat[i][j] == d:
					return (i,j)
		k+=3
	return None

def TestaMatrizPreenchida(mat):
	Q = Quadrados(mat)
	for k in range(0,10):	# checa se 0 ou os numeros de 1 a 9 aparecem mais de uma vez
		for i in range(len(mat)):

			#checa se aparece mais de uma vez nas linhas
			if mat[i].count(k) > 1:
				print(k, ' aparece mais de uma vez.')
				return -1
			else:
				return 1
		#checa colunas
		c=[]
		for j in range(len(mat[0])):
			c.append(mat[k[j]])
		if c.count(i) >1:
			print(k, ' aparece mais de uma vez.')
			return -1
		else:
			return 1
		#checa quadrados
		for i in range(len(Q)):
			if Q[i].count(k) >1:
				print(k, ' aparece mais de uma vez.')
				return -1
			else:
				return 1
####################################################################
def Quadrados(mat):
	# Q e a lista de quadrados

	###########################################
	# 3 primeiros quadrados do topo
	Q=[]
	k=0
	for z in range(3):
		q=[]
		for i in range(3):
			q.append([])
			for j in range(3):
				q[i].append(mat[i][k+j])

				#print(' ', '\n', 'z: ',z,  ' i: ', i ,' j: ', j, ' k+j: ', k+j) # contador de indices das matrizes quadradas
		Q.append(q)

		k+=3
		#print('quadrado: ', '\n', q)
	####################################################
	# Os 3 quadrados da segunda fileira: 

	k=0
	for z in range(3):
		q=[]
		for i in range(3):
			q.append([])
			for j in range(3):
				q[i].append(mat[i+3][k+j])
		Q.append(q)
		k+=3
	####################################################
	# Os 3 quadrados da ultima fileira:
	k=0
	for z in range(3):
		q=[]
		for i in range(3):
			q.append([])
			for j in range(3):
				q[i].append(mat[i+6][k+j])
		Q.append(q)

		k+=3
	###########################################3
	# Esta lista receberah listas que contem todos os numeros contidos num quadrado
	# isto e, sera uma matriz, lista de 9 elementos, e cada elemento e a lista dos numeros em um quadrado

	Quadrados=[]

	for x in range(len(Q)):
		Quadrados.append([])
		for k in range(len(Q[x])):
			for z in range(len(Q[x][k])):
				Quadrados[x].append(Q[x][k][z])
	#print('Quadrado 1: ', Quadrados[0])
#############################################################################
# def que define a regra, checa se o elemento já nao esta na linha, coluna e quadrado, para que se possa inserir um candidato


def regra(mat, n, pos):

	#regra da linha
	for i in range(len(mat[0])):
		if mat[pos[0]][i] == n and pos[1] != i:
			return False #-1

	# regra da coluna
	for i in range(len(mat)):
		if mat[i][pos[1]] == n and pos[0] != i:
			return False

	#regra quadrado
	quad_x = pos[1]//3
	quad_y = pos[0]//3

	# para atingir os quadrados, anda de casas de 3 em 3 vezes
	for i in range(quad_y * 3, quad_y *3 + 3):
		for j in range(quad_x * 3, quad_x *3 + 3):
			if mat[i][j] == n and (i,j) != pos:
				return False # -1

	return True # 1


def Sudoku(mat, verbose=False):
	""" Funcao recursiva, solucionadora da MatrizSudoku """

	#ImprimaMatriz(mat)
	#print(' ' + '\n' + 20*'_')
	procura = procura_vazio(mat, v)

	if not procura:
		if verbose == True:
			print('Solucao!')
		return True # encontrou solucao!
	else:
		lin, col = procura

	# tentativa de colocar os candidatos na solucao, por meio de loop
	for i in range(1, 10):
		if regra(mat, i, (lin, col)): # se for valido, colocara o valor na posicao
			
			# se de fato o candidato for valido, eh adicionado 
			mat[lin][col] = i

			# passo recursivo
			#recursivamente tenta-se encontrar solucao
			if Sudoku(mat, v):
				return True #1

			mat[lin][col] = 0 # backtracking!
			
			''' se nao foi possivel achar solucao, troca candidato por zero e retorna, 
			quantas vezes forem necessarias, ate encontrar candidatos validos para uma solucao.'''
	
	# se nao encontrar nenhuma solucao, retorna falso, e fara o backtracking
	return False


def main(verbose=False):

	# usuario escolhe a matriz, dizendo somente o nome, por ex sudoku1.txt
	mat = user_mat()

	m =[] # matriz copia para testar outra solucao
	for i in range(len(mat)):
		m.append([])
		for j in range(len(mat[0])):
			m[i].append(mat[i][j])

	if consist(mat) == True: # procede se for consistente

		tempo1 = time.clock() # tempo de inicio

		print(' '+ '\n')
		print(' * * * Matriz Inicial * * * ')
		print('\n' + ' ')
		ImprimaMatriz(mat) # matriz antes da solucao

		Sudoku(mat, v) # solucionador acionado

		print(' ' + '\n'+
			'Solucionando...'+
			'\n'+ ' ')
		
		#print(procura_vazio(mat))
		if procura_vazio(mat, True) != None: # checa se ainda contem zeros, apos aplicacao do solucionador
			procura_vazio(mat, True)
			#Se ainda tiver vazio, significa que nao encontrou solucao!

			print(' '+ '\n')
			print(' * * * Matriz Incompleta e Consistente * * * ')
			print('\n' + ' ')

			print(' ', '\n', 'Nao encontrou solucao!')
		else:
			# encontrou solucao e matriz eh consistente!
			
			print(' '+ '\n')
			print(' * * * Matriz Completa * * * ')
			print('\n' + ' ')
			ImprimaMatriz(mat)
			tempo2 = time.clock() # tempo de fim

			TestaMatrizPreenchida(mat) # testa se 0 ou os candidatos de 1 a 9 aparecem mais de uma vez
			print(' '+ '\n')
			print(' * * * Matriz Completa e Consistente * * * ')
			print('\n' + ' ')

			#ImprimaMatriz(mat)
			tempo = tempo2 - tempo1 # delta tempo da solucao

			print('Tempo decorrido: ', tempo, ' segundos.')
	else:
		# matriz nao eh consistente! nao eh aplicado o solucionador.
		print(' '+ '\n')
		print(' * * * Matriz inconsistente * * * ')
		print('\n' + ' ')


###########################
# define verbosidade, parametro das funcoes que pode printar e verbalizar o que esta acontecendo
v = False
############################

def Matriz(N):
	""" def para facilitar testes, em que soh se chama o parametro do numero do arquivo,
	para criacao da matriz"""

	mat = LeiaMatrizLocal(path + nome + str(N) + arqt)
	return mat

#alguns testes
#s1 = LeiaMatrizLocal(path + nome + '1' + arqt)

#s2 = Matriz(2)
#s3 = Matriz(3)
#ImprimaMatriz(s1)

#main(s1, v)
#main(s3, v)

##############################################################
def user_mat():

	#usuario diz qual arquivo
	R = str(input('Entre com o nome do arquivo:'))

	mat = LeiaMatrizLocal(path + R)
	
	#ImprimaMatriz(mat)
	# devolve matriz do arquivo escolhido pelo usuario
	return mat
	
def continua():
	#Pergunta para o usuário se deseja continuar, e caso obtenha resposta afirmativa, chama a função Histograma() novamente, caso não quebra.

	while True:
		try:
			#RESPOSTA como input
			print(20*'_'+'\n'+' ')
			R = str(input('Deseja continuar? S/N '))
			print(20*'_'+'\n'+' ')

			#print(R, type(R))
			if R == 'S' or R == 's' or R == 'sim' or R == 'Sim' or R == 'SIM':
				main(v)
			if R =='N' or R == 'n' or R == 'nao' or R == 'NAO' or R == 'Não' or R == 'NÃO':
				print('Fim...')
				break
			while R != 'S' or R != 's' or R != 'sim' or R != 'N' or R != 'n' or R != 'nao' or R != 'Sim' or R != 'Não' or R != 'não':
				#print('','\n',
				#	'(1) Ops! Valor inválido. Insira S ou N.',
				#	'\n','')
				print(20*'_'+'\n'+' ')
				R = str(input('Deseja continuar? S/N '))
				print(20*'_'+'\n'+' ')

				if R == 'S' or R == 's' or R == 'sim' or R == 'Sim' or R == 'SIM':
					main(v)
				if R =='N' or R == 'n' or R == 'nao' or R == 'NAO' or R == 'Não' or R == 'NÃO':
					print('Fim...')
					break
		except ValueError: #valor errado inserido
			print('','\n',
				'(2) Ops! Valor inválido. Insira S ou N.',
				'\n','')
			if R == 'S' or R == 's' or R == 'sim' or R == 'Sim' or R == 'SIM':
				main(v)
			if R =='N' or R == 'n' or R == 'nao' or R == 'NAO' or R == 'Não' or R == 'NÃO':
				print('Fim...')
				break
		else: break

########################################################################################
########################################################################################
# aplicacao do codigo!

main(v)
continua()

#########################################################################################
#########################################################################################
