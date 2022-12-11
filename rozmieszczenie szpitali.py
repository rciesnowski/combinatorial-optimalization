#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import random
from math import sqrt
from mpl_toolkits.mplot3d import Axes3D


# In[2]:


def odl(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)


# In[3]:


def wybierz_szpitale(punkty, n, k):
    # O(n) - wypełniamy listę odleglosciami do najblizszego szpitala
    # początkowo przyjmuje wartość maksymalnej przekątnej w przestrzeni wyznaczonej przez punkty
    # nawet nie znając zakresu punktów, szukanie skrajnych wartosci x, y, z może zająć O(3*n), więc nie przejmujemy się tym
    odl_do_szpitali = [odl([0,0,0], [30,30,30])]*n
    szpitale = []
    
    # na pierwszy szpital wyznaczamy pierwszy lepszy punkt
    maks = 0
    # O(n*k)
    for i in range(k):
        szpitale.append(punkty[maks])
        for j in range(n):
            # jeśli nowy szpital jest blizszy niz poprzedni najblizszy, aktualizujemy
            odl_do_szpitali[j] = min(odl_do_szpitali[j], odl(punkty[maks], punkty[j]))
            # print("maks:", maks, "j:", j, "odl:",odl_do_szpitali[j])
        # np.argmax(list) znajduje argument najwiekszego elementu w liscie O(n)
        # nowy szpital powstanie w punkcie najdalszym od jakiegokolwiek szpitala 
        maks = np.argmax(odl_do_szpitali)

    return max(odl_do_szpitali), szpitale


# In[4]:


def generuj(n, k):
    # dla powtarzalnosci wynikow z tymi samymi n i różnymi k ustawiam ziarno generatora na sztywno
    random.seed(42)
    punkty = np.array([[random.randint(0,30), random.randint(0,30), random.randint(0,30)] for i in range(0, n)])
    maks, szpitale = wybierz_szpitale(punkty, n, k)
    
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, projection='3d')

    for p in punkty:
        ax.scatter(p[0], p[1], p[2], zdir='z', c='b')

    for p in szpitale:
        ax.scatter(p[0], p[1], p[2], zdir='z', c='r')

    plt.show()

    print("Maksymalna odleglosc do szpitala wynosi", maks)


# In[5]:


generuj(10,4)


# In[6]:


generuj(100,4)


# In[7]:


generuj(100,20)


# In[ ]:




