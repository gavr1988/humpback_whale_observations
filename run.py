#How do North Pacific humpback whale observations vary by season and sea-surface temperature between 2010 and 2025?

#installation of extensions used
import pandas as pd
import numpy as np


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
df_selected = df[['occurrenceID', 'eventDate', 'date_year', 'month', 'decimalLatitude', 'decimalLongitude', 'sst', 'sss', 'datasetName', 'basisOfRecord', 'coordinateUncertaintyInMeters']]
print(df_selected.head(5))

##I will now check the datatypes of the columns in the dataframe to ensure that they are correct.
print ("Checking data types of columns:")
print (df_selected.dtypes)

#Now I will convert the datatypes


# eventDate contains dates recorded with different levels of detail.
# format="mixed" allows pandas to interpret the different ISO date formats.
# Invalid dates will be converted to NaT, meaning "Not a Time".
df_selected["eventDate"] = pd.to_datetime( df_selected["eventDate"],format="mixed", errors="coerce",utc=True)
#as date is required for the time-based analysis I will now remove any n/a values from the eventDate column.
df_selected = df_selected.dropna(subset=['eventDate'])
print ("Selected data after dropping rows with missing eventDate values:")
print (df_selected.head(5))

# Convert columns that should contain numerical data.
# errors="coerce" changes values that cannot be converted into NaN.
numeric_columns = ["date_year","month","decimalLatitude","decimalLongitude","sst","sss","coordinateUncertaintyInMeters"]

for column in numeric_columns:
    df_selected[column] = pd.to_numeric(df_selected[column],errors="coerce")

# Convert text-based columns to the pandas string data type.
text_columns = ["occurrenceID","datasetName","basisOfRecord"]

for column in text_columns:
    df_selected[column] = df_selected[column].astype("string")


# Check that the data types have been converted
print("\nChecking data types after conversion:")
print(df_selected.dtypes)

# Check whether the conversion created any additional missing values
print("\nMissing values after datatype conversion:")
print(df_selected.isnull().sum())


#Now this data has been selected I will begin to clean the data. 
#Initially I will check for duplicate data and remove it. 
#The reason I will do this as I want to ensure that the data I am using is accurate and not skewed by duplicate entries. 
print ("checking for duplicates")
print ("number of duplicates:", df.duplicated().sum())

#this shows that there are no duplicates in the data. 

# with datasetName i will replace the blanks with unknown
#coordinateUncertaintyInMeters is a numeric column so missing values will remain as NaN.
# rather than being replaced with text such as unknown  as this will prevent any numerical analysis.
df_selected['datasetName'] = df_selected['datasetName'].fillna('unknown')

print ("Selected data after replacing blanks with unknown:")
print (df_selected.head(5))
print ('Checking Missing Values:')
print ("number of missing values:", df_selected.isnull().sum())

# with SST i will keep the rows and exclude them from when i do the analysis on temperature. 
# with SSS i will keep the rows and exclude them from the salinity analysis. 
#I will create new dataframes for the SST and SSS analysis to ensure that I do not lose any data from the original dataframe.


#now i am going to remove 2026 data as my question focuses on the years 2010 to 2025.
df_selected = df_selected[df_selected["date_year"].between (2010,2025)]

#check that it has worked
print ("Earliest Year:", df_selected["date_year"].min())
print ("Latest Year:", df_selected["date_year"].max())


# I will now check whether date_year agrees with the year in eventDate
year_mismatches = df_selected[df_selected["eventDate"].dt.year != df_selected["date_year"]]

print("Year mismatches:", len(year_mismatches))


# I will now check whether month agrees with the month in eventDate
month_mismatches = df_selected[df_selected["eventDate"].dt.month != df_selected["month"]]

print("Month mismatches:", len(month_mismatches))

# 3628 values in the original month column do not agree with eventDate.
# As eventDate contains the complete observation date, I will derive the
# month directly from eventDate to make the date information consistent.
df_selected["month"] = df_selected["eventDate"].dt.month

month_mismatches = df_selected[ df_selected["eventDate"].dt.month != df_selected["month"]]

print("Month mismatches after correction:",len(month_mismatches))
#I want to create a new column called season which will be based on the month column. 
#month 1 will be January and be categorised as winted and month 12 will be categorised as winter. 
# The Royal meterorigical society catergorises the seasons as follows: 
#Winter: December, January, February
#Spring: March, April, May
#Summer: June, July, August
#Autumn: September, October, November
#source:
#https://www.rmets.org/metmatters/difference-between-meteorological-and-astronomical-seasons\

df_selected['season'] = df_selected['month'].apply(lambda x: 'Winter' if x in [12, 1, 2] else ('Spring' if x in [3, 4, 5] else ('Summer' if x in [6, 7, 8] else 'Autumn')))
print ("Selected data after creating season column:")
print (df_selected.head(5))

#the seasons are correct.
#i will now check the unique values in the season column to ensure that they are all valid seasons
print("Season values:", sorted(df_selected["season"].unique()))

#I intend to plot the coordinates on a map to highlight the locations of the observations when doing the dashboard on tableau.
#i must check the coordinates to ensure that they are valid.
#I will check the unique values in the decimalLatitude column to ensure that they are all valid

# Latitude must be between -90 and 90.
# Longitude must be between -180 and 180.
invalid_coordinates = df_selected[ ~df_selected["decimalLatitude"].between(-90, 90) | ~df_selected["decimalLongitude"].between(-180, 180) ]
print("Invalid coordinates:", len(invalid_coordinates))

#i will now check for any missing coordinates in the decimalLatitude and decimalLongitude columns
print(df_selected[["decimalLatitude", "decimalLongitude"]].isnull().sum())

#I will now export the cleaned dataframe to a new csv filed 
df_selected.to_csv('whale_data_cleaned.csv', index=False)

#EXPLORATION OF DATA USING NUMPY#

#I will now begin my NumPy exploration of the data


#I will be using Numpy to explore the data

#I will begin by creating separate dataframes for the SST and SSS analysis to ensure that I do not lose any data from the original dataframe.
df_sst = df_selected.dropna(subset=['sst']).copy()
df_sss = df_selected.dropna(subset=['sss']).copy()

print ("Total cleaned observations:", len(df_selected))
print ("observations with sst data:", len(df_sst))
print ("observations with SSS data:", len(df_sss))


#I will now convert the sst and sss columns to numpy arrays for analysis
sst_array = df_sst['sst'].to_numpy()
sss_array = df_sss['sss'].to_numpy()