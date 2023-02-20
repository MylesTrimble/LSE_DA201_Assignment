#!/usr/bin/env python
# coding: utf-8

# # <div align="center"> Exploratory Analysis of NHS Data

# # <div align="center">GitHub repository

# ## <div align="center">[My gitHub Repository](https://github.com/MylesTrimble/Trimble_Myles_DA201_Assignment)

# # <div align="center">Import

# #### Libraries

# In[1]:


# Import libraries.
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Import warnings to ignore output warnings.
import warnings
warnings.filterwarnings('ignore')


# #### Data

# In[3]:


# Import relevant .csv  and excel files as DataFrames.
ad = pd.read_csv('actual_duration.csv')
ar = pd.read_csv('appointments_regional.csv')
nc = pd.read_excel('national_categories.xlsx')
tweets = pd.read_csv('tweets.csv')


# # <div align="center">Sense-Check the DataFrames

# ## <div align="center">Actual Duration (ad)

# In[4]:


# Determine the shape of the DataFrame.
print(ad.shape)

# Show the first 5 rows of the DataFrame.
ad.head()


# In[5]:


# Show the last 5 rows of the DataFrame
ad.tail()


# In[6]:


# Create list of column names.
ad_column_names = ad.columns.values.tolist()

# View the column name list.
ad_column_names


# In[7]:


# Determine the data types.
# (Output also shown in ad.info).
ad.dtypes


# In[8]:


# Retreive metadata for the DataFrame.
ad.info()


# ### <div align="center">Determine Missing Values

# In[9]:


# Create a new DataFrame and use the .isna() function to find missing values.
                  # .any(axis=1) tells Python to count instances of NaN values.
                       # axis=1 indicates column.
ad_na = ad[ad.isna().any(axis=1)]

# View the shape of the DataFrame.
ad_na.shape


# The output shows that there are 0 rows with NaN values within the 8 columns.

# In[10]:


# Determine the sum of missing values in 'icb_ons_code' column.
ad['icb_ons_code'].isnull().sum()


# Looking at the metadata output **(ad.info)** we can see that there are **137793 non_null entries** in each of the columns out of the index range **(RangeIndex: 137793 entries, 0 to 137792)**.
# 
# This, along with the alternative code methods above, we can safely assume there are no missing values in the **Actual Duration (ad)** DataFrame.

# ### <div align="center"> Descriptive Statistics

# In[11]:


# Perform descriptive statistics on DataFrame.
# This will only retrive descriptive statistics on the 'count_of_appointments'
# column as it is the only column that contains int64 values.
ad.describe()


# **Max, Min, Sum**

# In[12]:


# Create a title for context.
print("Count of Appointments")

# Max number of appointments
print("Min: ", ad['count_of_appointments'].min())

# Min number of appointments
print("Max: ", ad['count_of_appointments'].max())

# Sum of count of appointments
print("Sum: ", ad['count_of_appointments'].sum())


# **IQR**

# In[13]:


# Determine the first and third quartiles.
ad_Q1 = ad['count_of_appointments'].quantile(0.25)
ad_Q3 = ad['count_of_appointments'].quantile(0.75)

# Determine the interquartile range (IQR).
ad_IQR_count_of_appointments = ad_Q3 - ad_Q1

# View the output.
print("IQR: ", ad_IQR_count_of_appointments)


# **Variance**

# In[14]:


# Variance of the DataFrame.
print("Count of Appointment Variance:",
      ad['count_of_appointments'].var())


# ## <div align="center">Appointments Regional

# In[15]:


# Determine the shape of the DataFrame.
print(ar.shape)

# Show the first 5 rows of the DataFrame.
ar.head()


# In[16]:


# Retreive metadata for the DataFrame.
ar.info()


# ### <div align="center"> Determine Missing Values

# In[17]:


# Check for missing values.
# Create a new DataFrame and use the isna() function to find missing values.
                  # .any(axis=1) tells Python to count instances of NaN values
                       # axis=1 indicates column.
ar_na = ar[ar.isna().any(axis=1)]

# View the shape of the DataFrame.
ar_na.shape


# The output shows that there are 0 rows with NaN values within the 7 columns.

# In[18]:


# Show the sum of missing values in 'icb_ons_code' column.
ar['icb_ons_code'].isnull().sum()


# Looking at the metadata output **(ar.info)** we can see that there are **596821 non_null entries** in each of the columns out of the index range **(RangeIndex: 596821 entries, 0 to 596820)**.
# 
# This, along with the alternative code methods above, we can safely assume there are no missing values in the **Appointments Regional (ar)** DataFrame.

# ### <div align="center"> Descriptive Statistics

# In[19]:


# Perform descriptive statistics on DataFrame.
# This will only retrive descriptive statistics on the 'count_of_appointments'
# column as it is the only column that contains int64 values.
ar.describe()


# **Max, Min, Sum**

# In[20]:


# Create a title for context.
print("Count of Appointments")

# Min number of appointments.
print("Min: ", ar['count_of_appointments'].min())

# Max number of appointments.
print("Max: ", ar['count_of_appointments'].max())

# Sum of count of appointments.
print("Sum: ", ar['count_of_appointments'].sum())


# **IQR**

# In[21]:


# Determine the first and third quartiles.
ar_Q1 = ar['count_of_appointments'].quantile(0.25)
ar_Q3 = ar['count_of_appointments'].quantile(0.75)

# Determine the interquartile range (IQR).
ar_IQR_count_of_appointments = ar_Q3 - ar_Q1

# View the output.
print("IQR: ", ar_IQR_count_of_appointments)


# **Variance**

# In[22]:


# Determine the variance of the DataFrame.
print("Count of Appointment Variance:",
      ar['count_of_appointments'].var())


# ## <div align="center"> National Categories

# In[23]:


# Determine the shape of the DataFrame.
print(nc.shape)

# Show the first 5 rows of the DataFrame.
nc.head()


# In[24]:


# Retreive metadata for the DataFrame.
nc.info()


# ### <div align="center"> Determine Missing Values

# In[25]:


# Check for missing values.
# Create a new DataFrame and use the isna() function to find missing values.
                  # .any(axis=1) tells Python to count instances of NaN values.
                       # axis=1 indicates column.
nc_na = nc[nc.isna().any(axis=1)]

# View the shape of the DataFrame.
nc_na.shape


# The output shows that there are 0 rows with NaN values within the 8 columns.

# In[26]:


# Show the sum of missing values in 'icb_ons_code' column.
nc['icb_ons_code'].isnull().sum()


# Looking at the metadata output **(nc.info)** we can see that there are **817394 non_null entries** in each of the columns out of the index range **(RangeIndex: 817394 entries, 0 to 817393)**.
# 
# This, along with the alternative code methods above, we can safely assume there are no missing values in the **National Categories (nc)** DataFrame.

# We can now conclude that there are no missing values in any of the imported DataFrames.

# ### <div align="center"> Descriptive Statistics

# In[27]:


# Perform descriptive statistics on DataFrame.
# This will only retrive descriptive statistics on 'count_of_appointments'
# as it is the only int64.
nc.describe()


# **Max, Min, Sum**

# In[28]:


# Create title for context.
print("Count of Appointments")

# Min number of appointments.
print("Min: ", nc['count_of_appointments'].min())

# Max number of appointments.
print("Max: ", nc['count_of_appointments'].max())

# Sum of count of appointments.
print("Sum: ", nc['count_of_appointments'].sum())


# **IQR**

# In[29]:


# Determine the first and third quartiles.
nc_Q1 = nc['count_of_appointments'].quantile(0.25)
nc_Q3 = nc['count_of_appointments'].quantile(0.75)

