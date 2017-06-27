
# coding: utf-8

# In[20]:

import pandas


# In[26]:

data = pandas.read_csv('C:\\Users\\Andrey\\Desktop\\titanic.csv')
print (data)


# In[51]:

guy=0
women=0
for index, row in data.iterrows(): 
    row[4]=str(row[4])
    if row[4]== "male":
        guy=guy+1
    else:
        women=women+1
print(guy,',',women)  #мужчины #женщины


# In[28]:

servived=0
non_servived=0
doly=0
for index, row in data.iterrows(): 
    row[1]=str(row[1])
    if row[1]== "1":
        servived=servived+1
    else:
        non_servived=non_servived+1
sum=servived+non_servived      
percent=round((servived*100)/sum)
print(percent) #выжившие


# In[72]:

class1=0
class2=0
class3=0
class4=0
sum=0
doly=0

for index, row in data.iterrows(): 
    row[2]=str(row[2])
    
    if row[2]== "1":
        class1=class1+1 
    if row[2]== "2":
        class2=class2+1
    if row[2]== "3":
        class3=class3+1
    if row[2]== "4":
        class4=class4+1
    
sum=class1+class2+class3+class4
doly= round(class1*(100/sum),2)
print(doly)  #доля первого класса


# In[189]:

survived=0
notsurvived=0
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D 
import pandas
data = pandas.read_csv('C:\\Users\\Andrey\\Desktop\\titanic.csv')
for index, row in data.iterrows(): 
    
    plt.plot(row[5], row[6], 'ro')
    
    row[1]=str(row[1])
    if row[1]== "1":
        survived=survived+1
    else:
        notsurvived=notsurvived+1
    
plt.grid(True)
plt.xlabel(u'Возраст')
plt.ylabel(u'Шлюпка')
plt.title(u'Рассадка пассажиров по шлюпкам')
plt.show()
sum=survived+notsurvived      
percent1=((survived*100)/sum)
percent2=100-percent1
print("Выжило = ",percent1,"%", "Кол-во", survived)
print("Не выжило = ",percent2,"%", "Кол-во",notsurvived)


# In[22]:

b=data['Age'].mean()  #среднее
m=data['Age'].median()   #медиана
print(round(b,2), m)


# In[188]:

import pandas
import math
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D 

data = pandas.read_csv('C:\\Users\\Andrey\\Desktop\\titanic.csv')
data.corr()


# In[176]:

import pandas
import math
data = pandas.read_csv('C:\\Users\\Andrey\\Desktop\\titanic.csv')
for index, row in data.iterrows(): 
    row[4]=str(row[4])
    if row[4]== "female":    
        row[3] = row[3].split(',')
        b=str(row[3][1:2]).split('.')
        c=str(b[1:2]).replace('\'',' ')  
        print(c)        

