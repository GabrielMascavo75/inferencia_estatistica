import pandas as pd #manipulação de dados tabulares (DataFrames e Series)
import numpy as np #computação numérica (arrays, raiz quadrada, soma acumulada)
from scipy import stats #funções estatísticas (distribuição t, Qui-Quadrado)
from sklearn.preprocessing import StandardScaler # padroniza dados (média 0, desvio 1)
from sklearn.decomposition import PCA #análise de componentes principais PCA
from sklearn.model_selection import train_test_split #divide dados em treino e teste
from sklearn.neighbors import KNeighborsClassifier #classificador KNN
from sklearn.metrics import confusion_matrix, classification_report #confusion_matrix: gera matriz de confusão (VN, FP, FN, VP) e classification_report: gera relatório com precisão, recall e F1-score

#Substituir pelo caminho correto do arquivo csv no drive
caminho_servidores = 'servidores_ti.csv'
df = pd.read_csv(caminho_servidores)
df.head()
print("\n" + "="*60 + "\n")

#PARTE 1 - Manipulação com Pandas, Estimadores e Intervalos de Confiança
print("="*60)
print("PARTE 1 - Manipulação com Pandas, Estimadores e Intervalos de Confiança")
print("="*60 + "\n")

'''Questão 1 Calcule a média amostral ( ar{X}) e a variância amostral (s^2) para as variáveis uso_cpu e
latencia_rede_ms.'''
#Média Amostral
media_uso_cpu = df['uso_cpu'].mean()
media_latencia_rede = df['latencia_rede_ms'].mean()
#Variância Amostral
variancia_uso_cpu = df['uso_cpu'].var()
variancia_latencia_rede = df['latencia_rede_ms'].var()
#Resultado
print(f'Média Amostral Uso CPU: {media_uso_cpu:.2f}')
print(f'Média Amostral Latência Rede: {media_latencia_rede:.2f}')
print(f'Variância Amostral Uso CPU: {variancia_uso_cpu:.2f}')
print(f'Variância Amostral Latência Rede: {variancia_latencia_rede:.2f}\n')

'''Questão 2 Construa formalmente um Intervalo de Confiança de 95% para a média verdadeira do uso_cpu de toda
a população de servidores utilizando a distribuição t de Student (ou Z, justificado pelo tamanho amostral).
Interprete o significado prático do intervalo obtido.'''
#Tamanho da amostra
n = len(df['uso_cpu'])
#Desvio padrão amostral
desvio_cpu = df['uso_cpu'].std(ddof = 1)#ddof é a correção para a amostra
#Graus de liberdade
graus_liberdade = n - 1
#Nível de confiança
confianca = 0.95
#Valor crítico da distribuição t
t_critico = stats.t.ppf((1 + confianca) / 2, graus_liberdade)
#Erro padrão da média
erro_padrao = desvio_cpu / np.sqrt(n)
#Margem de erro
margem_erro = t_critico * erro_padrao
#Intervalo de confiança
limiti_inferior = media_uso_cpu - margem_erro
limiti_superior = media_uso_cpu + margem_erro
#Resultado
print('Intervalo de confiança de 95% para o uso médio da CPU')
print(f'Média amostral: {media_uso_cpu:.2f}%')
print(f'Desvio padrão amostral: {desvio_cpu:.2f}%')
print(f'Graus de liberdade: {graus_liberdade}')
print(f'Valor crítico t: {t_critico:.4f}')
print(f'Margem de erro: {margem_erro:.2f}%')
print(f'Intervalo de Confiança para Uso CPU: {limiti_inferior:.2f}, {limiti_superior:.2f}')
print('')
print('''O intervalo de confiança de 95% indica que o procedimento utilizado
produz intervalos que, em amostragens repetidas, capturam a verdadeira
média populacional em aproximadamente 95% dos casos. Para esta
amostra, estimamos a média populacional de uso de CPU dentro dos limites
obtidos.''')
print("\n" + "="*60 + "\n")

#PARTE 2 - Teste de Hipóteses (Qui-Quadrado de Independência)
print("="*60)
print("PARTE 2 - Teste de Hipóteses (Qui-Quadrado de Independência)")
print("="*60 + "\n")

