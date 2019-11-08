# coding: utf-8
estados  = raw_input("Digite os Estados do Autômato:").split(", ")
inicial = raw_input("Estado inicial do Autômato:")
aceita = raw_input("Defina os Estados que serão de aceitação:").split(", ")
print "Informe as funções de transição:"



#Definindo a lista de transições
j = 0
transicoes = []
quant_funcoes = len(estados)*len(estados)
while(j < quant_funcoes):
	x = raw_input().split()
	transicoes += x
	j += 1
#Definindo a lista de transições

#Definindo entrada
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
			if((transicoes[j] == estado_atual) and (entrada[0] == transicoes[j+2])):
				entrada_reserva = []
				for l in entrada:
					entrada_reserva += l
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
if(execucao(estados, estado_atual, aceita, transicoes, entrada)):
	print "Palavra Aceita"
else:
	print"Palavra não aceita"
#Operação de Saída




