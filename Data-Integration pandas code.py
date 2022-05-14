#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import csv
import os

# Reading csv file using pandas
county_info=pd.read_csv('ACS Census Tract data for 2017.csv',header=0)


# Selecting specific columns
county_info=county_info[['County','State','TotalPop','Poverty','Income']]

county_info= county_info.groupby(['State','County']).sum()


# calculating poverty % and income per capita
county_info['Poverty%'] = (county_info['Poverty']/county_info['TotalPop'])*100
county_info['Incomepercapita'] = (county_info['Income']/county_info['TotalPop'])


county_info['ID_FK'] = range(1, len(county_info.index)+1)

print(county_info.to_string())


-----------------------------------------------X------------------------------------------------


import datetime


# Reading csv file using pandas
covid_monthly=pd.read_csv('COVID_county_data.csv',header=0)

# Selecting specific columns
covid_monthly=covid_monthly[['date','county','state','cases','deaths']]

# Spliting date column into day/month/year 
covid_monthly[["month", "day", "year"]] = covid_monthly["date"].str.split("/", expand = True)

covid_monthly=covid_monthly[['state','county','year','month','cases','deaths']]


covid_monthly= covid_monthly.groupby(['state','county','month','year']).sum()

covid_monthly['ID_FK'] = range(1, len(covid_monthly.index)+1)



covid_monthly