# Determine the interquartile range (IQR).
nc_IQR_count_of_appointments = nc_Q3 - nc_Q1

# View the output.
print("IQR: ", nc_IQR_count_of_appointments)


# **Variance**

# In[30]:


# Determine the variance of the DataFrame.
print(nc['count_of_appointments'].var())


# # <div align="center"> Analyse the data

# ## <div align="center"> Initial Research

# ## <div align="center"> Between what dates were appointments scheduled?

# In[31]:


# View the data types and first five rows of appointment_date
# for the ad DataFrame to determine the date format.
print(ad.dtypes)
ad.head()


# In[32]:


# Change the date format of ad['appointment_date'] to datetime.
ad['appointment_date'] = pd.to_datetime(ad['appointment_date'])

# View the data types and DataFrame.
print(ad.dtypes)
ad.head()


# In[33]:


# View the data types and first five rows of appointment_month
# for the ar DataFrame to determine the date format.
print(ar.dtypes)
ar.head()


# In[34]:


# View the data types and first five rows of appointment_date
# for the nc DataFrame to determine the date format.
print(nc.dtypes)
nc.head()


# In[35]:


# Determine the minimum and maximum dates in the nc DataFrame.
print("The earliest appointment was scheduled for:",
      nc['appointment_date'].min())

print("The latest appointment was scheduled for:",
      nc['appointment_date'].max())


# In[36]:


# Determine the minimum and maximum dates in the ad DataFrame.
print("The earliest appointment was scheduled for:",
      ad['appointment_date'].min())

print("The latest appointment was scheduled for:",
      ad['appointment_date'].max())


# In[37]:


# Determine the minimum and maximum dates in the ar DataFrame.
print("The earliest appointment was scheduled in the month:",
      ar['appointment_month'].min())

print("The latest appointment was scheduled in the month:",
      ar['appointment_month'].max())


# After checking each DataFrame, we can be sure that the earliest appointment was scheduled in **January 2020** and the latest appointment was scheduled on **30th June 2022**.

# # <div align = "center"> Which month had the highest number of appointments?

# In[38]:


# Use groupby() to subset the ar DataFrame with
# appointment_month and count_of_appointments.
                                                  # Incorporate .agg() function
                                                  # to add the appointments.
nc_gpby_app = nc.groupby(['appointment_month'])                         ['count_of_appointments'].agg('sum').reset_index()

# Sort the subset to see the highest number of appointments.
nc_gpby_app.sort_values(by = 'count_of_appointments', ascending=False)


# The month with the highest number of appointments was **November (2021)**.
# 
# The lead up to Christmas 2021 (**Oct-Nov**) have the most amount of appointments by a significant margin.

# ## <div align = "center"> What was the total number of records per month?

# In[39]:


# Use .value_counts() to determine the number of records per month.
nc['appointment_month'].value_counts(ascending = False)


# Each month appears to have a similar number of records, but **March 2022** has the most (**82,822**) by a siginificant margin (**5,170**).

# # <div align="center"> How many locations are there in the data sets?

# In[40]:


# Determine the number of unique locations.
print("The number of locations in the National Categories DataFrame is:",
      len(nc['sub_icb_location_name'].unique()))


# In[41]:


# Determine the umber of unique locations using the 'sub_icb_location_code' column.
print("The number of locations in the Actual Duration DataFrame is:",
      len(ad['sub_icb_location_code'].unique()))


# There are the same amount of locations **(106)** for the **Actual Duration** and **National Categories** data sets.

# The result **(106)** also shown in the **.describe(include=['object', 'bool'])** code below.

# **Object & Boolean Types**

# In[42]:


# Perform descriptive statistics, including object and boolean types.
nc.describe(include=['object', 'bool'])


# In[43]:


# Perform descriptive statistics, including object and boolean types.
ad.describe(include=['object', 'bool'])


# Here, we can also see that there are:
# - **5 unique service settings**
# - **3 unique conntext types**
# - **18 unique national categories**

# # <div align="center"> What are the five locations with the highest number of records?

# In[44]:


# Determine which location in nc has the highest number of records using .value_counts().
nc['sub_icb_location_name'].value_counts(ascending=False)


# In[45]:


# Determine which location in ad has the highest number of records using .value_counts().
ad['sub_icb_location_name'].value_counts(ascending=False)


# We can see that the locations with the highest number of records are:
# - **North West London**
# - **Kent and Medway**
# - **Devon**
# - **Hampshire and Isle Of Wight**
# - **North East London**

# # <div align="center"> Which location had the highest number of appointments?

# Using **.groupby()** is an efficient and effective way to filter, group, and aggregate data.

# In[46]:


# Group by the location name and sum the 'count_of_appointments' data.
nc_loc = nc.groupby(['sub_icb_location_name', 'icb_ons_code'])             ['count_of_appointments'].agg('sum').reset_index()

# Sort the subset to see the highest number of appointments.
nc_loc.sort_values(by = 'count_of_appointments', ascending=False)


# The location with the highest number of appointments was:
# - **North West London** with **12142390** appointments.
# 
# Perhaps unsurprisingly, three of the top five locations with the highest number of recorded appointments were in London, which has the highest population density of anywhere in England (**14,500 people per square mile** at time of data collection).

# # <div align="center"> How many service settings, context types, national categories, and appointment statuses are there?

# In[47]:


# Determine the number of unique service settings.
print("The number of service settings is:",
      len(nc['service_setting'].unique()))

# List the unique service settings.
print("They are:", nc['service_setting'].unique())


# In[48]:


# Determine the number of unique context types.
print("The number of context types is:",
      len(nc['context_type'].unique()))

# List the unique context types.
print("They are:", nc['context_type'].unique())


# In[49]:


# Determine the number of unique national categories.
print("The number of national categories is:",
      len(nc['national_category'].unique()))

# List the unique national categories.
print("They are:", nc['national_category'].unique())


# In[50]:


# Determine the number of unique appointment statuses.
print("The number of appointment statuses is:",
      len(ar['appointment_status'].unique()))

# List the unique appointment statuses.
print("They are:", ar['appointment_status'].unique())


# ## <div align="center"> Which service setting reported the most appointments in North West London from 1 January to 1 June 2022?

# Creating a new, subsetted DataFrame with **.groupby()** allows for more detailed filtering, as shown here with filtering for particular dates and location name.

# In[51]:


# Create a subset of the nc DataFrame.
nc_NWL = nc.groupby(['sub_icb_location_name', 'service_setting',
                     'appointment_date'])\
                    ['count_of_appointments'].agg('sum').reset_index()

# Filter subset for specific date range.
nc_NWL = nc_NWL[(nc_NWL['appointment_date'] > "2022-01-01") 
                      & (nc_NWL['appointment_date'] < "2022-06-01")]

# Filter subset for specific location.
nc_NWL = nc_NWL[nc_NWL['sub_icb_location_name']         .str.contains("NHS North West London ICB - W2U3Z")]

# Sort the subset DataFrame to view which service setting
# reported the most appointments.
nc_NWL.sort_values(by = ['count_of_appointments'], ascending=False)


# ## <div align="center"> Further Exploration

# I included the **appointment-date** column in the **.groupby()** initially so as to glean an understanding of which dates and months had more appointments with each **service setting**, but I also wanted to see an overview of exactly how many appointments each **service setting** had overall, as shown with the code below.

# #### Overall

# In[52]:


# Create a subset of the nc DataFrame.
nc_NWL_ss = nc.groupby(['sub_icb_location_name', 'service_setting'])                       ['count_of_appointments'].agg('sum').reset_index()

# Filter subset for specific location.
nc_NWL_ss = nc_NWL_ss[nc_NWL_ss['sub_icb_location_name']            .str.contains("NHS North West London ICB - W2U3Z")]

# Sort the subset DataFrame to view which service setting
# reported the most appointments.
nc_NWL_ss.sort_values(by = ['count_of_appointments'], ascending=False)


# In order to understand the data in more detail, I decided to expand the date selection and investigate the prevalence of **Context Types** and **National Categories**.

# ### <div align="center"> Which context type reported the most appointments in North West London from 1 August 2021 to 30 June 2022?

# In[53]:


# Create a subset of the nc DataFrame.
nc_NWL_ct = nc.groupby(['sub_icb_location_name', 'context_type'])                       ['count_of_appointments'].agg('sum').reset_index()

# Filter subset for specific location.
nc_NWL_ct = nc_NWL_ct[nc_NWL_ct['sub_icb_location_name']            .str.contains("NHS North West London ICB - W2U3Z")]

# Sort the subset DataFrame to view which context type
# reported the most appointments.
nc_NWL_ct.sort_values(by = ['count_of_appointments'], ascending=False)


# ### <div align="center"> Which national category reported the most appointments in North West London from 1 August 2021 to 30 June 2022?

# In[54]:


# Create a subset of the nc DataFrame.
nc_NWL_nc = nc.groupby(['sub_icb_location_name', 'national_category'])                       ['count_of_appointments'].agg('sum').reset_index()

# Filter subset for specific location.
nc_NWL_nc = nc_NWL_nc[nc_NWL_nc['sub_icb_location_name']            .str.contains("NHS North West London ICB - W2U3Z")]

# Sort the subset DataFrame to view which national category
# reported the most appointments.
nc_NWL_nc.sort_values(by = ['count_of_appointments'], ascending=False)


# I decided to investigate some of the other locations with the highest number of appointments to see if there were any national trends in prevelance of **service setting, context type, and national category**.

# ### <div align = "center"> Which service setting / context type / national category reported the most appointments in North East London from 1 August 2021 to 30 June 2022?

# #### Service Setting

# In[55]:


# Create a subset of the nc DataFrame.
nc_NEL_ss = nc.groupby(['sub_icb_location_name', 'service_setting'])                       ['count_of_appointments'].agg('sum').reset_index()

# Filter subset for specific location.
nc_NEL_ss = nc_NEL_ss[nc_NEL_ss['sub_icb_location_name']            .str.contains("NHS North East London ICB - A3A8R")]

# Sort the subset DataFrame to view which service setting
# reported the most appointments.
nc_NEL_ss.sort_values(by = ['count_of_appointments'], ascending=False)


# #### Context Type

# In[56]:


# Create a subset of the nc DataFrame.
nc_NEL_ct = nc.groupby(['sub_icb_location_name', 'context_type'])                       ['count_of_appointments'].agg('sum').reset_index()

# Filter subset for specific location.
nc_NEL_ct = nc_NEL_ct[nc_NEL_ct['sub_icb_location_name']            .str.contains("NHS North East London ICB - A3A8R")]

# Sort the subset DataFrame to view which context type
# reported the most appointments.
nc_NEL_ct.sort_values(by = ['count_of_appointments'], ascending=False)


# #### National Category

# In[57]:


# Create a subset of the nc DataFrame.
nc_NEL_nc = nc.groupby(['sub_icb_location_name', 'national_category'])                       ['count_of_appointments'].agg('sum').reset_index()

# Filter subset for specific location.
nc_NEL_nc = nc_NEL_nc[nc_NEL_nc['sub_icb_location_name']            .str.contains("NHS North East London ICB - A3A8R")]

# Sort the subset DataFrame to view which national category
# reported the most appointments.
nc_NEL_nc.sort_values(by = ['count_of_appointments'], ascending=False)


# ### <div align = "center"> Which service setting / context type / national category reported the most appointments in Kent and Medway from 1 January 2021 to 30 June 2022?

# #### Service Setting

# In[58]:


# Create a subset of the nc DataFrame.
nc_KM_ss = nc.groupby(['sub_icb_location_name', 'service_setting'])                      ['count_of_appointments'].agg('sum').reset_index()

# Filter subset for specific location.
nc_KM_ss = nc_KM_ss[nc_KM_ss['sub_icb_location_name']           .str.contains('NHS Kent and Medway ICB - 91Q')]

# Sort the subset DataFrame to view which service setting
# reported the most appointments.
nc_KM_ss.sort_values(by = ['count_of_appointments'], ascending=False)


# #### Context Type

# In[59]:


# Create a subset of the nc DataFrame.
nc_KM_ct = nc.groupby(['sub_icb_location_name', 'context_type'])                      ['count_of_appointments'].agg('sum').reset_index()

# Filter subset for specific location.
nc_KM_ct = nc_KM_ct[nc_KM_ct['sub_icb_location_name']           .str.contains('NHS Kent and Medway ICB - 91Q')]

# Sort the subset DataFrame to view which context type
# reported the most appointments.
nc_KM_ct.sort_values(by = ['count_of_appointments'], ascending=False)


# #### National Category

# In[60]:


# Create a subset of the nc DataFrame.
nc_KM_nc = nc.groupby(['sub_icb_location_name', 'national_category'])                      ['count_of_appointments'].agg('sum').reset_index()

# Filter subset for specific location.
nc_KM_nc = nc_KM_nc[nc_KM_nc['sub_icb_location_name']           .str.contains('NHS Kent and Medway ICB - 91Q')]

# Sort the subset DataFrame to view which national category
# reported the most appointments.
nc_KM_nc.sort_values(by = ['count_of_appointments'], ascending=False)


# The 3 locations with the highest number of appointments all show to have the most appointments occurring within:
# - Service Setting
#     - **GP**
# - Context Type
#     - **Care Related Encounter**
# - National Category
#     - **General Consultation Routine**

# # <div align = "center"> Visualise and Identify Initial Trends

# ### <div align = "center"> Create three visualisations indicating the number of appointments per month for service settings, context types, and national categories.

# I chose to use a similar design throughout all of my visualisations so as to maintain an aesthetic consistency.
# - For example, the spines of each plot has been removed for decluttering purposes and the **colorblind** palette was used throughout so as to increase accessibility.

# ### <div align = "center"> Service Setting (nc_ss)

# In[61]:


# Aggregate on monthly level and determine the sum of records per month.
nc_ss = nc.groupby(['appointment_month', 'service_setting'])                   ['count_of_appointments'].agg('sum').reset_index()


# In[62]:


# Import matplotlib.ticker for tick formatting capabilities.
import matplotlib.ticker as ticker


# In[121]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Set figure size.
sns.set(rc = {'figure.figsize':(16, 10)})


# Create a line plot.
sns.lineplot(x = 'appointment_month', y = 'count_of_appointments',
             hue = 'service_setting', ci = None,
             palette = 'colorblind', data = nc_ss)


# Format figure attributes:

# Set plot style.
sns.set_style('white')

#Set title.
plt.title('Appointments for each Service Setting Over Time', fontsize = 30)

# Set x and y axis headers.
plt.xlabel('Appointment Month', fontsize = 20)
plt.ylabel('Count of Appointments (millions)', fontsize = 20)

# Set a higher y-axis limit for clearer understanding of the plot.
ax.set_ylim(0, 30000000)

# Ensure axis ticks are present.
sns.set_style('ticks')

# Create a legend indicating the different Service Settings.
plt.legend(title = 'Service Setting', fontsize = 12,
           bbox_to_anchor = (1, .5), loc = 'center right', borderaxespad = -4)

# Add annotation lines at significant obserrvations.
plt.axvline(x = '2021-08', color = 'r', linestyle = '--')
plt.axvline(x = '2021-11', color = 'r', linestyle = '--')
plt.axvline(x = '2022-02', color = 'r', linestyle = '--')
plt.axvline(x = '2022-04', color = 'r', linestyle = '--')

# Define the scale of the y-axis for clarity.
scale_y = 1e6
ticks_y = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x / scale_y))
ax.yaxis.set_major_formatter(ticks_y)

# Despine the plot.
sns.despine()


# View the plot.
plt.show()

# Save the plot.
fig.savefig('Appointments for each Service Setting Over Time.jpg')


# We can clearly see spikes in appointments for each **Service Setting**, particularly **General Practice**, in the run-up to Chrismtas 2021 and in **March 2022** (as marked by the vertical dash annotation lines).
# 
# This is consistent with the previous finding that **March 2022** had the highest number of records out of every month.
# 
# There are also dips in appointments during **December 2021** up until **Febuary 2022**, and in **April 2022**.

# As the **general practice** service setting shows to have a significantly higher number of appointments compared to the rest of the service settings, I chose to view it in isolation and the others together so as to see a clearer picture of how each changed over time.

# #### General Practice Alone

# In[64]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Create a line plot
sns.lineplot(x = 'appointment_month', y = 'count_of_appointments',
             ci = None, palette = 'colorblind',
             data = nc_ss[nc_ss['service_setting'] == 'General Practice'])

# Format figure attributes.
plt.title('Appointments for General Practice Over Time', fontsize = 25)
plt.xlabel('Appointment Month', fontsize = 15)
plt.ylabel('Count of Appointments (millions)', fontsize = 15)
ax.set_ylim(20000000, 30000000)
ax.yaxis.set_major_formatter(ticks_y)
sns.despine()

# View the plot.
plt.show()

# Save the plot.
fig.savefig('Appointments for General Practice Over Time.png')


# #### Other Service Settings

# In[65]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Create a line plot
sns.lineplot(x = 'appointment_month', y = 'count_of_appointments',
             hue = 'service_setting', ci = None, palette = 'colorblind',
             data = nc_ss[nc_ss['service_setting'].isin(['Extended Access Provision',
                                                         'Primary Care Network',
                                                         'Other',
                                                         'Unmapped'])])

# Format figure attributes.
plt.title('Appointments for Service Settings (Excluding GP) Over Time', fontsize = 25)
plt.xlabel('Appointment Month', fontsize = 15)
plt.ylabel('Count of Appointments (millions)', fontsize = 15)
plt.legend(title = 'Service Setting', fontsize = 13,
           bbox_to_anchor = (1, 1),
           loc = 'upper right', borderaxespad = 2)
ax.yaxis.set_major_formatter(ticks_y)
sns.despine()

# Save the plot.
fig.savefig('Appointments for each Service Setting (Excluding GP) Over Time.jpg')


# On closer inspection, we can see that the rise in number of appointments for service settings other than **general practice** are, in relative terms, also significant increases.
# 
# While it is useful to view these variables over time, it would also be beneficial to get a sense of the spread of appointments across each **Service Setting** (excluding **GP**).

# In[66]:


# # Create a new DataFrame excluding General Practice.
nc_ss_2 = nc_ss[-(nc_ss['service_setting'] == 'General Practice')]


# In[67]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

box_plot = sns.boxplot(x = 'service_setting', y = 'count_of_appointments',
                       palette = 'colorblind', data = nc_ss_2)

# Format figure attributes.
plt.title('The Spread of Appointments for Each Service Setting (Excluding GP)',
          fontsize = 25)
plt.xlabel('Service Setting', fontsize = 15)
plt.ylabel('Count of Appointments (millions)', fontsize = 15)
ax.yaxis.set_major_formatter(ticks_y)
sns.despine()

# Create a Series of the median appointments for each Service Setting.
medians = nc_ss_2.groupby('service_setting')['count_of_appointments'].median()

# Annotate the boxplot with the median values.
for i in range(len(medians)):
    box_plot.annotate(str(medians[i]), xy = (i, medians[i]),
                      horizontalalignment = 'center', color = 'white',
                      fontweight = 'semibold', size = 12,
                      bbox = dict(facecolor = '#828280', edgecolor = '#828282'))

# Save the plot.
fig.savefig('The Spread of Each Service Settings (Excluding GP).jpg')


# The **Unmapped** category contains more records than the others.
#    - It would be useful to try to understand why this is the case as the true mapping of these data points may change the distribution significantly.
#         - Could it be due to poor data collection?
#         - Was data collection only poor during the months recorded in these datasets?
#             - Perhaps analysing data from preceding and succeeding months could answer this question.

# ### <div align = "center"> Context Types (nc_ct)

# In[68]:


# Aggregate on monthly level and determine the sum of records per month.
nc_ct = nc.groupby(['appointment_month', 'context_type'])['count_of_appointments']        .agg('sum').reset_index()


# In[69]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Create a line plot.
sns.lineplot(x = 'appointment_month', y = 'count_of_appointments',
             hue = 'context_type', ci = None, palette = 'colorblind',
             data = nc_ct)

# Format figure attributes.
plt.title('Appointments for each Context Type Over Time', fontsize = 25)
plt.xlabel('Appointment Month', fontsize = 20)
plt.ylabel('Count of Appointments (millions)', fontsize = 20)
plt.legend(title = 'Context Type', fontsize = 12,
           bbox_to_anchor = (1, .5), loc = 'center right',
           borderaxespad = -4)
plt.axvline(x = '2021-08', color = 'r', linestyle = '--')
plt.axvline(x = '2021-11', color = 'r', linestyle = '--')
plt.axvline(x = '2022-02', color = 'r', linestyle = '--')
plt.axvline(x = '2022-04', color = 'r', linestyle = '--')
ax.yaxis.set_major_formatter(ticks_y)
sns.despine()

# Save the plot.
fig.savefig('Appointments for each Context Type Over Time.jpg')


# We can clearly see spikes in appointments for the **Care Related Encounter** context type in the run-up to Chrismtas 2021 and in **March 2022**.
# 
# This is a similar trend to that of the service settings.

# ### <div align = "center"> National Categories (nc_nc)

# In[70]:


# Aggregate on monthly level and determine the sum of records per month.
nc_nc = nc.groupby(['appointment_month', 'national_category'])['count_of_appointments']        .agg('sum').reset_index()


# In[71]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Create a line plot.
sns.lineplot(x = 'appointment_month', y = 'count_of_appointments',
             hue = 'national_category', ci = None,
             palette = 'colorblind', data = nc_nc)

# Format figure attributes.
plt.title('Appointments for each National Category Over Time', fontsize = 25)
plt.xlabel('Appointment Month', fontsize = 15)
plt.ylabel('Count of Appointments (millions)', fontsize = 15)
plt.legend(title = 'National Category', fontsize = 12,
           bbox_to_anchor = (.97, .75), loc = 'upper left', borderaxespad = 0)
plt.axvline(x = '2021-08', color = 'r', linestyle = '--')
plt.axvline(x = '2021-11', color = 'r', linestyle = '--')
plt.axvline(x = '2022-02', color = 'r', linestyle = '--')
plt.axvline(x = '2022-04', color = 'r', linestyle = '--')
ax.yaxis.set_major_formatter(ticks_y)
sns.despine()


# While the above plot is informative in a broad sense, it is rather "busy" aesthetically, and so it may be more beneficial from the analytical perspective of looking to see where resources have been most utilised, to filter for the **National Categories** that have higher appointments.

# In[72]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Create a line plot.
sns.lineplot(x = 'appointment_month', y = 'count_of_appointments',
             hue = 'national_category', ci = None,
             palette = 'colorblind',
             data = nc_nc[nc_nc['count_of_appointments'] > 1500000])

# Format figure attributes.
plt.title('Appointments for National Categories Over Time (Apps > 1.2m)',
          fontsize = 25)
plt.xlabel('Appointment Month', fontsize = 20)
plt.ylabel('Count of Appointments (millions)', fontsize = 20)
plt.legend(title = 'National Category', fontsize = 12,
           bbox_to_anchor = (.9, .7), loc = 'upper left', borderaxespad = 0)
plt.axvline(x = '2021-08', color = 'r', linestyle = '--')
plt.axvline(x = '2021-11', color = 'r', linestyle = '--')
plt.axvline(x = '2022-02', color = 'r', linestyle = '--')
plt.axvline(x = '2022-04', color = 'r', linestyle = '--')
ax.yaxis.set_major_formatter(ticks_y)
sns.despine()

# Save the plot.
fig.savefig('Appointments for National Categories Over Time (Apps > 1.2m).jpg')


# We can clearly see spikes in appointments for each **National Category**, particularly **General Consultation Routine** and **Planned Clinical Procedure** in the run-up to Christmas 2021 and in **March 2022**.

# Perhaps the reason for the trend for each of the **service settings**, **context types** and most of the **national categories** having dips in the number of appointments in **December 2021** could be explained by the NHS having restricted availability of appointments due to the Christmas holiday period.

# ### <div align = "center"> Create four visualisations indicating the number of appointments for service setting per season.
# #### <div align = "center"> The seasons are summer (August 2021), autumn (October 2021), winter (January 2022), and spring (April 2022).

# In[73]:


# Aggregate on a monthly level and determine the sum of records per month.
nc_ss_season = nc.groupby(['appointment_month',
                           'appointment_date',
                           'service_setting'])\
                          ['count_of_appointments'].agg('sum').reset_index()


# ### Summer 2021

# **Using between()**

# In[74]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Create a line plot filtering for Summer 2021 (August 2021).
sns.lineplot(x = 'appointment_date', y = 'count_of_appointments',
             hue = 'service_setting', ci = None,
             palette = 'colorblind',
             data = nc_ss_season[nc_ss_season['appointment_date']\
                                 .between('2021-08-01', '2021-08-31')])

# Format figure attributes.
plt.title('Appointments for each Service Setting (Summer 2021)',
          fontsize = 25)
plt.xlabel('Appointment Date', fontsize = 15)
plt.ylabel('Count of Appointments (millions)', fontsize = 15)
plt.legend(title = 'Service Setting', fontsize = 12,
           bbox_to_anchor = (1, .5), loc = 'upper left', borderaxespad = 0)
ax.set_xlim(['2021-08-01'], ['2021-08-31'])
ax.yaxis.set_major_formatter(ticks_y)
sns.despine()


# The dips (gaps) in appointments are weekends (Sundays have no records).
# 
# The spikes in appointments are Mondays (particularly high for the **GP** service setting).
# 
# Appointments are booked mainly for earlier in each week and are consistent throughout the month.

# ### Autumn 2021

# **Using isin()**

# In[75]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Create a line plot filtering for Autumn 2021 (October 2021).
sns.lineplot(x = 'appointment_date', y = 'count_of_appointments',
             hue = 'service_setting', ci = None, palette = 'colorblind',
             data = nc_ss_season[nc_ss_season['appointment_month']\
                                 .isin(['2021-10'])])

# Format figure attributes.
plt.title('Appointments for each Service Setting (Autumn 2021)',
          fontsize = 25)
plt.xlabel('Appointment Date', fontsize = 15)
plt.ylabel('Count of Appointments (millions)', fontsize = 15)
plt.legend(title = 'Service Setting', fontsize = 12,
           bbox_to_anchor = (.97, .5), loc = 'upper left',
           borderaxespad = 0)
ax.set_xlim(['2021-10-01'], ['2021-10-31'])
ax.yaxis.set_major_formatter(ticks_y)
sns.despine()


# ### Winter 2021

# **Using ==**

# In[76]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Create a line plot filtering for Winter 2021 (January 2021).
sns.lineplot(x = 'appointment_date', y = 'count_of_appointments',
             hue = 'service_setting', ci = None, palette = 'colorblind',
             data = nc_ss_season[nc_ss_season['appointment_month'] == '2021-12'])

# Format figure attributes.
plt.title('Appointments for each Service Setting (Winter 2021)', fontsize = 25)
plt.xlabel('Appointment Date', fontsize = 15)
plt.ylabel('Count of Appointments (millions)', fontsize = 15)
plt.legend(title = 'Service Setting', fontsize = 12,
           bbox_to_anchor = (1, .5), loc ='upper left', borderaxespad = 0)
ax.set_xlim(['2021-12-01'], ['2021-12-31'])
ax.yaxis.set_major_formatter(ticks_y)
sns.despine()


# As expected, we can see a decrease in the number of appointments for each **service setting**, particularly for **General Practice**, as December progresses.
# 
# There is also seemingly a gap in records between December 25 and December 28, which can most likely be explained by GP Christmas holiday hours.

# ### Spring 2022

# In[77]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Create a line plot filtering for Spring 2022 (April 2022).
sns.lineplot(x = 'appointment_date', y = 'count_of_appointments',
             hue = 'service_setting', ci = None, palette = 'colorblind',
             data = nc_ss_season[nc_ss_season['appointment_month'] == '2022-04'])

# Format figure attributes.
plt.title('Appointments for each Service Setting (Spring 2022)', fontsize = 25)
plt.xlabel('Appointment Date', fontsize = 15)
plt.ylabel('Count of Appointments (millions)', fontsize = 15)
plt.legend(title = 'Service Setting', fontsize = 12,
           bbox_to_anchor=(1, .5), loc='upper left', borderaxespad=0)
ax.set_xlim(['2022-04-01'], ['2022-04-30'])
ax.yaxis.set_major_formatter(ticks_y)
sns.despine()


# ## <div align="center"> Further Exploration

# ### <div align="center"> Create a Line Plot showing the change in number of appointments during the run-up to Christmas 2021.

# In[78]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Create a line plot filtering for Christmas Run-Up 2021 (Sept 2021 - Jan 2022).
sns.lineplot(x = 'appointment_month', y = 'count_of_appointments',
             hue = 'service_setting', ci = None, palette = 'colorblind',
             data = nc_ss_season[nc_ss_season['appointment_month']\
                                 .between('2021-09', '2022-01')])

# Format figure attributes.
plt.title('Appointments for each Service Setting (Christmas Run-Up 2021)',
          fontsize = 25)
plt.xlabel('Appointment Date', fontsize = 20)
plt.ylabel('Number of Appointments (millions)', fontsize = 20)
plt.legend(title = 'Service Setting', fontsize = 12,
           bbox_to_anchor = (.9, .7), loc = 'upper left', borderaxespad = 1)
ax.set_xlim(['2021-09'], ['2022-01'])
ax.yaxis.set_major_formatter(ticks_y)
sns.despine()

# Save the plot.
fig.savefig('Appointments for each Service Setting (Christmas Run-Up 2021.jpg')


# The busy period of **October - December** may be explained by:
# 
# - "The NHS is always under considerable pressure over the winter period as demand for services tends to increase significantly with the onset of cold weather and flu."
#     - [NHS Providers](https://nhsproviders.org/topics/delivery-and-performance/winter-pressures#:~:text=The%20NHS%20frontline%20is%20always,of%20cold%20weather%20and%20flu.)
# 
# 
# - Perhaps the decrease in appointment numbers in **December** was due, in part, to the shortages in staff across the NHS over the Christmas period.
#     - [The Independent](https://www.independent.co.uk/news/health/nhs-mass-staff-shortage-christmas-b1981961.html)

