

# 📉 Simulação de Curtose: Mesocúrtica vs Leptocúrtica

Este exercício explora a curtose de uma distribuição, que mede o "grau de achatamento" ou o peso das caudas de uma distribuição de probabilidade.

## 📋 Enunciado
Gere um conjunto de dados que siga uma distribuição normal e outro que tenha muitos *outliers* propositais. Calcule a curtose de ambos e verifique se o resultado condiz com a teoria (Mesocúrtica vs Leptocúrtica).

## 💻 Código (Python)

```python
import numpy as np
from scipy.stats import kurtosis

# 1. Distribuição Normal (Esperado: Curtose próxima de 0 - Mesocúrtica)
dados_normal = np.random.normal(loc=0, scale=1, size=1000)

# 2. Distribuição com outliers propositais (Esperado: Curtose > 0 - Leptocúrtica)
dados_outliers = np.random.normal(loc=0, scale=1, size=1000)

# Adicionando valores extremos (outliers) que puxam as caudas para cima
outliers = np.array([10, 12, 15, -10, -12, -15])

# Concatenando os dados normais com os outliers
dados_outliers = np.concatenate((dados_outliers, outliers))

# Calculando a curtose (Fisher=True, que é o padrão, onde a normal tem curtose 0)
curtose_normal = kurtosis(dados_normal)
curtose_outliers = kurtosis(dados_outliers)

# Resultados
print("Curtose da distribuição normal:", curtose_normal)
print("Curtose da distribuição com outliers:", curtose_outliers)
