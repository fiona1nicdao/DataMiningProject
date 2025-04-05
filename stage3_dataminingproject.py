# -*- coding: utf-8 -*-
"""Stage3_DataMiningProject.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_Juz-5R0GFC4k8vTD6K7qL3OjgmJkeyl
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import cm

"""# Loading datasets and preprocessing"""

# prompt: import Sleep_Efficiency.csv as a df
# used AI to help import csv files on google colab

url_eff = 'https://raw.githubusercontent.com/fiona1nicdao/DataMiningProject/refs/heads/main/Sleep_Efficiency.csv'
df_eff = pd.read_csv(url_eff)
# df_eff = pd.read_csv('/content/Sleep_Efficiency.csv')
# print(df_eff.head(5))

url_health = 'https://raw.githubusercontent.com/fiona1nicdao/DataMiningProject/refs/heads/main/Sleep_health_and_lifestyle_dataset.csv'
df_health = pd.read_csv(url_health)
# df_health = pd.read_csv('/content/Sleep_health_and_lifestyle_dataset.csv')
# print(df_health.head(5))

url_cycle = 'https://raw.githubusercontent.com/fiona1nicdao/DataMiningProject/refs/heads/main/sleep_cycle_productivity.csv'
df_cycle = pd.read_csv(url_cycle)
# df_cycle = pd.read_csv('/content/sleep_cycle_productivity.csv')
# print(df_cycle.head(5))

url_depr = 'https://raw.githubusercontent.com/fiona1nicdao/DataMiningProject/refs/heads/main/sleep_deprivation_dataset_detailed.csv'
df_depr = pd.read_csv(url_depr)
# df_depr = pd.read_csv('/content/sleep_deprivation_dataset_detailed.csv')
# print(df_depr.head(5))

"""## Removing underage "samples"
"""

#remove underage items from sleep efficiency dataset
index_drop_under18 = df_eff[df_eff['Age'] < 18 ].index
df_eff = df_eff.drop(index_drop_under18)
# print(df_eff.head(10))

#drop null values from all data sets
df_eff = df_eff.dropna()
df_health = df_health.dropna()
df_cycle = df_cycle.dropna()
df_depr = df_depr.dropna()

"""## Dataset Shape Analysis
Count of number items (people) in each dataset (the number of rows)

Findings: Sleep cycle dataset is largest, with 5000 samples
"""

# Sleep_Efficiency.csv
print(df_eff.shape)
# Sleep_health_and_lifestyle_dataset.csv'
print(df_health.shape)
# sleep_cycle_productivity.csv
print(df_cycle.shape)
# sleep_deprivation_dataset_detailed.csv
print(df_depr.shape)

#before dropping null values sizes of datasets:
# (443, 15)
# (374, 13)
# (5000, 15)
# (60, 14)

"""# Creating combined dataset with all four datasets"""

# make a dataframe that combines all the ages
age1 = df_eff['Age'].tolist()
age2 = df_health['Age'].tolist()
age3 = df_cycle['Age'].tolist()
age4 = df_depr['Age'].tolist()
data = age1 + age2 + age3 + age4
data = {'Age':data}
df_age = pd.DataFrame(data)
print(len(df_age))
# print(df_age)

# add gender to all the df_age
gender1 = df_eff['Gender'].tolist()
gender2 = df_health['Gender'].tolist()
gender3 = df_cycle['Gender'].tolist()
gender4 = df_depr['Gender'].tolist()
data = gender1 + gender2 + gender3 + gender4
df_age['Gender'] = data
# print(df_age.columns)
print(df_age)

# add sleep duration
duration1 = df_eff['Sleep duration'].tolist()
duration2 = df_health['Sleep Duration'].tolist()
duration3 = df_cycle['Total Sleep Hours'].tolist()
duration4 = df_depr['Sleep_Hours'].tolist()
data = duration1 + duration2 + duration3 + duration4
df_age['Sleep Duration'] = data
print(df_age.columns)
print(df_age)

"""## Creating Age Group Attribute"""

# make a column for age groups
# 0 = 18-24
# 1 = 25-35
# 2 = 36-44
# 3 = 45-55
# 4 = 56-64
# 5 = 65 - 100
age_groups = []
for i in range(len(df_age)):
  if df_age['Age'][i] >= 18 and df_age['Age'][i] <= 24:
    age_groups.append(0)
  elif df_age['Age'][i] >= 25 and df_age['Age'][i] <= 35:
    age_groups.append(1)
  elif df_age['Age'][i] >= 36 and df_age['Age'][i] <= 44:
   age_groups.append(2)
  elif df_age['Age'][i] >= 45 and df_age['Age'][i] <= 55:
   age_groups.append(3)
  elif  df_age['Age'][i] >= 56 and df_age['Age'][i] <= 64:
   age_groups.append(4)
  else:
   age_groups.append(5)

#new column : Age Group
df_age['Age Group'] = age_groups
print(df_age)
# print(len(age_groups))

"""# Analysis of Combined Data Frame df_age

## Histogram of Age Distribution for combined data frame df_age
"""

#histogram of age distribution
# 18 -24 : young adults
# 25-35 : adults
# 36 -44 : mid-age adults
# 45 -55 : older adults
# 56-65 : even older adults
# 65 - 100 : adults older than 65
my_bins = [18,25,35,45,55,65,100]
# change to the common demographics ?
#  https://www.snapsurveys.com/blog/5-survey-demographic-question-examples/

n, _, patches = plt.hist(df_age['Age'], bins=my_bins,edgecolor = 'white',color='skyblue')
plt.bar_label(patches)
plt.xlabel('Age')
plt.ylabel('count')
plt.title('Count the Age distribution of all Datasets')
plt.show()

"""## Histograms of Age and Gender distribution from each dataset"""

my_bins = [18,25,35,45,55,65,100]
fig, axs = plt.subplots(figsize=(30,10), ncols=4);
# Sleep_Efficiency.csv
axs[0].hist(df_eff['Age'], bins=my_bins, edgecolor = 'white',color='skyblue')
axs[0].bar_label(axs[0].containers[0], label_type='edge')
axs[0].set(
  xlabel='Age',
  ylabel='count',
  title=' Sleep_Efficiency Dataset'
)

# Sleep_health_and_lifestyle_dataset.csv
axs[1].hist(df_health['Age'], bins=my_bins,edgecolor = 'white',color='skyblue')
axs[1].bar_label(axs[1].containers[0], label_type='edge')
axs[1].set(
  xlabel='Age',
  ylabel='count',
  title=' Sleep_health_and_lifestyle '
)

# sleep_cycle_productivity.csv
axs[2].hist(df_cycle['Age'], bins=my_bins,edgecolor = 'white',color='skyblue')
axs[2].bar_label(axs[2].containers[0], label_type='edge')
axs[2].set(
  xlabel='Age',
  ylabel='count',
  title='sleep_cycle_productivity '
)

# sleep_deprivation_dataset_detailed.csv
axs[3].hist(df_depr['Age'], bins=my_bins,edgecolor = 'white',color='skyblue')
axs[3].bar_label(axs[3].containers[0], label_type='edge')
axs[3].set(
  xlabel='Age',
  ylabel='count',
  title='sleep_deprivation_dataset_detailed'
)
# plt.show()

"""## Histogram of gender distribution for combined data frame df_age"""

# histogram of gender distribution

df_age.Gender.value_counts().plot(kind='bar')
ax = plt.gca()
container = ax.containers[0]
plt.bar_label(container, label_type='edge')
# add counts label for each bar
plt.xlabel('Gender')
plt.ylabel('count')
plt.title('Count the Gender distribution of all Datasets')
plt.xticks(rotation=0)
plt.show()

"""## Histogram of gender distribution for each dataset"""

