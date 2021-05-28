#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:17:16 2020

@author: elliotmuller
"""

import numpy as np 
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import validation_curve
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import learning_curve


data=sns.load_dataset('titanic')

copy=data[['survived','pclass','sex','age']]

copy=copy.replace(['male','female'],[0,1])
copy.dropna(inplace=True)

model=KNeighborsClassifier()
y=copy['survived']
x=copy.drop('survived',axis=1)

scores=np.zeros((1,10))
for i in range(1,11):
    model=KNeighborsClassifier(n_neighbors=i)
    model.fit(x,y)
    scores[0,i-1]=model.score(x,y)

print(scores)
np.max(scores)

x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,random_state=5)

    
cross_val_score(KNeighborsClassifier(n_neighbors=2),x_train,y_train,cv=5)

k=np.arange(1,50)
train_score,val_score=validation_curve(KNeighborsClassifier(),x_train,y_train,'n_neighbors',k,cv=5)

val_score=np.mean(val_score,axis=1)
train_score=np.mean(train_score,axis=1)
plt.figure()
plt.plot(val_score)
plt.plot(train_score)
plt.show()

param_grid={'n_neighbors': np.arange(1,20), 'metric':['euclidian','manhattan']}

grid=GridSearchCV(KNeighborsClassifier(),param_grid,cv=5)

grid.fit(x_train,y_train)
model=grid.best_estimator_
model.score(x_test,y_test)

print("Hello World")

print(confusion_matrix(y_test,model.predict(x_test)))

N,train_score,val_score= learning_curve( model, x_train, y_train,train_sizes=
                                        np.linspace(0.1,1,10),cv=5)

val_score=np.mean(val_score,axis=1)
train_score=np.mean(train_score,axis=1)

plt.figure()
plt.plot(N,val_score,label='validation')
plt.plot(N,train_score,label='apprentissage')
plt.legend()






