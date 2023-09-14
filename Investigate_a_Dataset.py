#!/usr/bin/env python
# coding: utf-8

# # Project: Investigate a Dataset - [noshowappointments-kagglev2-may-2016.csv] 
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# This dataset collects information
# from 100k medical appointments in
# Brazil and is focused on the question
# of whether or not patients show up
# for their appointment. A number of
# characteristics about the patient are
# included in each row.
# 
# ### Dataset Description 
# we Have a  file contains the data we are going to analyze
# 
# ### Question(s) for Analysis
# What factors are
# important for us to
# know in order to
# predict if a patient will
# show up for their
# scheduled
# appointment?

# In[3]:


#import statmentes for all of the packeges that we plan to use 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#Rember to include a 'Magic word' so that your visualzation are plotted
#inline with the notebook.see this page for more:
#http://ipython.readhedocs.io/en/stuble/interactive/magic.html
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


# Upgrade pandas to use dataframe.explode() function. 
get_ipython().system('pip install --upgrade pandas==0.25.0')


# <a id='wrangling'></a>
# ## Data Wrangling
#  In this section of the report, you will load in the data, check for cleanliness, and then trim and clean your dataset for analysis.
# 
# ### General Properties
# 

# In[19]:


import pandas as pd

# Load your data from 'noshowappointments-kagglev2-may-2016.csv' and print out the first few rows
df = pd.read_csv('noshowappointments-kagglev2-may-2016.csv')
df.head()


# In[20]:


#exploring the data shape
df.shape


# The data have 110527rows and 14 columns

# In[21]:


#check foe duplication
df.duplicated().sum()


# There is 0 duplication

# In[22]:


# Check the number of unique values in the id  
df['PatientId'].nunique()


# There is 62299 is unique values 

# In[23]:


#check for duplications id 
df['PatientId'].duplicated().sum()


# There is 48228 duplicated PatientId

# ### Data Cleaning

# In[24]:


#getting some information about your data
df.describe()


# In[25]:


#identify the row index -1 for the Age 
mask=df.query('Age=="-1"')
mask


# In[26]:


#remove the -1 value 
df.drop(index=99832)


# In[20]:


# inspection for missing values
df.info()


# In[ ]:


No missing values


# In[53]:


#correction the coulmens name
df.rename(columns={'Hipertension': 'Hypertension'})
df.rename(columns={'No-show': 'No_show'})


# In[43]:


df.drop_duplicates(subset=['PatientId', 'No-show'])
df.shape


# In[49]:


# removing unnecessary data
df.drop(['PatientId','AppointmentID','ScheduledDay','AppointmentDay'], axis=1, inplace=True)
df.head()


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# > Now that you've prepared and refined your dataset, it's time to delve into exploration. Begin by calculating statistical measures and crafting graphical representations, all aimed at addressing the research inquiries you introduced in the initial section of your analysis
# 
# 
# 
# 
# 
# ### Analysis

# In[42]:


#histogram of whole data
df.hist(figsize=(15,12)),


# In[44]:


# Assigning name of show and no show facilitate recall 
# DataFrame for 'No' and 'Yes' in the 'No-show' column
show = df['No-show'] == 'No'
noshow = df['No-show'] == 'Yes'
df[show].count(),df[noshow].count()


# The No show  is  88208 biger than no-show  22319

# ### Analysing 

# In[68]:


import matplotlib.pyplot as plt  # Import the matplotlib library
# compare those who showed to those who didnot according to Gender

plt.figure(figsize=(14, 6))
df.Gender[show].hist(alpha=0.5,color='blue',label='show')
df.Gender[noshow].hist(alpha=0.5,color='brown',label='noshow')
plt.legend();
plt.title('compare those who showed to those who didnot according to Gender')
plt.xlabel('Gender')
plt.ylabel('patients number')


# In[69]:


# compare those who showed to those who didnot according to Gender

print(df.Gender[show].value_counts())
print(df.Gender[noshow].value_counts())


# Gender is negligible famale are more than meale

# In[80]:


import matplotlib.pyplot as plt  # Import the matplotlib library
# compare those who showed to those who didnot according to enrollment in the Brasilan Welfare program

plt.figure(figsize=(16, 8))
df.Gender[show].hist(alpha=0.5,color='green',label='show')
df.Gender[noshow].hist(alpha=0.5,color='red',label='noshow')
plt.legend();
plt.title(' compare those who showed to those who didnot according to enrollment in the Brasilan welfare program')
plt.xlabel('Welfare')
plt.ylabel('patients number')


# In[81]:


#compare those who showed to those who didnot according to gender
print(df.Scholarship[show].value_counts())
print(df.Scholarship[noshow].value_counts())


#   enrollment in the Brasilan welfare program is negligible

# In[84]:


import matplotlib.pyplot as plt  # Import the matplotlib library
#compare those who showed to those who didnot according to Hypertension

plt.figure(figsize=(16, 8))
df.Hipertension[show].hist(alpha=0.5,color='blue',label='show')
df.Hipertension[noshow].hist(alpha=0.5,color='yellow',label='noshow')
plt.legend();
plt.title(' compare those who showed to those who didnot according to Hipertension')
plt.xlabel('Hipertension')
plt.ylabel('patients number')


