#How do North Pacific humpback whale observations vary by season and sea-surface temperature between 2010 and 2025?

#installation of extensions used
from calendar import month

import pandas as pd

df=pd.read_csv('whale_data_original.csv')
#checking the first 5 rows of the dataframe
print(df.head(5))

#I am now going to clean the data. 
#I obtained this data from the OBIS website. 
#There are 282 columns in this dataset, which I do not need to use them all to investigate my question. 
#I have consulted an AI assistant to help me identify the columns that are relevant to my question and initial exploration. 
#These columns are
#occuranceID, eventDate, date_year, month, decimalLattitude
#decimalLongitude, sst, sss, datasetName, basisofRecord, samplingProtocol, coordinateUncertaintyinMeters

#due to this leavng 272 columns that I do not need to use, I have consulted a variety of blogs to look at the best way of dropping these unwanted columns 
#After reading this blog https://medium.com/@whyamit101/pandas-only-keep-certain-columns-7710d6f71a56 - I have found I can keep selected columns by their names
#I will be calling this as df_selected and will be using the following code to select the columns I need. 
df_selected = df[['occurrenceID', 'eventDate', 'date_year', 'month', 'decimalLatitude', 'decimalLongitude', 'sst', 'sss', 'datasetName', 'basisOfRecord', 'samplingProtocol', 'coordinateUncertaintyInMeters']]
print(df_selected.head(5))

#Now this data has been selected I will begin to clean the data. 
#Initially I will check for duplicate data and remove it. 
#The reason I will do this as I want to ensure that the data I am using is accurate and not skewed by duplicate entries. 
print ("checking for duplicates")
print ("number of duplicates:", df.duplicated().sum())

#this shows that there are no duplicates in the data. 
# I will now check for missing values in the data.
# I will do this as I want to ensure that the data I am using is accurate and not skewed by missing values.
print ("Checking for missing values") 
print ("number of missing values:", df_selected.isnull().sum())

#From this we can see that from the printed output that the missing values in the sampling protocol is the highest and if we were to remove this data it would only leave approximately 4000 rows which doesnt fit the remit of the project. 
#I will now drop the sampling protocol column as it is not relevant to the question I am trying to answer. 

print ("Dropping sampling protocol column")
df_selected = df_selected.drop(columns=['samplingProtocol'])
print ("Selected data after dropping sampling protocol column:")
print (df_selected.head(5))
#Now I will drop the blank months as I will not be able to create the season column without the month data
print ("Dropping month data:")
df_selected = df_selected.dropna(subset=['month'])
print (df_selected.head(5))

#checking that this has worked
print ("number of missing values:", df_selected.isnull().sum())


#I want to create a new column called season which will be based on the month column. 
#month 1 will be January and be categorised as winted and month 12 will be categorised as winter. 
# The Royal meterorigical society catergorises the seasons as follows: 
#Winter: December, January, February
#Spring: March, April, May
#Summer: June, July, August
#Autumn: September, October, November
#https://www.rmets.org/metmatters/difference-between-meteorological-and-astronomical-seasons\