# histogram of gender distribution for each dataset
fig, axs = plt.subplots(figsize=(30,10), ncols=4);
# Sleep_Efficiency.csv
gender_counts = df_eff.Gender.value_counts()
axs[0].bar(gender_counts.index, gender_counts.values)
axs[0].bar_label(axs[0].containers[0], label_type='edge')
axs[0].set(
  xlabel='gender',
  ylabel='count',
  title=' Sleep_Efficiency Dataset'
)
# Sleep_health_and_lifestyle_dataset.csv
gender_counts_health = df_health.Gender.value_counts()
axs[1].bar(gender_counts_health.index, gender_counts_health.values)
axs[1].bar_label(axs[1].containers[0], label_type='edge')
axs[1].set(
  xlabel='gender',
  ylabel='count',
  title=' Sleep_health_and_lifestyle Dataset'
)
# sleep_cycle_productivity.csv
gender_counts_cycle = df_cycle.Gender.value_counts()
axs[2].bar(gender_counts_cycle.index, gender_counts_cycle.values)
axs[2].bar_label(axs[2].containers[0], label_type='edge')
axs[2].set(
  xlabel='gender',
  ylabel='count',
  title='sleep_cycle_productivity Dataset'
)
# sleep_deprivation_dataset_detailed.csv
gender_counts_depr = df_depr.Gender.value_counts()
axs[3].bar(gender_counts_depr.index, gender_counts_depr.values)
axs[3].bar_label(axs[3].containers[0], label_type='edge')
axs[3].set(
  xlabel='gender',
  ylabel='count',
  title='sleep_deprivation_dataset_detailed Dataset'
)

"""## Histogram of sleep for each age group"""

# histogram of sleep for each age group
sns.boxplot(data=df_age, x='Sleep Duration', hue='Age Group')
plt.xlabel('Sleep Duration)')
# plt.ylabel('Sleep Duration (Hours)')
plt.title('Distribution of Sleep Duration ')
plt.legend(['18-24','25-35','36 -44','45 -55','56-65','65 - 100'], title='Age Group',loc='upper left', bbox_to_anchor=(1, 1));
plt.show()

"""# Dataset : Sleep Cycle Productivity
used this one because 5000 people in this dataset
"""

# make a column for age groups
# 0 = 18-24
# 1 = 25-35
# 2 = 36-44
# 3 = 45-55
# 4 = 56-64
# 5 = 65 - 100
age_groups = []
for i in range(len(df_cycle)):
  if df_age['Age'][i] >= 18 and df_age['Age'][i] <= 24:
    age_groups.append(0)
  elif df_age['Age'][i] >= 25 and df_age['Age'][i] <= 35:
    age_groups.append(1)
  elif df_age['Age'][i] >= 36 and df_age['Age'][i] <= 44:
   age_groups.append(2)
  elif df_age['Age'][i] >= 45 and df_age['Age'][i] <= 55:
   age_groups.append(3)
  elif  df_age['Age'][i] >= 56 and df_age['Age'][i] <= 64:
   age_groups.append(4)
  else:
   age_groups.append(5)

#new column : Age Group
df_cycle['Age Group'] = age_groups
column_names = df_cycle.columns
# print(column_names)

# fig, axs = plt.subplots(figsize=(30,10), ncols=3);
# will fix to make it multiple plots

# Distribution of Sleep Duration for each Age Group
sns.boxplot(data=df_cycle, x='Total Sleep Hours', hue='Age Group')
plt.xlabel('Sleep Duration')
plt.ylabel('Age Group')
plt.title('Distribution of Sleep Duration ')
plt.legend(['18-24','25-35','36 -44','45 -55','56-65','65 - 100'], title='Age Group',loc='upper left', bbox_to_anchor=(1, 1));
plt.show()
# Distribution of Sleep Quality for each Age Group
sns.boxplot(data=df_cycle, x='Sleep Quality', hue='Age Group')
plt.xlabel('Sleep Quality')
plt.ylabel('Age Group')
plt.title('Distribution of Sleep Quality')
plt.legend(['18-24','25-35','36 -44','45 -55','56-65','65 - 100'], title='Age Group',loc='upper left', bbox_to_anchor=(1, 1));
plt.show()
# Distribution of Exercise  for each Age Group
sns.boxplot(data=df_cycle, x='Exercise (mins/day)', hue='Age Group')
plt.xlabel('Exercise (mins/day)')
plt.ylabel('Age Group')
plt.title('Distribution of Exercise (mins/day)')
plt.legend(['18-24','25-35','36 -44','45 -55','56-65','65 - 100'], title='Age Group',loc='upper left', bbox_to_anchor=(1, 1));
plt.show()
# Distribution of Productivity for each Age Group
sns.boxplot(data=df_cycle, x='Productivity Score', hue='Age Group')
plt.xlabel('Productivity Score')
plt.ylabel('Age Group')
plt.title('Distribution of Productivity Score')
plt.legend(['18-24','25-35','36 -44','45 -55','56-65','65 - 100'], title='Age Group',loc='upper left', bbox_to_anchor=(1, 1));
plt.show()

