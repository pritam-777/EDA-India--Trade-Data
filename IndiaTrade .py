#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# In[2]:


export_df=pd.read_csv("2018-2010_export.csv")
import_df=pd.read_csv("2018-2010_import.csv")


# In[3]:


export_df.head()


# In[4]:


import_df.head()


# In[5]:


export_df.describe()


# In[6]:


import_df.describe()


# In[7]:


import_df.shape


# In[8]:


export_df.shape


# In[9]:


import_df.info()


# In[10]:


export_df.info()


# In[11]:


export_df['value'].describe() 


# In[12]:


import_df['value'].describe()


# In[13]:


print("total null values in export data:",export_df['value'].isnull().sum())
print("total null values in export data:",import_df['value'].isnull().sum())


# In[14]:


def filling_null(data_df):
    #data_df = data_df[data_df.value!=0]
    data_df["value"].fillna(data_df['value'].mean(),inplace = True)
    import_df.year = pd.Categorical(import_df.year)
    return data_df


# In[15]:


import_df = filling_null(import_df)
export_df = filling_null(export_df)


# In[16]:


print("total null values in export data:",export_df['value'].isnull().sum())
print("total null values in export data:",import_df['value'].isnull().sum())


# In[17]:


print("total number of countries india exporting commodity:",len(export_df['country'].unique()))
print("total number of countries india importing commodity:",len(import_df['country'].unique()))


# ## Import And Export Country Wise

# In[18]:


import_df1= import_df.groupby('country').agg({'value':'sum'}).sort_values(by='value', ascending = False)
export_df1= export_df.groupby('country').agg({'value':'sum'}).sort_values(by='value', ascending = False)


# In[19]:


import_df1=import_df1.head(10)
export_df1=export_df1.head(10)


# ### Top Country's  India's Import

# In[22]:


#import_df1.plot(kind='bar',cmap="Dark2")
plt.figure(figsize=(10,6))
sns.barplot(import_df1.index,import_df1.value)
plt.xticks(rotation=35)
plt.savefig("pic1.png")


# 1. China - very Huge Trade Deficit
# 2. UAE - little Trade Deficit
# 3. SAUDI three Postion

# ### Top Country's  India's Export

# In[23]:


plt.figure(figsize=(10,6))
sns.barplot(export_df1.index,export_df1.value)
plt.xticks(rotation=35)


# USA - little Trade Surplus

# #### China has biggest market in india followed by UAE,Saudi Arabia and USA
# #### USA is our biggest importer followed by UAE and China Republic.

# In[24]:


import_Commodity= import_df.groupby('Commodity').agg({'value':'sum'}).sort_values(by='value', ascending = False)
export_Commodity= export_df.groupby('Commodity').agg({'value':'sum'}).sort_values(by='value', ascending = False)
import_Commodity=import_Commodity.head(10);
export_Commodity=export_Commodity.head(10);


# ### Top 10 importing Commodities

# In[26]:


plt.figure(figsize=(15,15))
sns.barplot(import_Commodity.value,import_Commodity.index,palette = 'Set1')
plt.savefig("pic2.png")


# ## Highest Importing Commodities
#  1. MINERAL FUELS, MINERAL OILS AND PRODUCTS OF THEIR DISTILLATION; BITUMINOUS SUBSTANCES; MINERAL WAXES 
#     
# 2. NATURAL OR CULTURED PEARLS,PRECIOUS OR SEMIPRECIOUS STONES,PRE.METALS,CLAD WITH PRE.METAL AND ARTCLS THEREOF;
#    IMIT.JEWLRY;COIN.
# 3. ELECTRICAL MACHINERY AND EQUIPMENT AND PARTS THEREOF; SOUND RECORDERS AND REPRODUCERS, TELEVISION IMAGE AND SOUND RECORDERS AND REPRODUCERS,
#     AND PARTS
# 
# 4. NUCLEAR REACTORS, BOILERS, MACHINERY AND MECHANICAL APPLIANCES; PARTS THEREOF.
#     
# 

# ## Top 10 Exporting Commodities
# 

# In[27]:


plt.figure(figsize=(15,15))
sns.barplot(export_Commodity.value,export_Commodity.index,palette='tab20')


# ## Highest Exporting  Commodities
# 1. MINERAL FUELS, MINERAL OILS AND PRODUCTS OF THEIR DISTILLATION; BITUMINOUS SUBSTANCES; MINERAL WAXES.
# 2. NATURAL OR CULTURED PEARLS,PRECIOUS OR SEMIPRECIOUS STONES,PRE.METALS,CLAD WITH PRE.METAL AND ARTCLSc    THEREOF;IMIT.JEWLRY;COIN.
# 3. VEHICLES OTHER THAN RAILWAY OR TRAMWAY ROLLING STOCK, AND PARTS AND ACCESSORIES THEREOF.
# 4. NUCLEAR REACTORS, BOILERS, MACHINERY AND MECHANICAL APPLIANCES; PARTS THEREOF.

# In[28]:


import_yearly=import_df.groupby('year').agg({'value':'sum'})
export_yearly=export_df.groupby('year').agg({'value':'sum'})


# ### Yearly Import

# In[30]:


plt.figure(figsize=(10,6))
sns.barplot(import_yearly.index,import_yearly.value,palette='plasma')
plt.savefig("pic3.png")


# ### Yearly Exporting

# In[32]:


plt.figure(figsize=(10,6))
sns.barplot(export_yearly.index,export_yearly.value,palette='cividis')
plt.savefig("pic4.png")


# In[33]:


plt.figure(figsize= (18,10))
sns.lineplot(x='year',y='value', data=import_df, label='Imports')
sns.lineplot(x='year',y='value', data=export_df, label='Exports')
plt.title('Values of Indian imports and exports', fontsize=16)
plt.xlabel('Year')
plt.ylabel('Value in million US$')
plt.show()


# In[34]:


import_df=import_df[import_df.value>1000]
export_df=export_df[export_df.value>1000]


# In[35]:


import_df2 = import_df.groupby(['country']).agg({'value': 'sum'}).sort_values(by='value')
export_df2 = export_df.groupby(['country']).agg({'value': 'sum'}).sort_values(by='value')


# In[36]:


plt.figure(figsize=(12,8))
plt.title('Highest Trade importing countrywise', fontsize = 20)
sns.heatmap(import_df2,cmap='Blues')


# In[39]:


plt.figure(figsize=(12,8))
plt.title('Highest Trade Exporting countrywise', fontsize = 20)
sns.heatmap(export_df2,cmap='YlOrBr')
plt.savefig("pic5.png")


# # Profit and Loss by Yaerly

# In[41]:


df_im = import_df.groupby('year').agg({'value':'sum'})
df_ex=  export_df.groupby('year').agg({'value':'sum'})


# In[43]:


df_im['deficit'] = df_ex-df_im


# In[50]:


plt.figure(figsize=(10,6))
sns.barplot(df_im.index,df_im.deficit, palette='RdYlGn')
sns.barplot(df_im.index,df_im.value,palette='CMRmap')
plt.savefig("pic6.png")


# In[ ]:





# In[ ]:




