import numpy as np
import pandas as pd

np.random.seed(42)

# 1. 100 números aleatórios entre 1 e 100
df = pd.DataFrame({'valores': np.random.randint(1, 101, size=100)})

# 2. Média e mediana antes
media_antes, mediana_antes = df['valores'].mean(), df['valores'].median()

# 3. Adiciona outlier
df = pd.concat([df, pd.DataFrame({'valores': [5000]})], ignore_index=True)

# 4. Média e mediana depois
media_depois, mediana_depois = df['valores'].mean(), df['valores'].median()

print(f"Média antes:   {media_antes:.2f}  |  depois: {media_depois:.2f}")
print(f"Mediana antes: {mediana_antes:.2f}  |  depois: {mediana_depois:.2f}")

# 5. Conclusão
var_media   = abs(media_depois - media_antes)
var_mediana = abs(mediana_depois - mediana_antes)
if var_media > var_mediana:
    mais_alterada = "MÉDIA"
else:
    mais_alterada = "MEDIANA"
print(f"\nA {mais_alterada} foi mais alterada pelo outlier.")
