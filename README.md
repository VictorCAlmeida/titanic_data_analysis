# 🚢 Análise Exploratória de Dados — Desastre do Titanic

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.5%2B-green)
![Seaborn](https://img.shields.io/badge/Seaborn-0.11%2B-lightblue)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

## 📋 Índice
- [Sobre o Projeto](#-sobre-o-projeto)
- [Objetivos da Análise](#-objetivos-da-análise)
- [Dataset](#-dataset)
- [Principais Insights](#-principais-insights)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Metodologia](#-metodologia)
- [Decisões de Tratamento dos Dados](#-decisões-de-tratamento-dos-dados)
- [Visualizações](#-visualizações)
- [Como Reproduzir o Projeto](#-como-reproduzir-o-projeto)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Limitações e Próximos Passos](#-limitações-e-próximos-passos)
- [Contato](#-contato)

## 📖 Sobre o Projeto
Este projeto realiza uma **Análise Exploratória de Dados (EDA)** no clássico dataset do Titanic, desenvolvida por **Victor Almeida, Analista de Dados**. O objetivo é investigar, de forma descritiva, quais fatores estiveram associados à sobrevivência dos passageiros durante o naufrágio em 1912.

Através de estatísticas descritivas, visualizações e feature engineering, buscamos entender como características como **gênero, idade, classe social, estrutura familiar e localização a bordo** influenciaram as chances de escapar com vida.

## 🎯 Objetivos da Análise
A análise busca responder a perguntas históricas e sociais com base nos dados:
- **Gênero**: O sexo do passageiro foi um fator determinante para a sobrevivência?
- **Classe Social**: A máxima "mulheres e crianças primeiro" foi aplicada igualmente em todas as classes?
- **Idade**: Crianças realmente tiveram prioridade na evacuação?
- **Estrutura Familiar**: Viajar sozinho ou em família impactou as chances de sobreviver?
- **Localização**: O porto de embarque ou o deck da cabine teve alguma relação com a taxa de sobrevivência?

## 📊 Dataset
O dataset utilizado é o **Titanic Dataset**, disponível no [Kaggle](https://www.kaggle.com/c/titanic). Ele contém informações de **891 passageiros**.

| Variável | Descrição |
| :--- | :--- |
| `Survived` | **Variável alvo**: Sobreviveu? (0 = Não, 1 = Sim) |
| `Pclass` | Classe social (1ª, 2ª ou 3ª) - proxy para status socioeconômico |
| `Sex` | Sexo do passageiro |
| `Age` | Idade em anos |
| `SibSp` | Nº de irmãos (siblings) ou cônjuges (spouse) a bordo |
| `Parch` | Nº de pais (parents) ou filhos (children) a bordo |
| `Fare` | Tarifa paga pela passagem |
| `Embarked` | Porto de embarque (C = Cherbourg; Q = Queenstown; S = Southampton) |
| `Cabin` | Número da cabine |

## 💡 Principais Insights
Minha análise revelou padrões marcantes, quantificando a tragédia com dados reais:

### 📊 Estatísticas Gerais
- **Taxa geral de sobrevivência**: **38,4%** dos passageiros sobreviveram
- **Total de sobreviventes**: 342 passageiros
- **Total de não sobreviventes**: 549 passageiros

### 🚺 **Gênero: O Fator Mais Decisivo**
- **Mulheres**: **74,2%** de sobrevivência
- **Homens**: **18,9%** de sobrevivência
- *As mulheres tiveram quase 4x mais chances de sobreviver que os homens*

### 👑 **Classe Social: A Posição Social Importou**
- **1ª Classe**: **63,0%** de sobrevivência
- **2ª Classe**: **47,3%** de sobrevivência
- **3ª Classe**: **24,2%** de sobrevivência
- *Um passageiro da 1ª classe tinha mais que o dobro de chances de sobreviver que um da 3ª classe*

### 🤝 **Interação entre Gênero e Classe**
O cruzamento dessas variáveis revela disparidades ainda mais extremas:

| Classe | Homens | Mulheres |
| :--- | :--- | :--- |
| **1ª Classe** | 36,9% | **96,8%** |
| **2ª Classe** | 15,7% | **92,1%** |
| **3ª Classe** | 13,5% | **50,0%** |

*Destaque: **96,8% das mulheres da 1ª classe sobreviveram**, enquanto **apenas 13,5% dos homens da 3ª classe tiveram a mesma sorte**.*

### 👶 **Idade: Crianças Tiveram Prioridade**
- **Crianças (≤ 12 anos)**: **53,0%** de sobrevivência
- **Adultos**: **36,7%** de sobrevivência
- *Crianças tiveram taxa de sobrevivência significativamente superior à média*

Por faixa etária detalhada:
- **Crianças (0-12 anos)**: 53,0%
- **Adolescentes (13-18 anos)**: 41,6%
- **Adultos (19-60 anos)**: 36,9%
- **Idosos (61+ anos)**: 22,2%

### 👨‍👩‍👧 **Estrutura Familiar**
- **Sozinhos**: **30,3%** de sobrevivência
- **Acompanhados**: **50,5%** de sobrevivência

Por categoria de família:
- **Sozinho**: 30,3%
- **Família Pequena (2-3 pessoas)**: 57,5%
- **Família Média (4-5 pessoas)**: 39,1%
- **Família Grande (6+ pessoas)**: 25,0%

*Famílias pequenas tiveram o melhor desempenho, enquanto grupos muito grandes enfrentaram dificuldades na evacuação*

### 🚢 **Porto de Embarque**
- **Cherbourg (C)**: 55,4% de sobrevivência
- **Queenstown (Q)**: 38,9% de sobrevivência
- **Southampton (S)**: 33,7% de sobrevivência

*Esta diferença está relacionada ao perfil dos passageiros: Cherbourg embarcou mais passageiros de 1ª classe*

### 🛏️ **Deck da Cabine**
Passageiros com cabine registrada tiveram taxas de sobrevivência variando por deck:
- **Deck B**: 71,4%
- **Deck D**: 68,8%
- **Deck E**: 63,0%
- **Deck C**: 59,3%
- **Deck F**: 57,1%
- **Deck A**: 46,2%
- **Deck G**: 33,3%
- **Deck T**: 0%
- **Sem registro (U)**: 29,8%

*Decks superiores (A, B, C) não necessariamente tiveram as maiores taxas - o que importava era a proximidade dos botes salva-vidas*

### 💰 **Tarifa**
A tarifa média paga por classe confirma a segmentação socioeconômica:
- **1ª Classe**: £84,15
- **2ª Classe**: £20,66
- **3ª Classe**: £13,68

Por faixa de tarifa:
- **Baixa**: 25,0%
- **Média**: 36,2%
- **Alta**: 42,6%
- **Muito Alta**: 58,1%

*Quanto mais alta a tarifa paga, maior a chance de sobrevivência*

## 🛠️ Tecnologias Utilizadas
- **[Python](https://www.python.org/)** (3.8+): Linguagem base para a análise
- **[Pandas](https://pandas.pydata.org/)** : Manipulação, limpeza e feature engineering
- **[NumPy](https://numpy.org/)** : Operações matemáticas (log da tarifa)
- **[Matplotlib](https://matplotlib.org/)** : Criação de gráficos estáticos
- **[Seaborn](https://seaborn.pydata.org/)** : Visualizações estatísticas avançadas

## 📐 Metodologia

### 1. Exploração Inicial
Os métodos `head()`, `info()` e `describe()` do Pandas foram utilizados para entender a estrutura, os tipos de dados e a presença de valores nulos. As colunas `Age`, `Cabin` e `Embarked` apresentaram dados faltantes.

### 2. Limpeza e Preparação dos Dados
Para garantir a qualidade da análise, realizei as seguintes transformações:

*   **Tratamento de Nulos**:
    *   `Age`: Valores nulos preenchidos com a **mediana** (28 anos), escolha robusta que minimiza impacto de outliers
    *   `Embarked`: As duas linhas com valor nulo foram removidas (parcela insignificante do total)
    *   `Cabin`: Devido à alta taxa de missing, criei uma nova feature `HasCabin` e extraí o `Deck` quando disponível

*   **Feature Engineering (Criação de Novas Variáveis)**:
    ```python
    # Indica se a cabine foi registrada (1) ou não (0)
    df['HasCabin'] = df['Cabin'].notna().astype(int)
    
    # Tamanho da família (incluindo o próprio passageiro)
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    
    # Indica se o passageiro viajava sozinho
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
    
    # Deck da cabine (primeira letra)
    df['Deck'] = df['Cabin'].str[0]
    df['Deck'] = df['Deck'].fillna('U')  # U = Unknown
    
    # Classificação por faixa etária
    df['AgeGroup'] = pd.cut(df['Age'], bins=[0,12,18,60,100], 
                            labels=['Child','Teen','Adult','Senior'])
    
    # Categorias de família
    df['FamilyCategory'] = pd.cut(df['FamilySize'], bins=[0,1,3,5,11],
                                  labels=['Sozinho','Pequena','Média','Grande'])
    
    # Faixas de tarifa (quartis)
    df['FareGroup'] = pd.qcut(df['Fare'], 4, 
                              labels=['Baixa','Média','Alta','Muito Alta'])
    
    # Log da tarifa para melhor visualização
    df['FareLog'] = np.log1p(df['Fare'])
    ```

### 3. Análises e Visualizações
Com os dados limpos e enriquecidos, utilizei `groupby`, tabelas de contingência e matriz de correlação para explorar as relações entre as variáveis e a sobrevivência. Os resultados foram consolidados em gráficos para uma comunicação clara. **Todos os gráficos são salvos automaticamente na pasta `images/` com alta resolução (300 dpi).**

### 4. Matriz de Correlação
Analisei a correlação entre as principais variáveis numéricas:
- `Survived` x `Pclass`: **-0,34** (correlação negativa - classe mais alta = mais sobrevivência)
- `Survived` x `Fare`: **+0,26** (tarifa mais alta = mais sobrevivência)
- `Survived` x `HasCabin`: **+0,32** (ter cabine registrada = mais sobrevivência)
- `Pclass` x `Fare`: **-0,55** (forte correlação negativa - esperado)

## 🧹 Decisões de Tratamento dos Dados

Durante a preparação dos dados para análise, as seguintes decisões foram tomadas:

### Valores Nulos
- **Idade (Age)** : 177 valores ausentes (19,9% do total) foram preenchidos com a **mediana (28 anos)** para evitar distorções por outliers, garantindo robustez na análise
- **Porto de Embarque (Embarked)** : Apenas 2 valores ausentes (0,2%) - optou-se por **remover essas linhas** por representarem parcela insignificante do dataset
- **Cabine (Cabin)** : 687 valores ausentes (77%) - devido à alta taxa de missing, não foi possível preencher. Estratégia adotada:
  - Criada feature `HasCabin` (1 = tinha cabine registrada, 0 = não tinha)
  - Extraída primeira letra da cabine quando disponível para análise do `Deck`
  - Valores sem registro classificados como 'U' (Unknown)

### Criação de Novas Variáveis (Feature Engineering)
- **`FamilySize`** : Soma de `SibSp` + `Parch` + 1 (incluindo o próprio passageiro) - permite analisar o impacto do tamanho familiar na sobrevivência
- **`IsAlone`** : Indicador binário se o passageiro viajava sozinho (1) ou acompanhado (0) - criado a partir de `FamilySize`
- **`Deck`** : Primeira letra da cabine (ou 'U' para Unknown) - possibilita análise por deck mesmo com muitos dados faltantes
- **`AgeGroup`** : Classificação etária (Child, Teen, Adult, Senior) - facilita a comparação entre faixas etárias
- **`FamilyCategory`** : Categorização do tamanho familiar (Sozinho, Pequena, Média, Grande) - agrupa famílias por porte
- **`FareGroup`** : Faixas de tarifa baseadas em quartis (Baixa, Média, Alta, Muito Alta) - permite analisar o poder aquisitivo de forma categorizada
- **`FareLog`** : Transformação logarítmica da tarifa - normaliza a distribuição assimétrica para melhor visualização

### Ajustes de Tipagem
- `Survived`: Convertido para categoria nas visualizações
- `Pclass`: Tratado como variável categórica ordinal
- `Sex`: Convertido para categoria
- Novas features categóricas (`AgeGroup`, `FamilyCategory`, `FareGroup`) devidamente tipadas como category

Essas decisões foram tomadas para maximizar a qualidade da análise exploratória, preservando ao máximo a integridade dos dados originais e permitindo extrair o maior número possível de insights relevantes.

## 📈 Visualizações
Abaixo estão as principais visualizações geradas na análise, todas com a paleta de cores em **verde escuro** para consistência visual:

### 1. Distribuição de Idade
![Age Distribution](images/Age%20Distribution.png)
*Histograma da distribuição etária dos passageiros*

### 2. Distribuição de Idade por Classe
![Age by Class](images/Age%20by%20Class.png)
*Distribuição de idade em cada classe social*

### 3. Distribuição por Idade e Sobrevivência
![Age Boxplot](images/Age%20Boxplot.png)
*Distribuição de idade entre sobreviventes e não sobreviventes*

### 4. Distribuição de Classes por Porto
![Class by Embarked](images/Class%20by%20Embarked.png)
*Composição de classes sociais em cada porto de embarque*

### 5. Matriz de Correlação
![Correlation Heatmap](images/Correlation%20Heatmap.png)
*Heatmap mostrando as correlações entre as principais variáveis numéricas*

### 6. Distribuição de Tarifa
![Fare Distribution](images/Fare%20Distribution.png)
*Histograma da tarifa paga (distribuição original)*

### 7. Distribuição Log da Tarifa
![Fare Log Distribution](images/Fare%20Log%20Distribution.png)
*Distribuição da tarifa em escala logarítmica*

### 8. Heatmap Sexo x Classe
![Sex Class Heatmap](images/Sex%20Class%20Heatmap.png)
*Visualização em calor da interação entre sexo e classe*

### 9. Sobrevivência por Idade
![survival_by_age](images/survival_by_age.png)
*Taxa de sobrevivência ao longo das diferentes idades*

### 10. Sobrevivência por Classe
![survival_by_class](images/survival_by_class.png)
*1ª Classe: 63,0% | 2ª Classe: 47,3% | 3ª Classe: 24,2%*

### 11. Sobrevivência por Porto
![survival_by_embarked](images/survival_by_embarked.png)
*Cherbourg: 55,4% | Queenstown: 38,9% | Southampton: 33,7%*

### 12. Sobrevivência por Categoria de Família
![survival_by_family category](images/survival_by_family%20category.png)
*Sozinho: 30,3% | Pequena: 57,5% | Média: 39,1% | Grande: 25,0%*

### 13. Sobrevivência por Faixa Etária
![survival_by_fare group](images/survival_by_fare%20group.png)
*Crianças: 53,0% | Adolescentes: 41,6% | Adultos: 36,9% | Idosos: 22,2%*

### 14. Sobrevivência por Isolamento
![survival_by_isolate](images/survival_by_isolate.png)
*Acompanhados tiveram vantagem significativa na evacuação*

### 15. Sobrevivência por Classe e Sexo
![survival_by_pclass_sex](images/survival_by_pclass_sex.png)
*O efeito combinado de gênero e classe social na sobrevivência*

### 16. Sobrevivência por Sexo
![survival_by_sex](images/survival_by_sex.png)
*Mulheres: 74,2% | Homens: 18,9%*

### 17. Sobrevivência por Título
![survival_by_title](images/survival_by_title.png)
*Taxas de sobrevivência por título (Mr, Mrs, Miss, etc.)*

## 🔧 Como Reproduzir o Projeto
Siga os passos abaixo para rodar a análise em sua máquina local.

1.  **Clone o repositório**
    ```bash
    git clone https://github.com/VictorCAlmeida/titanic-analysis.git
    cd titanic-analysis
    ```

2.  **Crie e ative um ambiente virtual (recomendado)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências**
    ```bash
    pip install pandas numpy matplotlib seaborn
    ```
   
4.  **Coloque o dataset na pasta correta**
    - Crie uma pasta `data/` na raiz do projeto
    - Adicione o arquivo `titanic_dataset.csv` dentro dela
    - **Nota:** Utilize a base disponível em: https://drive.google.com/file/d/1IHptTxjbUMRG16xpC39fcliba_-Z_J9d/

5.  **Execute o script principal**
    ```bash
    python Titanic.py
    ```
    
    **Nota:** O script criará automaticamente a pasta `images/` (se não existir) e salvará todos os gráficos nela com alta resolução.

## 📁 Estrutura do Projeto
```
titanic-analysis/
│
├── data/                       # Dados utilizados no projeto
│   └── titanic_dataset.csv     # (59 KB)
│
├── images/                      # Imagens e gráficos gerados automaticamente
│   ├── Age by Class.png
│   ├── Age Boxplot.png
│   ├── Age Distribution.png
│   ├── Class by Embarked.png
│   ├── Correlation Heatmap.png
│   ├── Fare Distribution.png
│   ├── Fare Log Distribution.png
│   ├── Sex Class Heatmap.png
│   ├── survival_by_age.png
│   ├── survival_by_class.png
│   ├── survival_by_embarked.png
│   ├── survival_by_family category.png
│   ├── survival_by_fare group.png
│   ├── survival_by_isolate.png
│   ├── survival_by_pclass_sex.png
│   ├── survival_by_sex.png
│   └── survival_by_title.png
│
├── Titanic.py                   # Script principal da análise
└── README.md                     # Documentação principal 
```

## ⚠️ Limitações e Próximos Passos

### Limitações da Análise
- Esta é uma análise **puramente descritiva**. Não foram realizados testes estatísticos para validar a significância das diferenças observadas
- O preenchimento dos valores nulos de `Age` com a mediana (28 anos) pode introduzir algum viés
- A coluna `Cabin` possui muitos dados faltantes (77% missing), limitando a profundidade da análise por deck
- Algumas categorias (como `Deck T` com 0% sobrevivência) têm amostras muito pequenas

### Próximos Passos
- Aplicar **testes estatísticos** (qui-quadrado, teste t) para validar as associações encontradas
- Construir **modelos preditivos de machine learning** (Regressão Logística, Random Forest, XGBoost) para quantificar a importância de cada variável
- Explorar técnicas mais avançadas de imputação para `Age` e `Cabin`
- Criar um dashboard interativo com Plotly Dash ou Streamlit
- Publicar a análise como um notebook Jupyter para maior interatividade

## 📧 Contato

**Victor Almeida**  
Analista de Dados

[![GitHub](https://img.shields.io/badge/GitHub-VictorCAlmeida-black?style=for-the-badge&logo=github)](https://github.com/VictorCAlmeida)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Victor%20Costa%20Almeida-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/victorcostaalmeida/)

---

**Data da Análise:** Março 2026  
**Licença:** MIT
