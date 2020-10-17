import numpy as np

#matriz com tamanho e peso 
medidas = np.matrix([[160, 150, 180, 190, 175, 160], [60, 45, 90, 105, 70, 65]]) 

covariancia = np.cov(medidas)

print('covariancia: %s', covariancia)
#covariancia: [[224.16666667 312.5] [312.5 467.5]]