# coding: utf-8
#Recebendo autômato
estados  = raw_input("Digite os Estados do Autômato:").split(", ")
inicial = raw_input("Estado inicial do Autômato:")
aceita = raw_input("Defina os Estados que serão de aceitação:").split(", ")
print "Informe as funções de transição:"
#Recebendo autômato


#Definindo a lista de transições
j = 0
transicoes = []
quant_funcoes = len(estados)*len(estados)
while(j < quant_funcoes):
	x = raw_input().split()
	transicoes += x
	j += 1
#Definindo a lista de transições

operacao = ""
while((operacao != "Executar") and (operacao != "Gerar")):
	operacao = raw_input("Deseja executar o autômato ou gerar um novo?(R: Executar ou Gerar) ")

#Definindo entrada
if(operacao == "Executar"):
	entrada = []
	entrada_f = raw_input("Informe a entrada do Autômato:")
	for f in  entrada_f:
		entrada += f
	estado_atual = inicial
#Definindo entrada

#Execução do autômato
def execucao (estados, estado_atual, aceita, transicoes, entrada):
	passou = False
	while (entrada != []):
		caminhos_possiveis = 0
		j = 0
		i = 0 
		while(j < len(transicoes)): 
			if((transicoes[j] == estado_atual) and ( (entrada[0] == transicoes[j+2]) or (transicoes[j+2] == "e") )):
				entrada_reserva = []
				for l in entrada:
					entrada_reserva += l
				if(transicoes[j+2] != "e"):
					del(entrada_reserva[0])
				if(execucao (estados, transicoes[j+1], aceita, transicoes, entrada_reserva)):
					passou = True
			j+= 3
		break
	if(entrada == [] and (estado_atual in aceita)):
		passou = True
	return passou
#Execução do autômato


#Operação de Saída
if(operacao == "Executar"):
	if(execucao(estados, estado_atual, aceita, transicoes, entrada)):
		print "Palavra Aceita"
	else:
		print"Palavra não aceita"
#Operação de Saída

#Operação entre autômatos
elif(operacao == "Gerar"):
	opcao = raw_input("Qual operação deseja fazer?(R: União ou Complemento) ")
	if(opcao == "União"):
		
		#Recebe atributos do segundo autômato
		estados_2  = raw_input("Digite os Estados do segundo Autômato:").split(", ")
		inicial_2 = raw_input("Estado inicial do segundo Autômato:")
		aceita_2 = raw_input("Defina os Estados que serão de aceitação do segundo Autômato:").split(", ")
		print "Informe as funções de transição do segundo Autômato:"
		j = 0
		transicoes_2 = []
		quant_funcoes = len(estados_2)*len(estados_2)
		while(j < quant_funcoes):
			x = raw_input().split()
			transicoes_2 += x
			j += 1
		#Recebe atributos do segundo autômato
		
		#Gera um novo autômato a partir dos que foram passados
		estado_novo = []
		estado_novo += "X"
		for i in estados:
			estado_novo += i
		for j in estados_2:
			if(j not in estado_novo):
				estado_novo += j
		inicial_novo = "X"
		aceita_novo = []
		for i in aceita:
			aceita_novo += i
		for j in aceita_2:
			if(j not in aceita_novo):
				aceita_novo += j
		
		transicoes_novo = []
		for i in transicoes:
			transicoes_novo += i
		for j in transicoes_2:
			transicoes_novo += j
		transicoes_novo += "X", inicial, "e"
		transicoes_novo += "X", inicial_2, "e"
		#Gera um novo autômato a partir dos que foram passados
			
		print inicial_novo
		print estado_novo
		print aceita_novo
		print transicoes_novo
	elif(opcao == "Complemento"):
		
		#Gera um complemento a partir do Autômato passado
		estado_novo = estados
		transicoes_novo = transicoes
		aceita_novo = []
		for i in estados:
			if(i not in aceita):
				aceita_novo += i
		inicial_novo = inicial
		#Gera um complemento a partir do Autômato passado
		
		print inicial_novo
		print estado_novo
		print aceita_novo
		print transicoes_novo
#Operação entre autômatos



