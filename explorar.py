import pandas as pd

df = pd.read_csv('dataset.csv')

df = df.drop_duplicates(subset=['track_id'], keep='first')


df_mpb_samba = df['track_genre'].str.contains('mpb') | df['track_genre'].str.contains('samba')
df_mpb_samba_solo = df[df_mpb_samba & ~ df['artists'].str.contains(';')]

df_grouped = df_mpb_samba_solo.groupby('artists')['popularity'].mean()


df_sorted = df_grouped.sort_values(ascending=False)

print(df_sorted.describe())

pd.set_option('display.max_rows', None)

print(df_sorted[df_sorted.index == 'Belchior'])
print(df_sorted)


