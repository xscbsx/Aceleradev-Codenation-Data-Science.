#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[50]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[10]:


black_friday.columns


# In[5]:


black_friday.head()


# In[7]:


pivot_data = pd.DataFrame({'colunas': black_friday.columns,
                          'tipos': black_friday.dtypes,
                          'nulls': black_friday.isna().sum(),
                          '% nulls': black_friday.isna().sum() / black_friday.shape[0] })


# In[8]:


pivot_data


# In[12]:


black_friday.Age.unique()


# In[32]:


black_friday.dtypes.unique()


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[11]:


def q1():

    return black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[29]:


def q2():
    womans = black_friday.query("Age == '26-35' & Gender == 'F'")
    return womans['User_ID'].shape[0]


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[78]:


def q3():
    
    return black_friday['User_ID'].nunique()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[101]:


def q4():
 
   return black_friday.dtypes.nunique()


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[88]:


def q5():
    pct_nulls = black_friday.isna().sum() / black_friday.shape[0]
    return float(pct_nulls.max())


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[115]:


def q6():
   
    return int(black_friday.isna().sum().max())


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[44]:


def q7():
    frequency = black_friday[black_friday['Product_Category_3'].notna()]['Product_Category_3'].value_counts()
    return float(frequency.index[0])


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[117]:


def q8():
    purch_normal = black_friday['Purchase']
    purch_normal = (purch_normal - purch_normal.min()) / (purch_normal.max() - purch_normal.min())
    return float(purch_normal.mean())


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[64]:


def q9():
    purch_padr = black_friday['Purchase']
    purch_padr = (purch_padr - purch_padr.mean()) / purch_padr.std()
    
    return purch_padr[purch_padr.between(-1, 1)].shape[0]


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[87]:


def q10():
    category_nulls = black_friday[black_friday['Product_Category_2'].isna()][['Product_Category_2','Product_Category_3']]
    return bool(category_nulls.isnull().values.all())

