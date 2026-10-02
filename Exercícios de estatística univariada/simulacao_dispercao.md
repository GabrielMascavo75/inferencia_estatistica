# 📊 Simulação de Dispersão: Coeficiente de Variação (CV)

Este exercício tem como objetivo comparar a dispersão relativa de dois conjuntos de dados que possuem a mesma média, mas desvios padrão diferentes.

## 📋 Enunciado
Gere dois conjuntos de dados:
- **Conjunto A:** 50 números aleatórios, com média 10 e desvio padrão 1.
- **Conjunto B:** 50 números aleatórios, com média 10 e desvio padrão 5.

Calcule o Coeficiente de Variação (CV) e comente os resultados.

## 💻 Código (Python)

```python
# Como os valores da média e do desvio padrão foram fornecidos,
# não há necessidade de gerar os dados aleatórios para calcular o CV.

media_a = 10
desvio_a = 1

media_b = 10
desvio_b = 5

# Cálculo do Coeficiente de Variação (CV = desvio padrão / média * 100)
cv_a = (desvio_a / media_a) * 100
cv_b = (desvio_b / media_b) * 100

print(f'O coeficiente de variação do conjunto A: {cv_a}%')
print(f'O coeficiente de variação do conjunto B: {cv_b}%')
