#How do North Pacific humpback whale observations vary by season and sea-surface temperature between 2010 and 2025?

#installation of extensions used
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#loading the data frame
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
#I will also be able to exclude missing measurements without changing the dataframes selected
df_sst = df_selected.dropna(subset=['sst']).copy()
df_sss = df_selected.dropna(subset=['sss']).copy()

print ("Total cleaned observations:", len(df_selected))
print ("observations with sst data:", len(df_sst))
print ("observations with SSS data:", len(df_sss))


#I will now convert the sst and sss columns to numpy arrays for analysis
sst_array = df_sst['sst'].to_numpy()
sss_array = df_sss['sss'].to_numpy()

#Exploration of the sea-surface temperature

print("sea-surface temperature (sst) analysis:")
print ("Mean sst:", np.mean(sst_array))
print ("median sst:", np.median(sst_array))
print ("maximum sst:", np.max(sst_array))
print ("minimum sst:", np.min(sst_array))
print ("Standard deviation of sst:", np.std(sst_array))

#Exploration of Sea Surface Temperature by Season
season_order = ["Winter", "Spring", "Summer", "Autumn"]

for season in season_order:

    season_sst = df_sst.loc[df_sst["season"] == season,"sst"].to_numpy()

    print("\nSeason:", season)
    print("Number of observations:", len(season_sst))
    print("Mean SST:", np.mean(season_sst))
    print("Median SST:", np.median(season_sst))
    print("Minimum SST:", np.min(season_sst))
    print("Maximum SST:", np.max(season_sst))
    print("Standard deviation:", np.std(season_sst))

#calculating the percentiles of the sst data
sst_percentiles = np.percentile(sst_array, [25, 50, 75])

print ("the SST percentiles:")
print ("25th percentils:", sst_percentiles[0])
print ("50th percentils:", sst_percentiles[1])
print ("75th percentils:", sst_percentiles[2])

#I now will investigate if there are any outliers in the sst data using the IQR method.
sst_q1 = np.percentile(sst_array, 25)
sst_q3 = np.percentile(sst_array, 75)

sst_iqr = sst_q3 - sst_q1

sst_lower_bound = sst_q1 - (1.5 * sst_iqr)
sst_upper_bound = sst_q3 + (1.5 * sst_iqr)

print ("SST lower boundary for outliers:", sst_lower_bound)
print ("SST upper boundary for outliers:", sst_upper_bound)

sst_outliers = df_sst[(df_sst['sst'] < sst_lower_bound) | (df_sst['sst'] > sst_upper_bound)]
print ("Number of outliers in SST data:", len(sst_outliers))
print ("Outliers in SST data:")
print(sst_outliers[['eventDate', 'season', 'decimalLatitude', 'decimalLongitude', 'sst']].head(20))

# The SST outlier data frame is empty which means there are no SST values that fall outside the IQR outlier boundaries.
# This does not mean there are no unusual values in the data overall, only that none were flagged by this method.

#Now I will use matplotlib to visualise these findings

# 1. Histogram showing the distribution of sea-surface temperature
plt.hist(df_sst["sst"], bins=30, edgecolor="black")

plt.title("Distribution of Sea-Surface Temperature")
plt.xlabel("Sea-Surface Temperature (°C)")
plt.ylabel("Number of Observations")

plt.show()

# 2. Box plot showing the spread and potential outliers in SST by season


sns.boxplot(data=df_sst, x="season", y="sst",order=season_order)

plt.title("Sea-Surface Temperature by Season")
plt.xlabel("Season")
plt.ylabel("Sea-Surface Temperature (°C)")

plt.show()

#3. Whale Observations by Season
plt.figure(figsize=(10, 6))

sns.countplot( data=df_sst, x="season",order=season_order)

plt.title("Number of Whale Observations by Season")
plt.xlabel("Season")
plt.ylabel("Number of Observations")

plt.tight_layout()
plt.show()

#4. Bar Chart: Mean and Median SST by season

#Calculating the mean and median SST by season
season_sst_summary = (df_sst.groupby("season")["sst"].agg(["mean", "median"]).reindex(season_order)).reset_index()

season_sst_chart = season_sst_summary.melt(id_vars="season",value_vars=["mean", "median"],var_name="statistic",value_name="sst")

