#Aqui vocês irão colocar seu algoritmo de aprendizado
import random
import connection as cn
import numpy as np
import sys

acoesPossiveis = 3
estadosPossiveis = 96
s = cn.connect(2037)
usarArquivo = input('Ler resultado (resultadoTreinamento.txt)? S/N\n')
q_values = []
for estado in range(estadosPossiveis):
    q_values.append([])
    for acao in range(acoesPossiveis):
        q_values[estado].append(float('0'));
if usarArquivo.capitalize() == 'S':
    with open('./resultadoTreinamento.txt') as file:
        q_values = [[float(digit) for digit in line.split()] for line in file]

elif usarArquivo.capitalize() != 'N':
    print('Opção inválida')
    sys.exit(-1)
actions = ['left','right','jump']
epsilon = 0.95  #best action factor
gamma = 0.97 #discount factor for future rewards
alpha = 0.1 #the rate at which the AI agent should learn

#[posição, recompensa]
def getEstadoInicial():
    return [int('0000000',2),-14];
def checkEstadoFinal(recompensa):
    if recompensa == 300:
        return True
    return False

def getAcao(pos_atual, epsilon):
   if random.random() > epsilon:
       return np.random.randint(3)
   else:
        #print('best known action');
        return np.argmax(q_values[pos_atual])
def getQvaluesTable(qValues):
    tempVar = ''
    for line in qValues:
        tempVar += ' '.join([str(value) for value in line]) + '\n'
    return tempVar
for episode in range(3000000000000):
    estadoAtual = getEstadoInicial()
    while not checkEstadoFinal(estadoAtual[1]):
        indiceAcao = getAcao(estadoAtual[0],epsilon)
        estado, recompensa = cn.get_state_reward(s,actions[indiceAcao])
        estadoInt = int(estado,2);
        resultado = q_values[estadoAtual[0]][indiceAcao] + (alpha * (recompensa + (gamma *(max(q_values[estadoInt]))) - q_values[estadoAtual[0]][indiceAcao]))
        q_values[estadoAtual[0]][indiceAcao] = resultado
        estadoAtual = [estadoInt, recompensa]
    valuesTable = getQvaluesTable(q_values)
    print(getQvaluesTable(valuesTable))
    f = open("ultimoResultado.txt", "w")
    f.write(valuesTable)
    f.close()