"""# Caffeine Dataset"""

display(df_eff.head(3))
display(df_cycle.head(3))

#caffeine dataset: sleep efficiency, sleep cycle

#merge age, gender, sleep hours
age1 = df_eff['Age'].tolist()
age3 = df_cycle['Age'].tolist()

caffeine_data = age1 + age3
caffeine_data = {'Age':caffeine_data}
df_caffeine = pd.DataFrame(caffeine_data)

print(len(df_caffeine))
# print(df_caffeine)

# add gender to all the df_age
gender1 = df_eff['Gender'].tolist()
gender3 = df_cycle['Gender'].tolist()

caffeine_data = gender1 + gender3
df_caffeine['Gender'] = caffeine_data

#convert categorical gender to numeric
df_caffeine['Gender'] = df_caffeine['Gender'].map({'Female':0, 'Male':1})
# print(df_caffeine)

# add sleep duration
duration1 = df_eff['Sleep duration'].tolist()
duration3 = df_cycle['Total Sleep Hours'].tolist()
caffeine_data = duration1 + duration3
df_caffeine['Sleep Duration'] = caffeine_data

#add caffeine intake column
caffeine1 = df_eff['Caffeine consumption'].tolist()
caffeine2 = df_cycle['Caffeine Intake (mg)'].tolist()
caffeine_data = caffeine1 + caffeine2
df_caffeine['Caffeine'] = caffeine_data

df_caffeine.dropna(inplace=True)

print(df_caffeine.columns)
print(df_caffeine)

#scatterplot for How Caffeine Consumption impacts Sleep Duration by Gender
#Very unclear and hard to extract info bc theres way too many data points

sns.scatterplot(data=df_caffeine, x='Caffeine', y='Sleep Duration', hue='Gender')
plt.xlabel('Caffeine Consumption (mg)')
plt.ylabel('Sleep Duration (Hours)')
plt.title('Caffeine Consumption vs. Sleep Duration')
plt.show()

#just for females ages 18-25
df_youngfemale = df_caffeine[(df_caffeine['Gender'] == 0.0 ) & (df_caffeine['Age'] >= 18) & (df_caffeine['Age'] <= 25)]
#drop null values
df_youngfemale = df_youngfemale.dropna()
# print(df_youngfemale)

sns.scatterplot(data=df_youngfemale, x='Caffeine', y='Sleep Duration')
plt.xlabel('Caffeine Consumption (mg)')
plt.ylabel('Sleep Duration (Hours)')
plt.title('Caffeine Consumption vs. Sleep Duration')
plt.show()

#Box plot for Caffeine Consumption by Gender

sns.boxplot(data=df_caffeine, x='Caffeine', hue='Gender')
plt.xlabel('Caffeine Consumption (mg)')
plt.title('Caffeine Consumption by Gender')
plt.show()

#Box plot for Caffeine Consumption by Gender
sns.boxplot(data=df_caffeine, x='Sleep Duration', hue='Gender')
plt.ylabel('Sleep Duration (Hours)')
plt.title('Sleep Duration by Gender')
plt.show()

"""Conclusion: Gender is not a good separator for caffeine and sleep duration

# Occupation and Sleep Duration
"""

#Top 5 occupations from Sleep Health and Lifestyle Dataset

top_5_occupations = df_health['Occupation'].value_counts().head(5)
print(top_5_occupations)
print()

#total occupation counts
occupation_counts = df_health['Occupation'].value_counts()
top_5_occupations = occupation_counts.head(5)
print(occupation_counts)

#graph the sleep duration of the top 5 occupations
top_occupations = df_health['Occupation'].value_counts().head(5).index.tolist()

#Filter data
df_top_occupations = df_health[df_health['Occupation'].isin(top_occupations)]

#Create bar plot of average sleep duration
avg_sleep = df_top_occupations.groupby('Occupation')['Sleep Duration'].mean().sort_values(ascending=False)

