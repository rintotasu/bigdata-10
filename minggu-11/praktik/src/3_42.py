#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from IPython.display import display


# In[15]:


movie = pd.read_csv('data/movie.csv')
movie2 = movie[['movie_title', 'imdb_score', 'budget']]
movie_smallest_largest = movie2.nlargest(100, 'imdb_score').nsmallest(5, 'budget')
movie_smallest_largest


# In[ ]:




