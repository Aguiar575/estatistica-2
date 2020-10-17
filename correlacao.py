import numpy as np

#matriz com tamanho e peso 
medidas = np.matrix([[160, 150, 180, 190, 175, 160], [60, 45, 90, 105, 70, 65]]) 

correlacao = np.corrcoef(medidas)

print('corelação: %s', correlacao)
#correlação: [[1.0 0.96532532] [0.96532532 1.0]]