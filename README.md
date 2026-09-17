# 📚 Inferência Estatística: Uma Apresentação Geral

Este documento reúne os principais conceitos, técnicas e aplicações práticas estudados ao longo da disciplina de **Inferência Estatística**. Ele está organizado em duas partes: uma **fundamentação teórica** e um **portfólio de aplicações práticas** (onde estão os códigos e exercícios que desenvolvi).

---

## 🧠 Parte I — Fundamentação Teórica

### 1. O que é Inferência Estatística?

A **Inferência Estatística** é o ramo da Estatística que se dedica a tirar conclusões sobre uma **população** (conjunto completo de elementos) a partir de uma **amostra** (subconjunto finito extraído da população). Diferente da Estatística Descritiva (que apenas resume os dados observados), a Inferência busca **generalizar** e **prever** com base em evidências limitadas.

Ela está fundamentada na **Teoria das Probabilidades** e é essencial em áreas como:
- Controle de qualidade industrial;
- Pesquisas de opinião e censos amostrais;
- Ensaios clínicos e epidemiológicos;
- **Machine Learning** e Ciência de Dados;
- Engenharia de Confiabilidade (SRE, DevOps).

### 2. Conceitos Fundamentais

| Conceito | Definição |
| :--- | :--- |
| **População** | Conjunto completo de todos os elementos de interesse. |
| **Amostra** | Subconjunto representativo extraído da população. |
| **Parâmetro** | Medida numérica que descreve a população (ex: média populacional \(\mu\)). Geralmente desconhecido. |
| **Estimador** | Função dos dados amostrais usada para estimar um parâmetro (ex: média amostral \(\bar{X}\)). |
| **Estimativa** | Valor numérico específico obtido ao aplicar o estimador a uma amostra. |
| **Erro Amostral** | Diferença entre a estimativa e o verdadeiro parâmetro. |

### 3. Principais Tópicos da Inferência Estatística

#### 3.1. Estimação Pontual
Consiste em usar um único valor (estimativa) para aproximar o parâmetro populacional.
- **Propriedades desejáveis de um estimador:** não tendenciosidade, consistência, eficiência e suficiência.
- **Exemplos:** média amostral (\(\bar{X}\)) para \(\mu\); variância amostral (\(s^2\)) para \(\sigma^2\).

#### 3.2. Estimação Intervalar (Intervalos de Confiança)
Em vez de um único valor, fornece um **intervalo** que provavelmente contém o parâmetro, com um certo **nível de confiança**.
- **Fórmula geral:** \(\text{Estimativa} \pm \text{Margem de Erro}\).
- **Distribuições usadas:** Normal (Z) quando \(\sigma\) é conhecido ou \(n\) é grande; **t de Student** quando \(\sigma\) é desconhecido e \(n\) é pequeno.
- **Interpretação:** Um IC de 95% significa que, se repetíssemos o experimento muitas vezes, 95% dos intervalos construídos conteriam o verdadeiro parâmetro.

#### 3.3. Testes de Hipóteses
Procedimento para decidir, com base em evidências amostrais, se uma afirmação sobre a população é suportada ou não.
- **Hipótese Nula (\(H_0\)):** afirmação inicial, geralmente de "não efeito" ou "independência".
- **Hipótese Alternativa (\(H_1\)):** negação de \(H_0\), o que se deseja provar.
- **Erros:** Tipo I (rejeitar \(H_0\) verdadeira) e Tipo II (não rejeitar \(H_0\) falsa).
- **p-valor:** probabilidade de observar um resultado tão extremo quanto o obtido, assumindo \(H_0\) verdadeira. Se \(p < \alpha\) (nível de significância), rejeita-se \(H_0\).

**Principais testes:**
- **Teste Z** e **Teste t** para médias;
- **Teste Qui-Quadrado (\(\chi^2\))** para independência e aderência;
- **ANOVA** para comparação de múltiplas médias;
- **Teste F** para variâncias.

#### 3.4. Inferência Não-Paramétrica
Métodos que não assumem uma distribuição específica para os dados.
- **Exemplos:** Teste de Mann-Whitney, Wilcoxon, Kruskal-Wallis.

### 4. Aplicações em Machine Learning

A Inferência Estatística é a base teórica de diversas técnicas de Machine Learning:
- **Validação de modelos:** testes de hipóteses para comparar algoritmos;
- **Seleção de features:** testes de dependência (Qui-Quadrado, ANOVA);
- **Redução de dimensionalidade:** PCA, que usa autovalores e autovetores (álgebra linear + estatística);
- **Intervalos de confiança em previsões:** para quantificar incerteza;
- **A/B Testing:** comparação estatística de duas versões de um produto.

---

## 💻 Parte II — Portfólio de Aplicações Práticas

*(Aqui serão documentados os códigos e exercícios desenvolvidos ao longo da disciplina.)*

### 📌 Estudo de Caso 1 — Análise de Confiabilidade de Servidores em Nuvem

**Contexto:** Aplicação de técnicas de Inferência Estatística e Machine Learning para monitorar servidores em nuvem e prever falhas iminentes.

**Dataset:** `servidores_ti.csv` (500 registros de telemetria operacional).

**Técnicas aplicadas:**
- **Estatística Descritiva:** média e variância amostral.
- **Intervalo de Confiança de 95%** para a média de `uso_cpu` (distribuição t de Student).
- **Teste Qui-Quadrado de Independência** entre `tipo_rede` e `status_alerta`.
- **PCA** para redução de dimensionalidade (4 variáveis → 2 componentes).
- **KNN (K=5)** para classificação de falhas iminentes.

**Aprendizados-chave:**
- Importância da padronização antes do PCA.
- Interpretação da variância explicada e dos *loadings*.
- Impacto operacional de Falsos Negativos em ambientes de SRE.
- Uso de `scipy.stats`, `sklearn.preprocessing`, `sklearn.decomposition` e `sklearn.neighbors`.

*(Código completo disponível no arquivo `servidor_nuvem.py`.)*

---

## 📝 Lista Consolidada de Conhecimentos Adquiridos

*(Atualizada conforme avanço na disciplina.)*

- [x] **Conceitos Fundamentais:** população, amostra, parâmetro, estimador, erro amostral.
- [x] **Estatística Descritiva com Pandas:** média, variância, tabelas de contingência.
- [x] **Estimação Intervalar:** construção de IC de 95% com distribuição t de Student.
- [x] **Testes de Hipóteses:** formulação de \(H_0\) e \(H_1\), interpretação do p-valor, teste Qui-Quadrado de Independência.
- [x] **Pré-processamento:** padronização com `StandardScaler`.
- [x] **Redução de Dimensionalidade:** PCA, variância explicada e *loadings*.
- [x] **Machine Learning:** KNN, divisão treino/teste, matriz de confusão e relatório de classificação.
- [x] **Análise Crítica:** impacto de Falsos Negativos em ambientes corporativos de TI.

---

## 📖 Referências Bibliográficas

- Bussab, W. O., & Morettin, P. A. *Estatística Básica*. Saraiva.
- Montgomery, D. C., & Runger, G. C. *Applied Statistics and Probability for Engineers*. Wiley.
- James, G., et al. *An Introduction to Statistical Learning*. Springer.
- Documentação oficial: [SciPy](https://docs.scipy.org/), [Scikit-learn](https://scikit-learn.org/), [Pandas](https://pandas.pydata.org/).

---
*Última atualização: 17 de Setembro de 2026*
