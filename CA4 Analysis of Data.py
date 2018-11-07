
# coding: utf-8

# In[2]:


#Import required libraries
import pandas as pd 
import matplotlib.pyplot as plt
import datetime as dt

# Read data from file 'filename.csv' 
data = pd.read_csv("CA4_changes.csv") 

# Preview the first 5 lines of the loaded data 
data.head()


# In[3]:


#Make data into data frame
dframe= pd.DataFrame(data)


# In[4]:


#Confirm type is now dataframe
print(type(dframe))


# In[5]:


#Check number of lines in dframe
dframe.index


# In[6]:


#Check Column names
dframe.columns


# In[7]:


#Shape indicates Columns by rows returned
dframe.shape


# In[8]:


#Learn the type of each Column
dframe.dtypes


# In[10]:


#One Author name was very long in the data. 
#I have renamed this so that it will graph better
dframe.author=dframe.author.replace({'/OU=Domain Control Validated/CN=svn.company.net':'Domain Control'})


# In[11]:


#Created a new variable called Author_Count. This will count the number of times each author has made a commit
Author_Count = dframe.author.value_counts()


# In[12]:


#Count for each commit
dframe.groupby(['author', 'date'])['revision'].count()


# In[13]:


#Sum for each commit by No of Lines
dframe.groupby(['author'])['number_of_lines'].sum()


# In[15]:


Author = dframe.author.value_counts()
print(Author)


# In[16]:


#Author_Count plotted using a bar graph
#Labels for x & y axis and title of graph created
Author_Count.plot(kind='bar')
plt.title("Authors Commits")
plt.xlabel("Author")
plt.ylabel("Frequency")


# In[18]:


#Changed the format of the Date column to datetime
dframe.date = pd.to_datetime(dframe.date)

#New column in dframe created. This deduces the day of the week for each date
dframe['Day']=dframe.date.dt.day_name()

#Variable Day created to count the instance of commits on each day
Day = dframe.Day.value_counts()
print(Day)


# In[19]:


#Day plotted using a horizontal bar graph
#Labels for x & y axis and title of graph created
Day.plot(kind='barh')
plt.title("Revisions by Day")
plt.ylabel("Day")
plt.xlabel("Frequency")


# In[20]:


#Breakdown of types of commits by day
dframe.groupby(['Day'])['number_of_lines'].sum()


# In[22]:


#New columns for hours created in dframe. This takes the hour information from the time column
dframe.Hours = dframe.time.map( lambda x: pd.to_datetime(x).hour )

#Hour variable created to count commits for each hour
Hour = dframe.Hours.value_counts()
Hour.sort_values()


# In[23]:


#Day plotted using a bar graph 
#Labels for x & y axis and title of graph created
Hour.plot(kind='bar')
plt.title("Revisions by Hour")
plt.ylabel("Frequency")
plt.xlabel("Hour (24hr clock)")


# In[24]:


#Day plotted using a pie chart - harder to read than bar graph
#Label for data and title of graph created
Hour.plot(kind='pie')
plt.title("Revisions by Hour")
plt.xlabel("Hour (24hr clock)")