# ### <div align="center"> How do the Healthcare Professional Types differ over time?

# In[79]:


# Subset the ar DataFrame, aggregating the hcp_type
# with count_of_appointments.
ar_hcp = ar.groupby(['hcp_type', 'appointment_month'])                    ['count_of_appointments'].agg('sum').reset_index()


# In[80]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Create a line plot.
sns.lineplot(x = 'appointment_month', y = 'count_of_appointments',
             hue = 'hcp_type', ci = None, palette = 'colorblind',
             data = ar_hcp)

# Format figure attributes.
plt.title('The Change in Healthcare Provider Types Over Time',
          fontsize = 25)
plt.xlabel('Appointment Month', fontsize = 20)
plt.ylabel('Number of Appointments (millions)', fontsize = 20)
plt.legend(title = 'Healthcare Provider', fontsize = 15,
           bbox_to_anchor = (.9, .5), loc = 'upper left', borderaxespad = 0)
plt.xticks(rotation = 40)
ax.yaxis.set_major_formatter(ticks_y)
sns.despine()

# Save the plot.
fig.savefig('The Change in Healthcare Provider Types Over Time.jpg')


# **GP** and **Other Practice Staff** seem to follow a similar trajectory.
# 
# - In **October 2020** and **2021** the **Other Practice Staff** category exceeds **GP** in the number of appointmets.
#     - It would be useful to access more specific staff data to break the Other Practice Staff category into its contained roles and see how in-demand they are during busy periods.
# 
# 
# We can see that there was a significant drop in appointments for both **GP** and **Other Practice Staff** between **January 2020** and **April 2020** which may be explained by the fact that these first few months of 2020 were when media and government coverage of the COVID-19 pandemic was taking hold in the UK, leading ultimately to the first of the nation-wide lockdowns, which meant that most people wouldn't have been able to attend appointments.
# 
# - This plot does not necessarily mean that all appointments dropped in number during this time.
#     - I would like to investigate whether all modes of appointments decreased in number during this period or was it just those which were Face-to-Face.

# ### <div align="center"> Display the change in number of appointments for each appointment mode over time.

# In[81]:


# Create a subset of the ar DataFrame, aggregating the
# appointment mode and count of appoinntments.
ar_mode = ar.groupby(['appointment_mode', 'appointment_month'])                     ['count_of_appointments'].agg('sum').reset_index()


# In[82]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Create a line plot.
sns.lineplot(x = 'appointment_month', y = 'count_of_appointments',
             hue = 'appointment_mode', ci = None,
             palette = 'colorblind',
             data = ar_mode)

# Format figure attributes.
plt.title('The Change in Appointment Modes over Time',
          fontsize = 25)
plt.xlabel('Appointment Month', fontsize = 20)
plt.ylabel('Number of Appointments (millions)', fontsize = 20)
plt.legend(title = 'Appointment Mode', fontsize = 12,
           bbox_to_anchor = (.9, .33), loc = 'upper left',
           borderaxespad = 0)
plt.xticks(rotation = 40)
plt.axvline(x = '2020-01', color = 'y', linestyle = '--')
plt.axvline(x = '2020-04', color = 'y', linestyle = '--')
ax.yaxis.set_major_formatter(ticks_y)
sns.despine()

# Save the plot.
fig.savefig('The Change in Appointment Modes over Time.jpg')


# Here we can see that as the UK entered lockdown, people were unable to physically attend appointments. Therefore, we could surmise that appointments via **telephone** were where patients turned to, as it is the only **mode** to rise, and they rose dramatically during this period and beyond.
# 
# As the vaccine was rolled out in the UK in late 2020 / early 2021 and the government eased lockdown restrictions, we can see the resulting gradual fall in **telephone** appointments and rise in those which were **Face-to-Face**.
# 
# It is also apparent that during the busiest months (**September - November 2021** and **March 2022**) the number of **Face-to-Face** appointments rose significantly.
#    - This seems to be a clear indication of where the NHS' resources are being utilised in busy periods.
#    
# - Was the NHS prepared for this rise in telephone appointments?

# ### <div align="center"> Should the NHS look at increasing staff levels?

# In[83]:


# Create a new DataFrame with only the appointment month
# and the aggregated sum of appointments.
ar_sub = ar.groupby('appointment_month')         ['count_of_appointments'].agg('sum').reset_index()

# Add a column to the new DataFrame indicating the average
# utilisation of service per day.
ar_sub['utilisation'] = ar_sub.count_of_appointments / 30

# Round the output to 2 decimal places.
ar_sub['utilisation'] = ar_sub['utilisation'].round(decimals = 1)

# View the output.
ar_sub


# In[84]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Create a line plot.
sns.lineplot(x = 'appointment_month', y = 'utilisation',
             data = ar_sub)

# Format figure attributes.
plt.title('Monthly Capacity Utilisation',
          fontsize = 25)
plt.xlabel('Appointment Month', fontsize = 20)
plt.ylabel('Utilisation (millions)', fontsize = 20)
plt.xticks(rotation = 40)
ax.yaxis.set_major_formatter(ticks_y)
sns.despine()


# In[85]:


# Create a new DataFrame with only the appointment month
# and the aggregated sum of appointments.
ar_sub_2 = ar.groupby(['appointment_month', 'appointment_mode'])         ['count_of_appointments'].agg('sum').reset_index()

# Add a column to the new DataFrame indicating the average
# utilisation of service per day.
ar_sub_2['utilisation'] = ar_sub_2.count_of_appointments / 30

# Round the output to 2 decimal places.
ar_sub_2['utilisation'] = ar_sub_2['utilisation'].round(decimals = 1)

# View the output.
ar_sub_2.sort_values(by = 'utilisation', ascending = False)


# Although the following plot is a scaled down version of the previous plot viewing the change in **appointment modes** overe time, it is also worth viewing the monthly capacity **utilisation** of each **appointment mode**.

# In[86]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Create a line plot.
sns.lineplot(x = 'appointment_month', y = 'utilisation',
             hue = 'appointment_mode', palette = 'colorblind',
             data = ar_sub_2)

# Format figure attributes.
plt.title('Monthly Capacity Utilisation of Each Appointment Mode',
          fontsize = 25)
plt.xlabel('Appointment Month', fontsize = 20)
plt.ylabel('Utilisation', fontsize = 20)
plt.legend(title = 'Appointment Mode', fontsize = 12,
           bbox_to_anchor = (.95, .65), loc = 'upper left',
           borderaxespad = 0)
plt.xticks(rotation = 40)
sns.despine()


# I have also created a chart focusing specifically on the utilisation of resources for **telephone** appointments to highlight the sharp rise in resource allocation.

# In[87]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Create a line plot.
sns.lineplot(x = 'appointment_month', y = 'utilisation',
             data = ar_sub_2[ar_sub_2['appointment_mode'] == 'Telephone'])

# Format figure attributes.
plt.title('Monthly Capacity Utilisation (Telephone Appointments)',
          fontsize = 25)
plt.xlabel('Appointment Month', fontsize = 20)
plt.ylabel('Utilisation', fontsize = 20)
sns.set_style('ticks')
plt.xticks(rotation=40)
sns.despine()


# I also thought it pertinent to display the NHS resource utilisation using the larger data set within the **National Categories** DataFrame, which highlights, quite starkly, the demands on the NHS during the busiest months.

