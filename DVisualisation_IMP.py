import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataframe = pd.read_csv('scottish_hills.csv')   #reading from .csv file
#dataframe1 = pd.read_excel('NOEXCEL.xlsx')      #reading from .xlsx file
#dataframe2 = pd.read_json('jsonFile1.json')     #reading from .json file
#print(dataframe)+
#print(dataframe1)
#print(dataframe2)

#print(dataframe.head())     #prints only 5 records from top/head, by default 5 if nothing given
#print(dataframe.tail(2))     #prints only 2 records from bottom/tail of the table

#print(dataframe['Hill Name'])
#print(dataframe['Height'])

#print(dataframe.iloc[5])        #5th record ko as a whole data display garcha

#print(dataframe.iloc[0,3])      #first record ko 3rd column ko data display garcha
#print(dataframe.loc[:,['Hill Name','Height','Latitude']])   #: denotes all data and [] gives the column name
                                                            #to be displayed
#if iloc used, index must be given, if loc used, column name must be given

#print(dataframe.loc[[1,10], :])     #getting all columns from 1st and 10th records

#print(dataframe.loc[(dataframe['Height']>500) & (dataframe['Hill Name']=='An Socach')])    #directly printed

dd = (dataframe.loc[(dataframe['Height']>500) & (dataframe['Hill Name']=='An Socach')])     #view generated
print(dd.loc[:,['Hill Name', 'Height','Latitude']])                                       #filter applied on view

dds = dd.sort_values(by=['Height'], ascending=True)
print(dds.loc[:,['Hill Name','Height','Latitude']])

#for scatter chart
x = dataframe.Height
y = dataframe.Latitude
plt.scatter(x, y)
plt.show()







