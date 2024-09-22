#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Read the data set and importing the packages


# In[28]:


import pandas as py
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


data=py.read_excel('Case.xlsx')
data


# In[11]:


control=py.read_excel('Case.xlsx','Control')
control


# In[13]:


test=py.read_excel('Case.xlsx','Test ')
test


# In[14]:


control.info()


# In[15]:


test.info() 


# In[16]:


test.describe()


# In[17]:


control.describe()


# In[ ]:


#Q1---Can the CEO market this product across India that BlueBull is a height enhancer ?


# In[19]:


from scipy.stats import ttest_ind
t_stat,p_value = ttest_ind(test.iloc[:,8:],control.iloc[:,8:])
print('P_values',p_value,'\n')
print('T_stat',t_stat)


# In[20]:


significant_months = [i+1 for i, p in enumerate(p_value) if p < 0.05]

print("Significant Months (p < 0.05):", significant_months,'\n')

print('Null hypothesis (H0): There is no significant difference in height increase between BlueBull consumers and non-consumers.\n')
print('Alternative hypothesis (H1): BlueBull consumers have a significant increase in height compared to non-consumers.')


# In[ ]:


#Q2 In which states of India can the marketing be done by BlueBull based on the experiment?


# In[21]:


# Get the unique states from the dataset
states = test['State'].unique()

significant_states = []

# Perform t-test for each state
for state in states:
    test_group_state = test[test['State'] == state].iloc[:, 8:20]
    control_group_state = control[control['State'] == state].iloc[:, 8:20]
    
    t_statistic, p_value = ttest_ind(test_group_state.values.flatten(), control_group_state.values.flatten())
    
    if p_value < 0.05:  # Adjust the significance level as necessary
        significant_states.append(state)

print("States with Significant Height Growth (p < 0.05):",'\n', significant_states,'\n')

print('Null hypothesis (H0): There is no significant difference in height increase between BlueBull consumers and non-consumers.\n')
print('Alternative hypothesis (H1): BlueBull consumers have a significant increase in height compared to non-consumers.')


# In[ ]:


#Q3 Can the CEO market this product across gender and age groups


# In[23]:


# Get the unique gender values from the dataset
genders = test['Is Male?'].unique()

significant_gender_groups = []

# Perform t-test for each gender group
for gender in genders:
    test_group_gender = test[test['Is Male?'] == gender].iloc[:, 8:20]
    control_group_gender = control[control['Is Male?'] == gender].iloc[:, 8:20]

    t_statistic, p_value = ttest_ind(test_group_gender.values.flatten(), control_group_gender.values.flatten()) # flatten() used to return a copy of a given array in such a way that it is collapsed into one dimension.

    if p_value < 0.05:  # Adjust the significance level as necessary
        significant_gender_groups.append(gender)

print("Significant Gender Groups (p < 0.05):",significant_gender_groups,'\n')


print('Null hypothesis (H0): There is no significant difference in height increase between BlueBull consumers and non-consumers.\n')
print('Altern')


# In[ ]:


#Q3months is really a long time to conclude an experiment and is there a faster way to conclude the experiment for this marketing problem



# In[24]:


# Define the months for analysis
months = [3, 6, 9, 12]

significant_months = []

# Perform t-test for each month
for month in months:
    test_height = test['Month {}'.format(month)]
    control_height = control['Month {}'.format(month)]

    t_statistic, p_value = ttest_ind(test_height, control_height)

    if p_value < 0.05:  # Adjust the significance level as necessary
        significant_months.append(month)

print("Significant Months (p < 0.05):", significant_months,'\n')
print('Null hypothesis (H0): There is no significant difference in height increase between BlueBull consumers and non-consumers.\n')
print('Alternative hypothesis (H1): BlueBull consumers have a significant increase in height compared to non-consumers.')



# In[29]:


sns.boxenplot(control['HouseHold Income per month']) # To check the distribution  of data 


# In[25]:


# Calculate height growth for each income group
test_low_income = test[test['HouseHold Income per month'] < 20000]['Month 12']
test_medium_income = test[(test['HouseHold Income per month'] >= 20000) & (test['HouseHold Income per month'] < 50000)]['Month 12']
test_high_income = test[test['HouseHold Income per month'] >= 80000]['Month 12']
control_low_income = control[control['HouseHold Income per month'] < 20000]['Month 12']
control_medium_income = control[(control['HouseHold Income per month'] >= 20000) & (control['HouseHold Income per month'] < 50000)]['Month 12']
control_high_income = control[control['HouseHold Income per month'] >= 80000]['Month 12']

# Perform t-tests for low, medium, and high-income groups
tstat_low_income, pvalue_low_income = ttest_ind(test_low_income, control_low_income)
tstat_medium_income, pvalue_medium_income = ttest_ind(test_medium_income, control_medium_income)
tstat_high_income, pvalue_high_income = ttest_ind(test_high_income, control_high_income)

# Print the t-test results
print("Household Income Category:")
print("Low Income - p-value:", pvalue_low_income)
print("Medium Income - p-value:", pvalue_medium_income)
print("High Income - p-value:", pvalue_high_income)

#A p-value less than 0.05 indicates a significant difference in height growth between BlueBull consumers and non-consumers within that category, suggesting that BlueBull works as a height enhancer. in the low household icome categorey as they might habve not be abble to have proper nutrinet through food 


# In[ ]:


Conclusion

I would absolutely suggest bluebull work as height ehancer is low income house house hold category

I would suggest bluebull does not work as hieght ehancer as per residence categorey

i would suggest to reseach more on the meat conuming candidate |


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




