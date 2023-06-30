#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

x = random.randrange(1, 100)
i=1
while True :
    a = int(input('Entrer un nombre entre 1 et 100 :'))
    if a > 100 :
        print('Veuillez vérifier le nombre saisi, il doit être compris entre 1 et 100')
        i = i + 1
    elif a < x: 
        print('Le nombre que vous venez de saisir est inférieur au nombre correcte. ')
        i = i + 1
    elif a > x :
        print('Le nombre que vous venez de saisir est supérieur au nombre correcte. ')
        i = i + 1
    else:
        print('Bravo, vous avez trouvé le nombre secret qui est ', x, 'après ', i, 'tentatives')
        break


# In[ ]:




