import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#determina o dataframe base para a análise
df = pd.read_csv('dataset.csv')

#remove duplicatas de músicas, mantendo a primeira ocorrência
df = df.drop_duplicates(subset=['track_id'], keep='first')

#filtra apenas músicas dos gêneros MPB e Samba (artistas clássicos são categorizados em ambos os gêneros a depender da versão do álbum)
df_mpb_samba = df['track_genre'].str.contains('mpb') | df['track_genre'].str.contains('samba')

#filtra apenas artistas solo (sem colaborações)
df_mpb_samba_solo = df[df_mpb_samba & ~ df['artists'].str.contains(';')]

#agrupa as músicas por artista e calcula a popularidade média
df_grouped = df_mpb_samba_solo.groupby('artists')['popularity'].mean()

#ordena os artistas pela popularidade média em ordem decrescente
df_sorted = df_grouped.sort_values(ascending=False)

#exibe as estastísticas descritivas da popularidade média dos artistas
print(df_sorted.describe())

# Exibe todas as linhas sem truncamento para análise completa

pd.set_option('display.max_rows', None)

#exibe a popularidade média do artista Belchior e a lista completa de artistas ordenados pela popularidade média
print(df_sorted[df_sorted.index == 'Belchior'])
print(df_sorted)

#plota o gráfico de barras horizontais com os 20 artistas mais populares
first20 = df_sorted.head(20).iloc[::-1]
plt.figure()
plt.barh(first20.index, first20.values, color='skyblue')
plt.xlabel('Popularidade Média')
plt.ylabel('Artistas')
plt.title('Top 20 Artistas de MPB e Samba por Popularidade Média')
plt.show()

#hipótese: para o gráfico de dispersão, vamos analisar a relação de valência e popularidade das músicas de MPB e Samba
plt.figure()
plt.scatter(df_mpb_samba_solo['valence'], df_mpb_samba_solo['popularity'], alpha=0.5, color='green')
plt.xlabel('Valência')
plt.ylabel('Popularidade')
plt.title('Relação entre Valência e Popularidade das Músicas de MPB e Samba')
plt.show()

correlation = df_mpb_samba_solo['valence'].corr(df_mpb_samba_solo['popularity'])
print(f'Correlação entre Valência e Popularidade: {correlation:.2f}')

pd.set_option('display.max_columns', None)
print(df_mpb_samba_solo.corr(numeric_only=True))

plt.figure()
sns.heatmap(df_mpb_samba_solo.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.1f', linewidths=0.5, annot_kws={'size': 10}   )
plt.title('Mapa de Calor da Correlação entre Variáveis Numéricas')
plt.show()