plt.figure(figsize=(10, 6))

sns.barplot(data=season_sst_chart, x="season", y="sst", hue="statistic", order=season_order)

plt.title("Mean and Median Sea-Surface Temperature by Season")
plt.xlabel("Season")
plt.ylabel("Sea-Surface Temperature (°C)")
plt.legend(title="Statistic")

plt.tight_layout()
plt.show()
#5: Observations by Sea Surface Temperature Range
#Calculating the number of observation by sst_range
# Divide SST values into five-degree ranges
df_sst["sst_range"] = pd.cut(
    df_sst["sst"],
    bins=[-5, 0, 5, 10, 15, 20, 25, 30, 35, 40],
    labels=[
        "-5 to 0°C",
        "0 to 5°C",
        "5 to 10°C",
        "10 to 15°C",
        "15 to 20°C",
        "20 to 25°C",
        "25 to 30°C",
        "30 to 35°C",
        "35 to 40°C"
    ],
    include_lowest=True
)
#I was having trouble with the above function and had to consult chatgpt to help me with the syntax.
# Count observations within each SST range
sst_range_counts = (df_sst["sst_range"].value_counts().sort_index().reset_index())

sst_range_counts.columns = ["sst_range","observation_count"]

plt.figure(figsize=(12, 6))

sns.barplot(data=sst_range_counts,x="sst_range",y="observation_count")

plt.title("Whale Observations by Sea-Surface Temperature Range")
plt.xlabel("Sea-Surface Temperature Range")
plt.ylabel("Number of Observations")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#6. Mean SST by Year
yearly_mean_sst = (df_sst.groupby("date_year")["sst"].mean().reset_index())

plt.figure(figsize=(12, 6))

sns.lineplot(data=yearly_mean_sst,x="date_year",y="sst",marker="o")

plt.title("Mean Sea-Surface Temperature of Whale Observations by Year")
plt.xlabel("Year")
plt.ylabel("Mean Sea-Surface Temperature (°C)")

plt.xticks(range(2010, 2026),rotation=45)

plt.tight_layout()
plt.show()

#Now I will begin my exploration of the sea-surface salinity data

#Exploration of the sea-surface temperature

print("sea-surface salinity (sss) analysis:")
print ("Mean sss:", np.mean(sss_array))
print ("Median sss:", np.median(sss_array))
print ("Maximum sss:", np.max(sss_array))
print ("Minimum sss:", np.min(sss_array))
print ("Standard deviation of sss:", np.std(sss_array))


#calculating the percentiles of the sss data
sss_percentiles = np.percentile(sss_array, [25, 50, 75])

print ("the SSS percentiles:")
print ("25th percentils:", sss_percentiles[0])
print ("50th percentils:", sss_percentiles[1])
print ("75th percentils:", sss_percentiles[2])

#I now will investigate if there are any outliers in the sss data using the IQR method.
sss_q1 = np.percentile(sss_array, 25)
sss_q3 = np.percentile(sss_array, 75)

sss_iqr = sss_q3 - sss_q1

sss_lower_bound = sss_q1 - (1.5 * sss_iqr)
sss_upper_bound = sss_q3 + (1.5 * sss_iqr)

print ("SSS lower boundary for outliers:", sss_lower_bound)
print ("SSS upper boundary for outliers:", sss_upper_bound)

sss_outliers = df_sss[(df_sss['sss'] < sss_lower_bound) | (df_sss['sss'] > sss_upper_bound)]
print ("Number of outliers in SSS data:", len(sss_outliers))
print ("Outliers in SSS data:")
print(sss_outliers[['eventDate', 'season', 'decimalLatitude', 'decimalLongitude', 'sss']].head(20))

#Investigating SSS values by season

# Investigate SSS values by season
# Investigate SSS values by season using the season order already created

for season in season_order:

    season_sss = df_sss.loc[df_sss["season"] == season,"sss"].to_numpy()

    print("\nSeason:", season)
    print("Number of observations:", len(season_sss))
    print("Mean SSS:", np.mean(season_sss))
    print("Median SSS:", np.median(season_sss))
    print("Minimum SSS:", np.min(season_sss))
    print("Maximum SSS:", np.max(season_sss))
    print("Standard deviation:", np.std(season_sss))