'''Investigue se há dependência estatística entre o tipo de infraestrutura onde o servidor opera (tipo_rede) e
a propensão a falhas (status_alerta):
Questão 1 Construa uma tabela de contingência cruzando tipo_rede e status_alerta por meio da função
apropriada do pandas.'''
tabela_contigencia = pd.crosstab(df['tipo_rede'], df['status_alerta'])
print(tabela_contigencia)


'''Questão 2 Aplique o teste Qui-Quadrado de Independência considerando um nível de significância de lpha = 0.05.
Formule claramente a hipótese nula (H_0) e a alternativa (H_1), avalie o p-valor obtido e conclua
analiticamente.'''
qui2, p_valor, graus_liberdade, frequencias_esperadas = stats.chi2_contingency(tabela_contigencia)

print(f'\nEstatística Qui-Quadrado: {qui2:.2f}')
print(f'p-valor: {p_valor:.4f}')
print(f'Graus de Liberdade: {graus_liberdade}')
alfa = 0.05
print(f'\nNível de Signficância (alfa): {alfa}')

if p_valor < alfa:
    print('''\nConclusão: Rejeitamos a hipótese nula (H₀). Há evidências de que
    existe dependência estatística entre o tipo de infraestrutura e a propensão
    a falhas.''')
else:
    print('''\nConclusão: Não rejeitamos a hipótese nula (H₀). Não há evidências
    suficientes para afirmar que existe dependência estatística entre o tipo de
    infraestrutura e a propensão a falhas.''')
print("\n" + "="*60 + "\n")

#PARTE 3 - Redução de Dimensionalidade com PCA (Principal Component Analysis)
print("="*60)
print("PARTE 3 - Redução de Dimensionalidade com PCA")
print("="*60 + "\n")
'''Prepare as métricas quantitativas contínuas para alimentar os modelos preditivos:
Questão 1 Selecione as colunas quantitativas: uso_cpu, uso_memoria, latencia_rede_ms e taxa_pacotes_perdidos.'''
#Selecionando as colunas Quantitativas
colunas_quantitativas = ['uso_cpu', 'uso_memoria', 'latencia_rede_ms', 'taxa_pacotes_perdidos']
dados_quantitativos = df[colunas_quantitativas]

#Visualizando as primeiras linhas dos dados selecionados
print("Dados quantitativos selecionados:")
print(dados_quantitativos.head())#Verifica se as 5 colunas realmente foram selecionadas
print("\n")


'''Questão 2 Padronize os dados utilizando escalonamento de média zero e variância unitária.'''
#Instanciando o StandardScaler
scaler = StandardScaler() #Ira aprender os dados para média e o desvio padrão

#Ajuste e transformação dos dados
dados_padronizados = scaler.fit_transform(dados_quantitativos) #fit() ira calcular e armazenar a média e desvio para cada coluna e o transform() usa a fórmula z-score nos valores

#Conversão para o DF
dados_padronizados_df = pd.DataFrame(dados_padronizados, columns = colunas_quantitativas)#Reaproveitamento das colunas da questão

#Verificar as médias após padronização
print("Médias após padronização:")
print(dados_padronizados_df.mean().round(10))#.round(10) arredonda para 10 casas decimais para evitar erros de ponto flutuante e mostrar que os resultados são praticamente zero

#Verificar os desvios padrões após padronização
print("\nDesvios padrão após padronização:")
print(dados_padronizados_df.std().round(10))


'''Questão 3 Aplique o algoritmo PCA para projetar o espaço multidimensional em
exatamente 2 Componentes Principais (PC1 e PC2). Analise a proporção da variância
explicada endividual e acumulada.'''
#Instanciando o PCA com 2 componentes
pca = PCA(n_components = 2)

#Ajustando e transformando os dados padronizados
componentes_principais = pca.fit_transform(dados_padronizados)
#vai centralizar os dados calculando autovalores e autovetores, ordena os
#autovalores por autovetor decrescente, seleciona os 2 autovetores mais importantes
#e projeta cada ponto dos dados originais nas 2 direções encontradas

#Criando DataFrame com as componentes principais
df_pca = pd.DataFrame(data=componentes_principais,columns=['PC1', 'PC2'])
print("Componentes Principais:")
print(df_pca.head(10))#Pedirei para mostrar apenas 10 linhas

#Variância explicada
variancia_explicada = pca.explained_variance_ratio_#variancia_explicada[i] = autovalor[i] / soma(todos os autovalores)
variancia_acumulada = np.cumsum(variancia_explicada)#retorna a soma acumulada dos elementos

