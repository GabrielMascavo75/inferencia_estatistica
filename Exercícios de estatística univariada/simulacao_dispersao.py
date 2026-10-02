#Como os valores da média e dodesvio padrão foram fornecidos
#para ambos os conjunto, não há necessidade de gerar outros valores.

media_a = 10
desvio_a = 1

media_b = 10
desvio_b = 5

cv_a = (desvio_a / media_a) * 100
cv_b = (desvio_b / media_b) * 100

print(f'O coeficiente padrão do conjunto A: {cv_a}%')
print(f'O coeficiente padrão do conjunto B: {cv_b}%')

'''O conjunto B possui uma dispersão maior que o conjunto A'''
