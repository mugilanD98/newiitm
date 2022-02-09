#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import lxml
import schedule
import time
import mysql.connector
import pymysql
from sqlalchemy import create_engine


# In[14]:


def scrc():
    html_text=requests.get('https://www.renewablesindia.in/').text
    soup= BeautifulSoup(html_text,'lxml')
    location=soup.find('h1',class_='hand').text
    location=location.strip()
    renewable=soup.find_all('div',class_='card-heading-1')
    renew_india=[]
    for i in range(0,3):
      renew_india.append(renewable[i].text)
    renew_india.append(location)
    a=[renew_india]
    renew=pd.DataFrame(a,columns=['co2','solar','wind','location'])
    print(renew)
    


# In[23]:


schedule.every(2).minutes.do(scrc)
while True:
    schedule.run_pending()
    time.sleep(1)


# In[ ]:




