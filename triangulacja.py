#!/usr/bin/env python
# coding: utf-8

# In[227]:


wielokat = [(0, 30), (30, 50), (60, 30), (70, 35), (80, 60), (90, 50), (100, 65), (110, 70), (105, 0), (40, 30), (35, 10), (15, 10)]
indeks = 0
maks = wielokat[0][0]
for i in range(1,len(wielokat)):
    if wielokat[i][0] > maks:
        maks = wielokat[i][0]
        indeks = i

wielokat_nieposort = wielokat

wielokat = []
for i in range(0, len(wielokat_nieposort)):
    if i <= indeks:
        wielokat.append(list(wielokat_nieposort[i]) + [1])
    else: wielokat.append(list(wielokat_nieposort[i]) + [-1])
wielokat = sorted(wielokat, key=lambda x: x[0])


# In[199]:


class Stos: 
    def __init__ (self):
        self.Stos = []
 
    def wloz(self, s):
        self.Stos.append(s)   
 
    def zdejmij(self):
        if not Stos.czy_pusty(self):
            self.Stos.pop(-1)
 
    def rozmiar(self):
        return len(self.Stos)
 
    def top(self):
        return self.Stos[-1]
 
    def czy_pusty(self):
        return len(self.Stos) == 0
    
    def zawartość(self):
        return self.Stos


# In[200]:


def szukaj(list, element):
    for i in range(len(list)):
        if list[i] == element:
            return i


# In[226]:


stos = Stos()
stos.wloz(wielokat[0])
stos.wloz(wielokat[1])
przekatne = []
    
def skret_w_prawo(lancuch, p1, p2, p3):
    if lancuch == -1: return (p3[0] - p1[0])*(p2[1] - p1[1]) > (p2[0] - p1[0])*(p3[1] - p1[1])
    if lancuch == 1: return (p1[0] - p3[0])*(p2[1] - p3[1]) > (p2[0] - p3[0])*(p1[1] - p3[1])

for i in range (2, len(wielokat)-1):
    print("wierzcholek: ", tuple(wielokat[i][:-1]))
    print("stos:", stos.zawartość())

    last_top = stos.top()
    # inny lancuch - doczepiamy przekatne do wszystkich ze stosu
    if last_top[2] != wielokat[i][2]:
        print("inny lancuch")
        for j in range (1, stos.rozmiar()):
            przekatne.append([tuple(wielokat[i][:-1]), tuple(stos.top()[:-1])])
            print("dodaję: ", przekatne[-1])
            last_top = stos.top()
            stos.zdejmij()
        stos.zdejmij()
        lancuch = last_top[2]
        stos.wloz(last_top)
        stos.wloz(wielokat[i])
    # ten sam lancuch
    else:
        print("ten sam lancuch")
        last_top = None
        vk = stos.top()
        stos.zdejmij()
        while stos.rozmiar() > 0 and skret_w_prawo(vk[2], tuple(wielokat[i][:-1]), tuple(vk[:-1]), tuple(stos.top()[:-1])):
            print("skret w prawo")
            przekatne.append([tuple(wielokat[i][:-1]), tuple(stos.top()[:-1])])
            print("dodaję: ",przekatne[-1])
            vk = stos.top()
            stos.zdejmij()
        stos.wloz(vk)
        stos.wloz(wielokat[i])
        last_top = vk if last_top is None else last_top
        
vn = wielokat[-1]
for i in range(0, stos.rozmiar()-1):
    if (i != 0):
        przekatne.append([tuple(vn[:-1]), tuple(stos.top()[:-1])])
    stos.zdejmij()
    
print(przekatne)
import matplotlib.pyplot as plt
from shapely.geometry import Polygon

x,y = Polygon(wielokat_nieposort).exterior.xy
plt.plot(x,y)
for i in przekatne:
    plt.plot((i[0][0], i[1][0]), (i[0][1], i[1][1]))
plt.plot()


# if (vi oraz wierzchołek na szczycie stosu są na różnych łańcuchach)
#     4. then Zdejmij wszystkie wierzchołki ze stosu S = (v′1, . . . , v′k). then Zgłoś wszystkie przekątne {vi, v′j}, j = 2, . . . , k. then Włóż v′k i vi na stos.
#     5. else Zdejmij wierzchołek v′k ze stosu S = (v′1, . . . , v′k). else Zdejmuj pozostałe wierzchołki tak długo, aż odpowiednie przekątne
# else {vi, v′j} są wewnątrz wielokąta; zgłaszaj te przekątne.
# else Włóż ostatnio zdjęty wierzchołek na stos.
# else Włóż vi na stos.
# 6. Dodaj przekątne z vn do wszystkich wierzchołków na stosie, oprócz pierwszego i ostatniego

# In[ ]:




