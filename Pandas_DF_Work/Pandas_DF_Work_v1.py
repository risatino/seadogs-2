
# coding: utf-8

# In[1]:


#Import dependencies

import json
import numpy as np
import matplotlib.pyplot as plt
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import urllib
import json
from urllib import request
import pandas as pd

#establish API urls for JSON conversion to pandas dataframe

url = 'http://127.0.0.1:5000/population_urban'
url1 = 'http://127.0.0.1:5000/population_suburban'
url2 = 'http://127.0.0.1:5000/population_total'
url3 = 'http://127.0.0.1:5000/employment_urban'
url4 = 'http://127.0.0.1:5000/employment_suburban'
url5 = 'http://127.0.0.1:5000/employment_total'


# In[2]:


#read in JSON Data

#url - population urban
u = urllib.request.urlopen(url)
pop_urb = u.read()

#url - population suburban
a = urllib.request.urlopen(url1)
pop_sub = a.read()

#url - population total
b = urllib.request.urlopen(url2)
pop_tot = b.read()

#url - employment urban
c = urllib.request.urlopen(url3)
emp_urb = c.read()

#url - employment suburban
d = urllib.request.urlopen(url4)
emp_sub = d.read()

#url - employment total
e = urllib.request.urlopen(url5)
emp_tot = e.read()


# In[3]:


#convert JSON to DF

df = pd.DataFrame(eval(pop_urb))
df_PS = pd.DataFrame(eval(pop_sub))
df_PT = pd.DataFrame(eval(pop_tot))
df_EU = pd.DataFrame(eval(emp_urb))
df_ES = pd.DataFrame(eval(emp_sub))
df_ET = pd.DataFrame(eval(emp_tot))


# In[4]:


#setting order of DFs and setting region as index

df = df[["region", "pop_density", "lat", "long", "cbsa_code","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"]]
df.set_index('region', inplace=True)

df_PS = df_PS[["region", "pop_density", "lat", "long", "cbsa_code","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"]]
df_PS.set_index('region', inplace=True)

df_PT = df_PT[["region", "pop_density", "lat", "long", "cbsa_code","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"]]
df_PT.set_index('region', inplace=True)

df_EU = df_EU[["region", "pop_density", "lat", "long", "cbsa_code","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"]]
df_EU.set_index('region', inplace=True)

df_ES = df_ES[["region", "pop_density", "lat", "long", "cbsa_code","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"]]
df_ES.set_index('region', inplace=True)

df_ET = df_ET[["region", "pop_density", "lat", "long", "cbsa_code","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"]]
df_ET.set_index('region', inplace=True)


# In[5]:


#establish list of columns that need to be coverted to numeric so that they can be charted

cols = ["pop_density","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"]
cols1 = ["pop_density","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"]

#replacing commas in population DFs to help with conversion to numeric

df[cols] = df[cols].replace({ ',': ''}, regex=True)
df_PS[cols] = df_PS[cols].replace({ ',': ''}, regex=True)
df_PT[cols] = df_PT[cols].replace({ ',': ''}, regex=True)

#replacing commas in employment DFs to help with conversion to numeric

df_EU[cols1] = df_EU[cols1].replace({ ',': ''}, regex=True)
df_ES[cols1] = df_ES[cols1].replace({ ',': ''}, regex=True)
df_ET[cols1] = df_ET[cols1].replace({ ',': ''}, regex=True)


# In[6]:


#replace '0' string with NaN in population DF

df[cols] = df[cols].replace({'0':np.nan, 0:np.nan})
df_PS[cols] = df_PS[cols].replace({'0':np.nan, 0:np.nan})
df_PT[cols] = df_PT[cols].replace({'0':np.nan, 0:np.nan})

#replace '0' string with NaN in employment DF

df_EU[cols1] = df_EU[cols1].replace({'0':np.nan, 0:np.nan})
df_ES[cols1] = df_ES[cols1].replace({'0':np.nan, 0:np.nan})
df_ET[cols1] = df_ET[cols1].replace({'0':np.nan, 0:np.nan})


# In[7]:



#convert all tables to numeric
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
df_PS[cols] = df_PS[cols].apply(pd.to_numeric, errors='coerce')
df_PT[cols] = df_PT[cols].apply(pd.to_numeric, errors='coerce')

#convert all tables to numeric
df_EU[cols1] = df_EU[cols1].apply(pd.to_numeric, errors='coerce')
df_ES[cols1] = df_ES[cols1].apply(pd.to_numeric, errors='coerce')
df_ET[cols1] = df_ET[cols1].apply(pd.to_numeric, errors='coerce')


# In[9]:


#Concatenate Pop_Urban and Pop_Suburban for visual purposes

combine_population = [df, df_PS]
combine_employment = [df_EU, df_ES]
df_UrbSub_Pop = pd.concat(combine_population)
df_UrbSub_Emp = pd.concat(combine_employment)


# In[14]:


#add column that calculates growth from 1970-2017 for population
df_UrbSub_Pop['Growth'] =  (df_UrbSub_Pop['2017'] - df_UrbSub_Pop['1970']) / (df_UrbSub_Pop['1970'])
df_UrbSub_Emp['Growth'] =  (df_UrbSub_Emp['2017'] - df_UrbSub_Emp['1990']) / (df_UrbSub_Emp['1990'])


# In[16]:


data = [go.Bar(
            x=df_UrbSub_Pop.index,
            y=df_UrbSub_Pop['Growth'],
            name = 'Population Growth 1970-2017'
        
    )]

py.iplot(data, filename='basic-bar')


# In[21]:


trace1 = go.Bar(
    y=df.cbsa_code,
    x=df['2017'],
    name=df.index,
    orientation='h'
)
trace2 = go.Bar(
    y=df_PS.cbsa_code,
    x=df_PS['2017'],
    name=df_PS.index,
    orientation='h',
)

data = [trace1, trace2]

layout = go.Layout(
    barmode='stack',
#     shapes=rectangle
)

fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig)


# In[22]:


#calculate growth seperately in each population DF
df['Growth'] =  (df['2017'] - df['1970']) / (df['1970'])
df_PS['Growth'] =  (df_PS['2017'] - df_PS['1970']) / (df_PS['1970'])


# In[38]:


df['Category'] = 'Urban'
df_PS['Category'] = 'Suburban'
combine_population2 = [df, df_PS]
df_UrbSub_Pop2 = pd.concat(combine_population)
df_UrbSub_Pop2


# In[24]:


trace0 = go.Scatter(
    x=df['Growth'],
    y=df['pop_density'],
    mode='markers',
    marker=dict(
        size=20,
    )
)
trace1 = go.Scatter(
    x=df_PS['Growth'],
    y=df_PS['pop_density'],
    mode='markers',
    marker=dict(
        size=20,
    )
)
data = [trace0, trace1]
py.iplot(data, filename='bubblechart-size')


# In[60]:


import plotly.plotly as py
import plotly.graph_objs as go

trace = go.Heatmap(z=df_UrbSub_Pop2['Growth'],
                   x=df_UrbSub_Pop2['cbsa_code'],
                   y=df_UrbSub_Pop2['Category'],
                   hoverinfo='text',
                                  text = df_UrbSub_Pop2.index)
heat = [trace]
py.iplot(heat, filename='labelled-heatmap')


# In[ ]:


transposed_urbPop = df.transpose()
transposed_urbPop


# In[ ]:


# transposed_urbPop.iloc[5:52].plot(y='NY-NYC Urban')
# plt.show()