# In[88]:


# Create a new DataFrame with only the appointment month
# and the aggregated sum of appointments.
nc_sub = nc.groupby('appointment_month')         ['count_of_appointments'].agg('sum').reset_index()

# Add a column to the new DataFrame indicating the average
# utilisation of service per day.
nc_sub['utilisation'] = nc_sub.count_of_appointments / 30

# Round the output to 2 decimal places.
nc_sub['utilisation'] = nc_sub['utilisation'].round(decimals = 1)

# View the output.
nc_sub.sort_values(by = 'utilisation', ascending = False)


# In[89]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Create a line plot.
sns.lineplot(x = 'appointment_month', y = 'utilisation',
             data = nc_sub)

# Format figure attributes.
plt.title('Monthly Capacity Utilisation (National)',
          fontsize = 25)
plt.xlabel('Appointment Month', fontsize = 20)
plt.ylabel('Utilisation (millions)', fontsize = 20)
ax.yaxis.set_major_formatter(ticks_y)
sns.despine()


# ### <div align="center"> Display the proportion of appointments in relation to the time between booking and appointment.

# In[90]:


# Create a subset of the ar DataFrame, aggregating the
# 'time_between_book_and_appointment' and count_of_appointments.
ar_book = ar.groupby(['time_between_book_and_appointment',
                      'appointment_month'])\
                     ['count_of_appointments'].agg('sum').reset_index()

# Determine the unique category names for the
# 'time_between_book_and_appointment' column.
ar_book['time_between_book_and_appointment'].unique()


# In[91]:


# Convert the values in the subset to categorical.
ar_book['time_between_book_and_appointment'] =        pd.Categorical(ar_book['time_between_book_and_appointment'],
                       ['Same Day', '1 Day', '2 to 7 Days', '8  to 14 Days',
                        '15  to 21 Days', '22  to 28 Days', 'More than 28 Days',
                        'Unknown / Data Quality'])

# View the data types.
print(ar_book.dtypes)


# In[92]:


# Use the unique category values to create a chronological order.
my_order = ['Same Day', '1 Day', '2 to 7 Days', '8  to 14 Days',
            '15  to 21 Days', '22  to 28 Days', 'More than 28 Days',
            'Unknown / Data Quality']

# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Create a bar plot.
sns.barplot(x = 'time_between_book_and_appointment',
            y = 'count_of_appointments',
            data = ar_book, order = my_order,
            palette = 'colorblind')

# Format figure attributes.
plt.title('Appointments for each Booking Wait Time Period',
          fontsize = 25)
plt.xlabel('Time Between Booking and Appointment', fontsize = 20)
plt.ylabel('Number of Appointments (millions)', fontsize = 20)
plt.xticks(rotation = 30)
ax.yaxis.set_major_formatter(ticks_y)
sns.despine()


# We can see that there is a trend of most appointments being booked for the same day, with fewer being booked as the wait time increases.

# ### <div align="center"> Display the change in time between booking and appointment over time.

# In[93]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Create a line plot.
sns.lineplot(x = 'appointment_month', y = 'count_of_appointments',
             hue = 'time_between_book_and_appointment',
             hue_order = my_order,
             palette = 'colorblind',
             data = ar_book)

# Format figure attributes.
plt.title('Changes in Time Between Booking and Appointment Over Time',
          fontsize = 25)
plt.xlabel('Appointment Month', fontsize = 20)
plt.ylabel('Number of Appointments (millions)',
           fontsize = 20)
plt.legend(title = 'Time Between Booking and Appointment',
           fontsize = 12,
           bbox_to_anchor = (.87, .77), loc = 'upper left',
           borderaxespad = 0)
plt.xticks(['2020-01', '2020-04', '2020-07', '2020-10',
            '2021-01', '2021-04', '2021-07', '2021-10',
            '2022-01', '2022-04', '2022-07'])
ax.yaxis.set_major_formatter(ticks_y)
sns.despine()

# Save the plot.
fig.savefig('Changes in Time Between Booking and Appointment Over Time.jpg')


# We can see that for the categories where the time between booking and appointment is less, the number of appointments see more dramatic increases and decreases.
#    - This may be due to the constant changing nature of the COVID-19 pandemic, with regards to how severe people may view their health issues in relation to the virus.
#    
# - Was appointment attendance affected by the time between booking and appointment?

# ### <div align="center"> Display the proportion of appointment status in relation to the time between booking and appointment.

# In[94]:


# Create a subset of the ar DataFrame, aggregating the
# time_between_book_and_appointment and count_of_appointments.
ar_book_2 = ar.groupby(['time_between_book_and_appointment',
                        'appointment_status'])\
                       ['count_of_appointments'].agg('sum').reset_index()


# In[95]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Create a bar plot.
sns.barplot(x = 'time_between_book_and_appointment',
            y = 'count_of_appointments', hue = 'appointment_status',
            order = my_order, palette = 'colorblind',
            data = ar_book_2)

# Format figure attributes.
plt.title('Appointments for each Booking Wait Time Period',
          fontsize = 25)
plt.xlabel('Time Between Booking and Appointment', fontsize = 20)
plt.ylabel('Number of Appointments (millions)', fontsize = 20)
plt.legend(title = 'Appointment Status', fontsize = 15,
           loc = 'right', borderaxespad = 0)
plt.xticks(rotation = 30)
ax.yaxis.set_major_formatter(ticks_y)
sns.despine()


# There doesn't appear to be any significant trends with regards to appointment status and the time between booking and appointment.

# ### <div align="center"> What is the distribution of appointments between the appointment status categories?

# In[96]:


# Create a subset of the ar DataFrame, aggregating the
# appointment status with count of appointments.
ar_status = ar.groupby('appointment_status')            ['count_of_appointments'].agg('sum').reset_index()

# Sort the subset DataFrame to see the highest number of appointments.
ar_status.sort_values(by = 'count_of_appointments', ascending = False)


# There are more appointment statuses recorded as **Unknown** than **DNA (Did Not Attend)**.
# - Why is this?
#     - Could it be due to poor data collection? Was data collection only poor during the months recorded in these datasets?
#         - Perhaps analysing data of this nature from preceding and succeeding months could answer this question.

# In[97]:


# Create a subset of the ar DataFrame using
# appointment_month and appointment_status.
ar_month_stat = ar.groupby(['appointment_month', 'appointment_status'])                        ['count_of_appointments'].agg('sum').reset_index()


# In[98]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Create a line plot.
sns.lineplot(x = 'appointment_month', y = 'count_of_appointments',
            hue = 'appointment_status', ci = None,
            palette = 'colorblind',
            data = ar_month_stat)

# Format figure attributes.
plt.title('Appointment Status Over Time',
          fontsize = 25)
plt.xlabel('Appointment Month', fontsize = 20)
plt.ylabel('Number of Appointments (millions)', fontsize = 20)
plt.legend(title = 'Appointment Status', fontsize = 15,
           bbox_to_anchor = (1, .5), loc = 'upper left',
           borderaxespad = 0)
plt.xticks(rotation = 45)
ax.yaxis.set_major_formatter(ticks_y)
sns.despine()


# There is a higher proportion of **DNA** and **Unknown** in **September** and **October** in both **2020** and **2021**.
#    - These are the busier months for the NHS.
#        - Could this trend be due to appointment cancellations or reschedules?
#    
# There is a significant spike in the **Unknown** category in **March 2020**.
#    - This lack of record documentation could be due to the NHS being under significant pressure during March 2020 with the outbreak of COVID-19 in the UK and thee newly-introduced lockdown.

# # <div align="center"> Twitter data

# In[99]:


# Set the maximum column width to display.
pd.options.display.max_colwidth = 200


# In[100]:


# View the tweets DataFrame.
tweets.head()


# In[101]:


# Explore the overview of the DataFrame.
print(tweets.info())

# View descriptive statistics of retweets and favourites.
tweets.describe()


# In[102]:


# Assess the value counts for how many times tweets were retweeted.
tweets.value_counts('tweet_retweet_count', ascending = False)


# In[103]:


# Assess the value counts for how many times tweets were favourited.
tweets.value_counts('tweet_favorite_count', ascending = False)


# **Retweet** is a more utilised feature of twitter than **Favourite** and these statistics show that to be true.
#    - While it is certainly worth looking at them both, the **retweet** column would perhaps provide more insight.

# In[104]:


# Order the DataFrame by retweet counts.
tweets_re = tweets.sort_values(['tweet_retweet_count'], ascending = False)

tweets_re


# Looking at **tweets_re** we can immediately see what looks like duplicate tweets. Therefore I decided to investigate to determine if there are in fact absolute duplicates using the **tweet_full_text** and **tweet_id** columns.

# In[105]:


# Create a new DataFrame and use the .duplicated() function to find duplicates.
tweets_duplicated = tweets[tweets['tweet_full_text'].duplicated()]

tweets_duplicated.shape


# In[106]:


# Create a new DataFrame and use the .duplicated() function to find duplicates.
tweets_duplicated_id = tweets[tweets['tweet_id'].duplicated()]

tweets_duplicated_id.shape


# Even though the second code snippet reveals there to be no duplicates for **tweet_id**, tweet IDs are not unique identifiers in the sense that each belongs to a unique account or individual.
# 
# Tweet IDs incorporate a time-stamp digit sequence and, therefore, it may still be assumed that there are duplicates in the Data Set.
#    - [Twitter IDs](https://developer.twitter.com/en/docs/twitter-ids#:~:text=Today%2C%20Twitter%20IDs%20are%20unique,number%2C%20and%20a%20sequence%20number.)

# #### Remove Duplicates

# In[107]:


# Before removing duplicates, check that the 'tweet_full_text' column
# does not have any mixed data types that could prevent .drop_duplicates()
# from working.
def check_obj_columns(dfx):
    tdf = tweets.select_dtypes(include = ['object']).applymap(type)
    for col in tdf:
        if len(set(tdf[col].values)) > 1:
            print("Column '{}' has mixed object types.".format(col))

# Check for mixed data types in the DataFrame.
check_obj_columns(tweets)


# In[108]:


# Drop the duplicates.
                      # subset = tells Python to look specifically in the tweet_full_text column.
                                                                  # inplace = True tells Python to apply the
                                                                  # duplicate drop to the original DataFrame.
tweets.drop_duplicates(subset = 'tweet_full_text', keep = 'first', inplace = True)


# In[109]:


# Check that the duplicates have been dropped.
tweets_duplicated = tweets[tweets['tweet_full_text'].duplicated()]

tweets_duplicated.shape


# In[110]:


# Order the amended DataFrame by retweet counts.
tweets_re = tweets.sort_values(['tweet_retweet_count'], ascending = False)

tweets_re


# In[111]:


# Order the amended DataFrame by favourite counts.
tweets_fav = tweets.sort_values(['tweet_favorite_count'], ascending = False)

tweets_fav


# In[112]:


# Create a new DataFrame with only text values.
tweets_text = tweets['tweet_full_text']

tweets_text.head()


# In[113]:


# Create variable with an empty list.
tags = []

# Use a for loop and specify the iterator_variable and the sequence.
for y in [x.split(' ') for x in tweets['tweet_full_text'].values]:
    for z in y:
        if '#' in z:
            # Change to lowercase.
            tags.append(z.lower())

# Create a Pandas Series to count the values in the list.
# Set the Series equal to tags.
tweets_text = pd.Series(tags)

# View the hashtags list.
tags


# In[114]:


# Count the values in the list.
hashtags_c = tweets_text.value_counts(normalize = False, sort = True,
                         ascending = False, bins = None, dropna = True)

# Show the first 30 rows.
hashtags_c.head(30)


# ## <div align="center"> Identify the top trending hashtags with a visualisation

# In[115]:


# Create a DataFrame with the hashtags_c data.
hashtags = pd.DataFrame(hashtags_c).reset_index()

# View the DataFrame.
hashtags


# In[116]:


# Rename the columns to word and count.
hashtags.columns = ['word', 'count']

# View the updated DataFrame.
print(hashtags.dtypes)
hashtags


# #### Sense-Check

# In[117]:


# Check the DataFrame for missing values
hashtags.isnull().sum()


# ### Barplot the Hashtags

# In[118]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Set figure size.
sns.set(rc = {'figure.figsize':(16, 10)})

# Create a bar plot.
sns.barplot(x = 'word', y = 'count',
            palette = 'colorblind',
            data = hashtags[hashtags['count'] > 20])

# Format figure attributes.
plt.title('The Top Trending Twitter Hashtags', fontsize = 25)
plt.xlabel('Hashtag Word', fontsize = 20)
plt.ylabel('Count', fontsize = 20)
plt.xticks(rotation = 45)
sns.despine()
sns.set_style('white')


# Although this chart clearly signifies that **#healthcare** is the most used hashtag, it would be beneficial to view the same chart excluding this particular hashtag so as to see how the other top hashtags fair more clearly.

# In[119]:


# Create a new DataFrame excluding the #healthcare hashtag.
hashtags_new = hashtags[-(hashtags['word'] == '#healthcare')]


# In[120]:


# Define figure.
fig, ax = plt.subplots(dpi = 150)

# Set figure size.
sns.set(rc = {'figure.figsize':(16, 10)})

# Create a bar plot.
sns.barplot(x = 'word', y = 'count',
            palette = 'colorblind',
            data = hashtags_new[hashtags_new['count'] > 20])
                            
# Format figure attributes.
plt.title('Top Trending Twitter Hashtags', fontsize = 25)
plt.xlabel('Hashtag', fontsize = 20)
plt.ylabel('Count', fontsize = 20)
plt.xticks(rotation = 60)
sns.despine()
sns.set_style('white')


# # <div align="center"> Summary of Findings

# - The run-up to Christmas 2021 (**October - December**) and **March 2022** show to be the busiest periods for the NHS within the data provided.
# 
# 
# - The locations with the highest number of appointments were:
#    - **North West London** (n = 12142390)
#    - **North East London** (n = 9588891)
#    - **Kent and Medway** (n = 9286167)
#    
#    
# - Throughout the datasets, most appointments occurred within:
#    - The Service Setting of **General Practice**
#    - The Context Type of **Care Related Encounter**
#    - The National Category of **General Consultation Routine**
#    
#    
# - The most utilised Healthcare Professional Type was **GP**.
#    
#    
# - **Face-to-Face** appointments were favoured by patients for the most part, although during lockdowns, **Telephone** appointments rose signnificantly.
# 
# 
# - Appointments with a shorter time between booking and the appointment saw greater fluctuation, particularly during busy periods.
# 
# 
# - The change in resource allocation over time seemed to be influenced somewhat by the severity of Covid-19 in the UK and whether government-imposed lockdowns were in place.
#    - I have included a link to a graphic detailing the UK's timeline during the peak of the Covid-19 pandemic which may be helpful to reference alongside looking at thee findings.
#        - [UK Covid Timeline](https://www.instituteforgovernment.org.uk/sites/default/files/timeline-lockdown-web.pdf)
# 
# 
# - I did not find sufficient data to accurately determine staff levels within the NHS and whether they were adequate.