sns.barplot(x=avg_sleep.index, y=avg_sleep.values, palette='pastel')

plt.title('Average Sleep Duration by Top 5 Occupations')
plt.ylabel('Average Sleep Duration (Hours)')
plt.xlabel('Occupation')
plt.show()

#boxplot for top 5 occupations and sleep duration

sns.boxplot(data=df_top_occupations, x='Occupation', y='Sleep Duration', palette='pastel')
sns.stripplot(data=df_top_occupations, x='Occupation', y='Sleep Duration', color='black', alpha=0.3)

plt.title('Sleep Duration by Top 5 Occupations')
plt.ylabel('Sleep Duration (Hours)')
plt.xlabel('Occupation')

plt.show()

"""Conclusions:



Within the top 5 occupations of: teacher, nurse, doctor, accountant, and salesperons

*   Salespersons and nurses experience the least sleep duration based on median sleep duration
*   Following that, teachers and accountants, and then doctors have the highest median of sleep duration
*   Nurses have the highest range of sleep duration, from ~6.2 hours - ~8.1 hours

# Exploring relationships between BMI Category, Sleep Duration, and Sleep Disorders
"""

#looking at df_health
display(df_health.head(5))

#list all the unique values from the columns Sleep Disorder and BMI Category in df_health
print(df_health['Sleep Disorder'].unique())
print(df_health['BMI Category'].unique())

#counting how many there are of each unique value
disorder_counts = df_health['Sleep Disorder'].value_counts()
print(disorder_counts)

print()
bmi_counts = df_health['BMI Category'].value_counts()
print(bmi_counts)

#dropping Normal Weight since it is repetitive and such a low count
df_health = df_health.drop(df_health[df_health['BMI Category'] == 'Normal Weight'].index)

#boxplot to display relationship between BMI Category and Sleep Duration
sns.boxplot(data=df_health, x='BMI Category', y='Sleep Duration', palette='pastel')
sns.stripplot(data=df_health, x='BMI Category', y='Sleep Duration', color='black', alpha=0.3)
plt.xlabel('BMI Category')
plt.ylabel('Sleep Duration (Hours)')
plt.title('Sleep Duration vs. BMI Category')
plt.show()

"""Conclusions:

*   Those with a normal BMI and obese BMI have similar medians for sleep duration, but those with normal BMIs have a much smaller range of about 7.3-7.6 hours. The range for sleep duration of obese BMI is about 6.0-7.4 hours of sleep.
*   For the overweight BMI, the median sleep duration for this group is 6.5, and the range is 6.4-6.6 hours of sleep. However, this group also has many outliers that indicate there are a few overweight people that get around 8 hours of sleep.


"""

#boxplot to display relationship between Sleep Disorder and Sleep Duration
sns.boxplot(data=df_health, x='Sleep Disorder', y='Sleep Duration', palette = 'pastel')
sns.stripplot(data=df_health, x='Sleep Disorder', y='Sleep Duration', color='black', alpha=0.3)
plt.xlabel('Sleep Disorder')
plt.ylabel('Sleep Duration (Hours)')
plt.title('Sleep Duration vs. Sleep Disorder')
plt.show()

"""Conclusion:

*   As expected, those with insomnia sleep much less than those with sleep apnea. The insomnia group's median sleep duration is 6.5, and the sleep duration ranges from 6.4-6.6 hours of sleep. There are many outliers with this group, however, with many people sleeping more than these values and many sleeping even less.
*   The sleep apnea group's median sleep duration is 6.9 hours, but the range is very large from 6.1-8.1 hours of sleep. So, it seems like sleep duration might be independent of sleep apnea.

# PCA
"""

from sklearn.decomposition import PCA

# change columns - delete date, person id, age
# one-hot encoding of gender
print(df_cycle.head(5))

#still working on this
# X = df_cycle.iloc[:, 1:-1]   # all the rows, all columns except the last one
# y = df_cycle.iloc[:, -1].astype(int)    # just the last column with class labels
# pca_X = PCA(n_components=2).fit_transform(X)

# fig, ax = plt.subplots(figsize=(12, 8));
# plot_mnist_scatter(data=pca_X, c=y, name='PCA');
# ax.set(
#     xlabel='PCA_1',
#     ylabel='PCA_2',
# );