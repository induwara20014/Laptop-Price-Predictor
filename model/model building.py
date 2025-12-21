#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install numpy')
get_ipython().system('pip install pandas')


# In[2]:


import numpy as np
import pandas as pd


# In[3]:


import pandas as pd

url = "https://raw.githubusercontent.com/dineshpiyasamara/LaptopPricePredictor/master/model%20building/laptop_price.csv"
data = pd.read_csv(url, encoding="latin-1")

print(data.head())


# In[4]:


data.shape


# In[5]:


data.isnull()


# In[6]:


data.isnull().sum()


# In[7]:


data.info()


# In[8]:


data['Ram'] = data['Ram'].astype(str).str.replace('GB', '').astype('int32')
data['Weight'] = data['Weight'].str.replace('kg','').astype('float32')


# In[9]:


data.head(2)


# In[10]:


data.corr(numeric_only=True)['Price_euros']


# In[11]:


data['Company'].value_counts()


# In[12]:


def add_company(inpt):
    if inpt == 'Samsung' or inpt == 'Razer' or inpt == 'Mediacom' or  inpt == 'Microsoft' or inpt == 'Vero' or inpt == 'Xiaomi' or inpt == 'Chuwi' or inpt == 'Google'  or inpt == 'Fujitsu' or inpt == 'LG' or inpt == 'Huawei':return 'Other'
    else:
        return inpt
data['Company'] =  data['Company'].apply(add_company)


# In[13]:


data['Company'].value_counts()


# In[14]:


len(data['Product'].value_counts())


# In[15]:


data['TypeName'].value_counts()


# In[16]:


data['ScreenResolution'].value_counts()


# In[17]:


data['Touchscreen'] = data['ScreenResolution'].apply(lambda x:1 if 'Touchscreen' in x else 0)
data['Ips'] = data['ScreenResolution'].apply(lambda x:1 if 'IPS' in x else 0 )


# In[18]:


data.head(2)


# In[19]:


data['Cpu'].value_counts()


# In[20]:


data['cpu_name'] = data['Cpu'].apply(lambda x:" ".join(x.split()[0:3]))


# In[21]:


data['cpu_name'].value_counts()


# In[22]:


def set_processor(name):
    if name == 'Intel Core i7' or name == 'Intel Core i5' or name == 'Intel Core i3':
        return name
    else:
        if name.split()[0] == 'AMD':
            return 'AMD'
        else:
            return 'Other'
data['cpu_name'] = data['cpu_name'].apply(set_processor)


# In[23]:


data['cpu_name'].value_counts()


# In[24]:


data['Gpu'].value_counts()


# In[25]:


data['gpu_name'] = data['Gpu'].apply(lambda x:" ".join(x.split()[0:1]))


# In[26]:


data['gpu_name'].value_counts()


# In[27]:


data.shape


# In[28]:


data = data[data['gpu_name'] != 'ARM']


# In[29]:


data.shape


# In[30]:


data.head(2)


# In[31]:


data['OpSys'].value_counts()


# In[ ]:


def set_os(inpt):
    if inpt == 'Windows 10' or inpt == 'windows 7' or inpt == 'Windows 10 S':
        return 'Windows'
    elif inpt == 'macOS' or inpt == 'Mac OS X':
        return 'Mac'
    elif inpt == 'Linux':
        return 'Linux'
    else:
        return 'Other'


# Notebooks (.ipynb files) cannot be executed directly as Python scripts. Open the file in VS Code's notebook editor or Jupyter, select a Python kernel, and run the cells individually. If you need a script version, convert the notebook to .py using `jupyter nbconvert`.

# In[33]:


data.head(2)


# In[34]:


data = data.drop(columns=['laptop_ID','Inches','Product','ScreenResolution','Cpu','Gpu'])


# In[35]:


data.head()


# In[36]:


data = pd.get_dummies(data)


# In[37]:


data.head(2)


# In[38]:


data.shape


# In[39]:


x = data.drop('Price_euros', axis=1)
y = data['Price_euros']


# In[40]:


get_ipython().system('pip install scikit-learn')


# In[41]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25)


# In[42]:


x_train.shape, x_test.shape


# In[43]:


def model_acc(model):
    model.fit(x_train, y_train)
    acc = model.score(x_test, y_test)
    print(str(model)+'---->'+str(acc))


# In[44]:


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


# In[45]:


from sklearn.model_selection import GridSearchCV

parameters = {'n_estimators':[10,50,100],
              'criterion':['squared_error','absolute_error','poisson']}

grid_obj = GridSearchCV(estimator=rf, param_grid=parameters)

grid_fit = grid_obj.fit(x_train,y_train)

best_model = grid_fit.best_estimator_
best_model


# In[46]:


best_model.score(x_test,y_test)


# In[47]:


import pickle
with open('predictor.pickle','wb') as file:
    pickle.dump(best_model, file)


# In[48]:


x_train.columns


# In[49]:


best_model.predict([[8,1.3,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0]])


# In[ ]:




