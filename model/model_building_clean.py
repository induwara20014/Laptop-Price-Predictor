import numpy as np
import pandas as pd
import sys

import pandas as pd

url = "https://raw.githubusercontent.com/dineshpiyasamara/LaptopPricePredictor/master/model%20building/laptop_price.csv"
data = pd.read_csv(url, encoding="latin-1")

print(data.head())

data.shape

data.isnull()

data.isnull().sum()

data.info()

data['Ram'] = data['Ram'].astype(str).str.replace('GB', '').astype('int32')
data['Weight'] = data['Weight'].str.replace('kg','').astype('float32')

data.head(2)

data.corr(numeric_only=True)['Price_euros']

data['Company'].value_counts()

def add_company(inpt):
    if inpt == 'Samsung' or inpt == 'Razer' or inpt == 'Mediacom' or  inpt == 'Microsoft' or inpt == 'Vero' or inpt == 'Xiaomi' or inpt == 'Chuwi' or inpt == 'Google'  or inpt == 'Fujitsu' or inpt == 'LG' or inpt == 'Huawei':return 'Other'
    else:
        return inpt
data['Company'] =  data['Company'].apply(add_company)

data['Company'].value_counts()

len(data['Product'].value_counts())

data['TypeName'].value_counts()

data['ScreenResolution'].value_counts()

data['Touchscreen'] = data['ScreenResolution'].apply(lambda x:1 if 'Touchscreen' in x else 0)
data['Ips'] = data['ScreenResolution'].apply(lambda x:1 if 'IPS' in x else 0 )

data.head(2)

data['Cpu'].value_counts()

data['cpu_name'] = data['Cpu'].apply(lambda x:" ".join(x.split()[0:3]))

data['cpu_name'].value_counts()

def set_processor(name):
    if name == 'Intel Core i7' or name == 'Intel Core i5' or name == 'Intel Core i3':
        return name
    else:
        if name.split()[0] == 'AMD':
            return 'AMD'
        else:
            return 'Other'
data['cpu_name'] = data['cpu_name'].apply(set_processor)

data['cpu_name'].value_counts()

data['Gpu'].value_counts()

data['gpu_name'] = data['Gpu'].apply(lambda x:" ".join(x.split()[0:1]))

data['gpu_name'].value_counts()

data.shape

data = data[data['gpu_name'] != 'ARM']

data.shape

data.head(2)

data['OpSys'].value_counts()

def set_os(inpt):
    if inpt == 'Windows 10' or inpt == 'windows 7' or inpt == 'Windows 10 S':
        return 'Windows'
    elif inpt == 'macOS' or inpt == 'Mac OS X':
        return 'Mac'
    elif inpt == 'Linux':
        return 'Linux'
    else:
        return 'Other'

data.head(2)

data = data.drop(columns=['laptop_ID','Inches','Product','ScreenResolution','Cpu','Gpu'])

data.head()

data = pd.get_dummies(data)

data.head(2)

data.shape

print("Columns:", data.columns.tolist())

sys.exit()

x = data.drop('Price_euros', axis=1)
y = data['Price_euros']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25)

x_train.shape, x_test.shape

def model_acc(model):
    model.fit(x_train, y_train)
    acc = model.score(x_test, y_test)
    print(str(model)+'---->'+str(acc))

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
model_acc(lr)

from sklearn.linear_model import Lasso
lasso = Lasso()
model_acc(lasso)

from sklearn.tree import DecisionTreeRegressor
dt = DecisionTreeRegressor()
model_acc(dt)

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()
model_acc(rf)

from sklearn.model_selection import GridSearchCV

parameters = {'n_estimators':[10,50,100],
              'criterion':['squared_error','absolute_error','poisson']}

grid_obj = GridSearchCV(estimator=rf, param_grid=parameters)

grid_fit = grid_obj.fit(x_train,y_train)

best_model = grid_fit.best_estimator_
best_model

best_model.score(x_test,y_test)

import pickle
with open('predictor.pickle','wb') as file:
    pickle.dump(best_model, file)

x_train.columns