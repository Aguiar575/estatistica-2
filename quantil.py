import numpy as np

amostra = np.array([12, 23, 43, 3, 8, 20, 9])

quantil50 = np.quantile(amostra, 0.5)
quantil25 = np.quantile(amostra, 0.25)


print('quantil de 50%: %s', quantil50)
#quantil de 50%: 12.0

print('quantil de 25%: %s', quantil25)
#quantil de 25%: 8.5