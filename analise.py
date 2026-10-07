import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dataset.csv')

df_mpb = df[df['track_genre'].str.contains('mpb', case=False, na=False)]
df_samba = df[df['track_genre'].str.contains('samba', case=False, na=False)]

mpb_mean = df_mpb[['valence', 'energy', 'danceability', 'acousticness']].mean()
samba_mean = df_samba[['valence', 'energy', 'danceability', 'acousticness']].mean()

print(mpb_mean)
print(samba_mean)

df_mpb_samba = pd.DataFrame({
    'MPB': mpb_mean,
    'Samba': samba_mean
    })

df_mpb_samba.plot(kind='bar', figsize=(10, 6))
plt.title('Comparação de Perfil Musical entre MPB e Samba')
plt.ylabel('Média')
plt.xticks(rotation=0)
plt.show()