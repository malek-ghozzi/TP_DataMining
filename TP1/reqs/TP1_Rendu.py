#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from functools import reduce


# # PART I

# 
# 
# ## 1 Exploration du dataset

# In[2]:


# Exporter BL-Flickr-Images-Book.csv dans un data frame nomé df
df = pd.read_csv('Datasets/BL-Flickr-Images-Book.csv')


# In[3]:


# afficher les 5 premières lignes
df.head()


# In[4]:


df['Shelfmarks']


# ## 2 Jeter un coup d'oeil dans le dataset

# In[5]:


df.info()


# ## 3 Qu'est ce que vous remarquez?

# In[6]:


#on peut supprimé les champs vides , Corporate Author ,Corporate Contributors et  Engraver  sont vides


# ## 4 Dropping unnecessary columns

# In[7]:


to_drop = ['Edition Statement',
           'Corporate Author',
           'Corporate Contributors',
           'Former owner',
           'Engraver',
           'Contributors',
           'Issuance type',
           'Shelfmarks']
df.drop(to_drop, inplace = True, axis = 1)
df.head()


# ## 5 Setting the index of the dataset
# Changer l'index pourqu'ille prenne la valeur de l'identifiant `Identifier`

# In[8]:


###Changerl'index 
df.set_index('Identifier', inplace=True)

###Afficher le résultat
df.head()


# ## 6 Donner un appérçu sur la colonne `Date of Publication` 
# 

# In[9]:


### Afficher  les 25 premières valeurs de Date of Publication
dop=df['Date of Publication']
dop.head(25)


# ## 7 Cleaning columns using the `.apply` function
# 
# ### Ecrire une fonction qui permet de nettoyer la colonne des dates 

# In[10]:


unwanted_characters = ['[', ',', ']','-']
# Completer la fonction suivante
def clean_dates(item):
    dop= str(item.loc['Date of Publication'])
    
    if dop == 'nan' or dop[0] == '[':
        return np.NaN
    
    
    for character in unwanted_characters:
        if character in dop:
            character_index=dop.find(character)
            dop=dop[:character_index]
    return dop

df['Date of Publication'] = df.apply(clean_dates, axis = 1)


# In[11]:


dop.head(25)


# ## 8 Observer la colonne `Author`
# ### Completer la fonction `clean_author_names`qui permet de corriger les valeurs de cet colonne

# In[12]:


author=df['Author']
author.head(25)


# In[ ]:


# compléter la fonction suivante ( à la place de pass)
"""
def clean_author_names(author):
    author = str(author)
    
    if author == 'nan':
        return 'NaN'
    
    author = author.split(',')

    if len(author) == 1:
        name = filter(lambda x: x.isalpha(), author[0])
        return reduce(lambda x, y: x + y, name)
    
    last_name, first_name = author[0], author[1]

    first_name = first_name[:first_name.find('-')] if '-' in first_name else first_name
    
    if first_name.endswith(('.', '.|')):
            parts=first_name.split('.')
        
        if len(parts) > 1:
            first_occurence=first_name.find('.')
            first_occurence=first_name.find('.').
            pass
            pass
        else:
            pass
    
    last_name = last_name.capitalize()
    
    return f'{first_name} {last_name}'


df['Author'] = df['Author'].apply(clean_author_names)
"""


# In[ ]:




