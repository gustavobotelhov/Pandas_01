# %% 
import pandas as pd
# %%
idades = [10,18,30,29]
media = sum(idades) / len(idades)

total = 0

for i in idades:
    total += (media - i)**2

variancia = total / (len(idades) - 1)
# %%
# definindo Series
series_idades = pd.Series(idades)
#%%
# Media
series_idades.mean()
# %%
# Mediana
series_idades.median()
# %%
# Descrever
series_idades.describe()
#%%
#Dimensão da série
series_idades.shape
#%% 
# Variancia
series_idades.var()
#%%
# Desvio padrao
series_idades.std()
 # %% 
 # Verificar os index
series_idades.index
# %%
#Alterando index da serie
series_idades.index = ['t','o','a','x']
#%%
#Navegando nos indices novos
series_idades['t']

