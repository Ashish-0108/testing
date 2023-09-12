import pandas as pd
df = pd.read_csv('mtsamples.csv')
df['Summary'] = df.apply(lambda x: ' '.join(x.astype(str)), axis=1)
df.drop(df.columns[0:-1], axis=1, inplace=True)

df.to_csv('theory.csv', index=False)
