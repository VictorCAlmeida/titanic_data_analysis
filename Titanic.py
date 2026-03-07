import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# ======================================
# CONFIGURAÇÕES INICIAIS
# ======================================

# Criar pasta images se não existir
if not os.path.exists('images'):
    os.makedirs('images')

# Configurar estilo dos gráficos
sns.set_style('whitegrid')
cor_verde_escuro = '#006400'  # Código hexadecimal para verde escuro

# ======================================
# IMPORTANDO DATASET
# ======================================

caminho = r'C:\Users\User\Documents\Victor\SCTEC Análise de dados\Desafio\titanic_dataset.csv'
df = pd.read_csv(caminho)

# ======================================
# EXPLORAÇÃO INICIAL
# ======================================

# print(df.head())
# print(df.info())
# print(df.describe())

# ======================================
# LIMPEZA DE DADOS
# ======================================

df['Age'] = df['Age'].fillna(df['Age'].median())

df = df.dropna(subset=['Embarked'])

df['HasCabin'] = df['Cabin'].notna().astype(int)

df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

df['Deck'] = df['Cabin'].str[0]
df['Deck'] = df['Deck'].fillna('U')

# ======================================
# FEATURE ENGINEERING
# ======================================

# Crianças
df['IsChild'] = (df['Age'] <= 12).astype(int)

# Faixa etária
df['AgeGroup'] = pd.cut(
    df['Age'],
    bins=[0, 12, 18, 60, 100],
    labels=['Child', 'Teen', 'Adult', 'Senior']
)

# Categorias de família
df['FamilyCategory'] = pd.cut(
    df['FamilySize'],
    bins=[0, 1, 3, 5, 11],
    labels=['Sozinho', 'Pequena', 'Média', 'Grande']
)

# Faixas de tarifa
df['FareGroup'] = pd.qcut(df['Fare'], 4, labels=['Baixa', 'Média', 'Alta', 'Muito Alta'])

# Log da tarifa para visualização
df['FareLog'] = np.log1p(df['Fare'])

# ======================================
# ESTATÍSTICA DESCRITIVA
# ======================================

print("\nTaxa geral de sobrevivência")
overall_survival = df['Survived'].mean()
print(overall_survival)

print("\nContagem de sobreviventes")
print(df['Survived'].value_counts())

# ======================================
# ANÁLISES
# ======================================

print("\nSobrevivência por Classe")
print(df.groupby('Pclass')['Survived'].mean())

print("\nSobrevivência por Sexo")
print(df.groupby('Sex')['Survived'].mean())

print("\nSobrevivência por Porto")
print(df.groupby('Embarked')['Survived'].mean())

print("\nSobrevivência por Tamanho da Família")
print(df.groupby('FamilySize')['Survived'].mean())

print("\nSobrevivência por Sexo + Classe")
print(df.groupby(['Sex', 'Pclass'])['Survived'].mean())

print("\nTarifa média por classe")
print(df.groupby('Pclass')['Fare'].mean())

print("\nIdade média por classe e sobrevivência")
print(df.groupby(['Pclass', 'Survived'])['Age'].mean())

print("\nNúmero médio de familiares por classe")
print(df.groupby('Pclass')[['SibSp', 'Parch']].mean())

print("\nSobrevivência por Deck")
print(df.groupby('Deck')['Survived'].mean())

print("\nSobrevivência por Classe + Sexo + Porto")
print(df.groupby(['Pclass', 'Sex', 'Embarked'])['Survived'].mean())

print("\nSobrevivência Crianças vs Adultos")
print(df.groupby('IsChild')['Survived'].mean())

print("\nSobrevivência Sozinho vs Acompanhado")
print(df.groupby('IsAlone')['Survived'].mean())

print("\nSobrevivência por Faixa Etária")
print(df.groupby('AgeGroup')['Survived'].mean())

print("\nSobrevivência por Categoria de Família")
print(df.groupby('FamilyCategory')['Survived'].mean())

print("\nSobrevivência por Faixa de Tarifa")
print(df.groupby('FareGroup')['Survived'].mean())

# ======================================
# MATRIZ DE CORRELAÇÃO
# ======================================

print("\nMatriz de Correlação")

colunas_correlacao = [
    'Survived',
    'Pclass',
    'Age',
    'Fare',
    'SibSp',
    'Parch',
    'FamilySize',
    'IsAlone',
    'HasCabin'
]

correlation_matrix = df[colunas_correlacao].corr()

print(correlation_matrix)

# ======================================
# GRÁFICOS COM SALVAMENTO AUTOMÁTICO
# ======================================

