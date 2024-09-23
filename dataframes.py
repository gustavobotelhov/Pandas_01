#%%
import pandas as pd
#%%
# declarando dicionário data.
data = {
    "nome": ["gustavo","botelho","vieira"],
    "sobrenome": ["gus","bot","vi"],
    "idade": [18,28,29]
}
#%%
# buscando a idade da primeira pessoa do dicionario data.
data["idade"][0]

#%%
# Transformar o dicionario em um DataFrame

df = pd.DataFrame(data)
df

#%%
# Agora vamos visualizar uma coluna do df, vai retornar uma série como visto acima.
df['idade']

#%%
# Também podemos ver uma posição
df["idade"][0]
#%%
# ou se quiser garantir e ter o mesmo resultado
df["idade"].iloc[0]
#%%
# Ou todas as posições da coluna
df["idade"][:]