#  Hypertension is negligible

# In[85]:


import matplotlib.pyplot as plt  # Import the matplotlib library
#compare those who showed to those who didnot according to Diabetes

plt.figure(figsize=(16, 8))
df.Diabetes[show].hist(alpha=0.5,color='pink',label='show')
df.Diabetes[noshow].hist(alpha=0.5,color='black',label='noshow')
plt.legend();
plt.title(' compare those who showed to those who didnot according to Diabetes')
plt.xlabel('Diabetes')
plt.ylabel('patients number')


# Diabetes is negligible

# In[86]:


import matplotlib.pyplot as plt  # Import the matplotlib library
#compare those who showed to those who didnot according to Alcoholism

plt.figure(figsize=(16, 8))
df.Alcoholism[show].hist(alpha=0.5,color='red',label='show')
df.Alcoholism[noshow].hist(alpha=0.5,color='orange',label='noshow')
plt.legend();
plt.title(' compare those who showed to those who didnot according to Alcoholism')
plt.xlabel('Alcoholism')
plt.ylabel('patients number')


# Alcoholism is negligible

# In[88]:


import matplotlib.pyplot as plt  # Import the matplotlib library
#compare those who showed to those who didnot according to Handcap

plt.figure(figsize=(16, 8))
df.Handcap[show].hist(alpha=0.5,color='green',label='show')
df.Handcap[noshow].hist(alpha=0.5,color='black',label='noshow')
plt.legend();
plt.title(' compare those who showed to those who didnot according to Handcap')
plt.xlabel('Handcap')
plt.ylabel('patients number')


# Handcap is negligible

# In[90]:


import matplotlib.pyplot as plt  # Import the matplotlib library
#compare those who showed to those who didnot according to SMS_received

plt.figure(figsize=(16, 8))
df.SMS_received[show].hist(alpha=0.5,color='blue',label='show')
df.SMS_received[noshow].hist(alpha=0.5,color='yellow',label='noshow')
plt.legend();
plt.title(' compare those who showed to those who didnot according to SMS_received')
plt.xlabel('SMS_received')
plt.ylabel('patients number')


# In[94]:


import matplotlib.pyplot as plt  # Import the matplotlib library
#compare those who showed to those who didnot according to Neighbourhood

plt.figure(figsize=(16, 8))
df.Neighbourhood[show].value_counts().plot(kind='bar',alpha=0.5,color='black',label='show')
df.Neighbourhood[noshow].value_counts().plot(kind='bar',alpha=0.5,color='yellow',label='noshow')
plt.legend();
plt.title(' compare those who showed to those who didnot according to Neighbourhood')
plt.xlabel('Neighbourhood')
plt.ylabel('patients number')


# In[ ]:


import matplotlib.pyplot as plt  # Import the matplotlib library
#compare those who showed to those who didnot according to SMS_received

plt.figure(figsize=(16, 8))
df.SMS_received[show].hist(alpha=0.5,color='blue',label='show')
df.SMS_received[noshow].hist(alpha=0.5,color='yellow',label='noshow')
plt.legend();
plt.title(' compare those who showed to those who didnot according to SMS_received')
plt.xlabel('SMS_received')
plt.ylabel('patients number')


# I can assert that there is a significant correlation between the patients' choice of neighborhood and their attendance at the clinic.

# In[92]:


import matplotlib.pyplot as plt  # Import the matplotlib library
#compare those who showed to those who didnot according to Age
plt.figure(figsize=(16, 8))
df.Age[show].hist(alpha=0.5,color='red',label='show')
df.Age[noshow].hist(alpha=0.5,color='pink',label='noshow')
plt.legend();
plt.title(' compare those who showed to those who didnot according to Age')
plt.xlabel('Age')
plt.ylabel('patients number')


# 
# "Patients between the ages of 0 to 10 exhibited a higher appointment rate compared to all other age groups. Appointment rates tend to decrease as patients grow older.

# <a id='conclusions'></a>
# ## Conclusions
# n conclusion, it is evident that the neighborhood plays a significant role in patients showing up at the clinic. Age also plays a crucial role, with the 0-10 age group showing the highest attendance, followed by the 35-70 age group. Surprisingly, a larger number of patients attended appointments without receiving an SMS reminder.These findings highlight the complex interplay of factors affecting patient attendance and suggest that more research is needed to explore the nuances of this relationship.
# 
# ## Submitting your Project 
# 
# > **Tip**: Before you submit your project, you need to create a .html or .pdf version of this notebook in the workspace here. To do that, run the code cell below. If it worked correctly, you should get a return code of 0, and you should see the generated .html file in the workspace directory (click on the orange Jupyter icon in the upper left).
# 
# > **Tip**: Alternatively, you can download this report as .html via the **File** > **Download as** submenu, and then manually upload it into the workspace directory by clicking on the orange Jupyter icon in the upper left, then using the Upload button.
# 
# > **Tip**: Once you've done this, you can submit your project by clicking on the "Submit Project" button in the lower right here. This will create and submit a zip file with this .ipynb doc and the .html or .pdf version you created. Congratulations!

# In[1]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])


# In[ ]:




