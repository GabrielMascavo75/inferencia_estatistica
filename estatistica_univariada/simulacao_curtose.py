import numpy as np
from scipy.stats import kurtosis

# Distribuição normal
dados_normal = np.random.normal(loc=0, scale=1, size=1000)

# Distribuição com outliers
dados_outliers = np.random.normal(loc=0, scale=1, size=1000)

outliers = np.array([10, 12, 15, -10, -12, -15])

dados_outliers = np.concatenate((dados_outliers, outliers))

# Calculando a curtose
curtose_normal = kurtosis(dados_normal)
curtose_outliers = kurtosis(dados_outliers)

# Resultados
print("Curtose da distribuição normal:", curtose_normal)
print("Curtose da distribuição com outliers:", curtose_outliers)