# 1. Heatmap de correlação
plt.figure(figsize=(10, 8))
sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap='Greens',  # Mudei para um mapa de cores em tons de verde
    fmt=".2f"
)
plt.title("Matriz de Correlação - Titanic")
plt.savefig('images/correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.show()

# 2. Sobrevivência por sexo
plt.figure()
sns.barplot(data=df, x='Sex', y='Survived', color=cor_verde_escuro)
plt.title("Sobrevivência por Sexo")
plt.savefig('images/survival_by_sex.png', dpi=300, bbox_inches='tight')
plt.show()

# 3. Sobrevivência por classe
plt.figure()
sns.barplot(data=df, x='Pclass', y='Survived', color=cor_verde_escuro)
plt.title("Sobrevivência por Classe")
plt.savefig('images/survival_by_class.png', dpi=300, bbox_inches='tight')
plt.show()

# 4. Classe + sexo
plt.figure()
sns.barplot(data=df, x='Pclass', y='Survived', hue='Sex', 
            palette={'female': cor_verde_escuro, 'male': '#90EE90'})  # Verde claro para contraste
plt.title("Sobrevivência por Classe e Sexo")
plt.savefig('images/sex_class_survival.png', dpi=300, bbox_inches='tight')
plt.show()

# 5. Heatmap Sexo x Classe
plt.figure(figsize=(8, 4))
survival_heatmap = pd.pivot_table(
    df,
    values='Survived',
    index='Sex',
    columns='Pclass'
)
sns.heatmap(survival_heatmap, annot=True, cmap='Greens', fmt=".2f")
plt.title("Heatmap Sobrevivência Sexo x Classe")
plt.savefig('images/sex_class_heatmap.png', dpi=300, bbox_inches='tight')
plt.show()

# 6. Idade por sobrevivência
plt.figure()
sns.boxplot(data=df, x='Survived', y='Age', 
            palette=[cor_verde_escuro, '#90EE90'])
plt.title("Idade vs Sobrevivência")
plt.savefig('images/age_boxplot.png', dpi=300, bbox_inches='tight')
plt.show()

# 7. Distribuição idade
plt.figure()
sns.histplot(df['Age'], bins=30, color=cor_verde_escuro)
plt.title("Distribuição de Idade")
plt.savefig('images/age_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# 8. Distribuição idade por classe
plt.figure()
sns.boxplot(data=df, x='Pclass', y='Age', 
            palette=[cor_verde_escuro, '#90EE90', '#32CD32'])
plt.title("Distribuição de Idade por Classe")
plt.savefig('images/age_by_class.png', dpi=300, bbox_inches='tight')
plt.show()

# 9. Distribuição tarifa
plt.figure()
sns.histplot(df['Fare'], bins=30, color=cor_verde_escuro)
plt.title("Distribuição de Tarifa")
plt.savefig('images/fare_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# 10. Distribuição tarifa log
plt.figure()
sns.histplot(df['FareLog'], bins=30, color=cor_verde_escuro)
plt.title("Distribuição Log da Tarifa")
plt.savefig('images/fare_log_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# 11. Sobrevivência por porto
plt.figure()
sns.barplot(data=df, x='Embarked', y='Survived', color=cor_verde_escuro)
plt.title("Sobrevivência por Porto")
plt.savefig('images/survival_by_embarked.png', dpi=300, bbox_inches='tight')
plt.show()

# 12. Classe por porto
plt.figure()
sns.countplot(data=df, x='Embarked', hue='Pclass',
              palette=[cor_verde_escuro, '#90EE90', '#32CD32'])
plt.title("Distribuição de Classes por Porto")
plt.savefig('images/class_by_embarked.png', dpi=300, bbox_inches='tight')
plt.show()

# 13. Sobrevivência por tarifa
plt.figure()
sns.barplot(data=df, x='FareGroup', y='Survived', color=cor_verde_escuro)
plt.title("Sobrevivência por Faixa de Tarifa")
plt.savefig('images/survival_by_faregroup.png', dpi=300, bbox_inches='tight')
plt.show()

# 14. Sobrevivência por faixa etária
plt.figure()
sns.barplot(data=df, x='AgeGroup', y='Survived', color=cor_verde_escuro)
plt.title("Sobrevivência por Faixa Etária")
plt.savefig('images/survival_by_agegroup.png', dpi=300, bbox_inches='tight')
plt.show()

# 15. Sobrevivência por categoria de família
plt.figure()
sns.barplot(data=df, x='FamilyCategory', y='Survived', color=cor_verde_escuro)
plt.title("Sobrevivência por Categoria de Família")
plt.savefig('images/survival_by_familycategory.png', dpi=300, bbox_inches='tight')
plt.show()

# 16. Sobrevivência sozinho vs acompanhado
plt.figure()
sns.barplot(data=df, x='IsAlone', y='Survived', color=cor_verde_escuro)
plt.title("Sozinho vs Acompanhado")
plt.savefig('images/survival_by_isalone.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n✅ Todos os gráficos foram salvos na pasta 'images/'")