print("\nProporção da Variância Explicada:")
print(f"PC1: {variancia_explicada[0]:.4f} ({variancia_explicada[0]*100:.2f}%)")
print(f"PC2: {variancia_explicada[1]:.4f} ({variancia_explicada[1]*100:.2f}%)")
print(f"Variância acumulada (PC1 + PC2): {variancia_acumulada[1]:.4f} ({variancia_acumulada[1]*100:.2f}%)")
#Dependendo do resultado ira definir o sucesso ou fracasso em comprimir 4 dimensões
#em 2 maior que 90%(excelente, mas raro); 70-90%(bom, caso típico); 50-70%(aceitável, depende do domínio)
#ou menor que 50%(ruim, é melhor manter mais componentes)

#Análise dos componentes
print("\nPesos de cada variável nas componentes principais:")
loadings = pd.DataFrame(pca.components_.T,columns=['PC1', 'PC2'],index=colunas_quantitativas)
print(loadings)
#pca.components_.T transpõe a matriz original de autovalores, assim facilitando a leitura
#de cada linha(variável) e cada coluna(componente)
print("\n" + "="*60 + "\n")

#PARTE 4 - Classificação Supervisionada com KNN(K-Nearest Neighbors)
print("="*60)
print("PARTE 4 - Classificação Supervisionada com KNN(K-Nearest Neighbors)")
print("="*60 + "\n")
'''Construa um modelo preditivo baseado nas componentes principais obtidas:
Questão 1 Defina as features preditoras (x) utilizando as componentes principais
do PCA e o vetor alvo (y) com a coluna status_alerta.'''
# Definição das features (x) e target (y)
x = df_pca[['PC1', 'PC2']].values
y = df['status_alerta'].values

print(f"Shape de X: {x.shape}")
print(f"Shape de y: {y.shape}")
print(f"Distribuição de classes em y:")
print(pd.Series(y).value_counts())

'''Questão 2 Divida o conjunto de dados em Treino (70%) e Teste (30%) com
semente aleatória fixa (ex: random_state=42).'''
#Divisão treino/teste (70%/30%)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state = 50) #30% de teste em 50 linhas

print(f"Tamanho do conjunto de treino: {len(x_train)} registros ({len(x_train)/len(x)*100:.0f}%)")
print(f"Tamanho do conjunto de teste: {len(x_test)} registros ({len(x_test)/len(x)*100:.0f}%)")

'''Questão 3 Instancie e treine um classificador KNN configurado com K = 5 vizinhos.'''
#Instanciando o classificador KNN com k = 5
knn = KNeighborsClassifier(n_neighbors = 5)

#Treinando o modelo com os dados de treino
knn.fit(x_train, y_train)

print("Modelo KNN treinado com sucesso!")
print(f"Número de vizinhos (K): {knn.n_neighbors}")#confirma se o parâmetro foi aplicado corretamente
print(f"Número de características: {knn.n_features_in_}")#confirma se o modelo foi treinado com 2 features
print(f"Classes conhecidas: {knn.classes_}")#confirma se o modelo conhece as duas classes(saudável e falha iminente)

'''Questão 4 Avalie o modelo gerando a matriz de confusão e o relatório de
classificação completo (precisão,revocação e F1-score). Escreva uma análise
crítica sobre o impacto operacional dos falsos negativos em um ambiente
corporativo de TI.'''
# Fazendo as previsões no conjunto de teste
y_pred = knn.predict(x_test)

# Matriz de Confusão
print("Matriz de Confusão:")
cm = confusion_matrix(y_test, y_pred)#tabela de confusão que cruza as previsões do modelo com as respostas reais
print(cm)

# Extraindo os valores individuais
vn, fp, fn, vp = cm.ravel()#vn/vp(verdadeiros negativos/positivos); fp/fn(falsos positivos/negativos)
print(f"\nVerdadeiros Negativos (VN): {vn}")
print(f"Falsos Positivos (FP): {fp}")
print(f"Falsos Negativos (FN): {fn}")
print(f"Verdadeiros Positivos (VP): {vp}")

# Relatório de Classificação
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred, target_names=['Saudável (0)', 'Falha Iminente (1)']))

#Análise se encontra após a janela de saída, está em marckdown
