# "English Premier League"- season match stats 2017/2018
### Extract data from "English Premier League" semi-structed (JSON) dataset, parse, transform and load into an Excel file.

***Hi,Friends***
I am going to show you getting data from semi-structed (JSON) dataset, parse, transform and load into an Excel file
Steps:
1. Extracting data from JSON dataset
2. Parsing and Transforming
3. Loading into an Excel file.

***Used tools:***<br>
1. Jupyter Notebook
2. Pyton (Pandas Library)

JSON dataset content:
"English Premier League"-season match stats 2017/2018

![image](https://user-images.githubusercontent.com/60735401/215338209-e1eb446d-579c-473c-97a1-85ad94016394.png)

***First of all***

We need Jupyter notebook. We can follow the steps with different application or tools. The Jupyter notebook is one of the powerful web application for data purpose
1.	We have to import pandas.
2.	Use “read_json” function to convert JSON string to pandas object. 

![image](https://user-images.githubusercontent.com/60735401/215338281-125577ec-7b93-42b4-925e-7cf42bf0f057.png)
<h4 align="center">Pic:1</h1>

The output is not understandable because keys of JSON are defined as indexes instead of columns.
In this case, we have to use orient="index" and replace indexes to columns and columns to indexes.

***orient="index"*** – defines indexes as columns<br>
***head(10) function*** – retriving 10 rows.<br>

![image](https://user-images.githubusercontent.com/60735401/215338309-c2a2f6b5-cc51-43fb-a62d-4b56578c5d6a.png)
<h4 align="center">Pic:2</h1>

So, we extracted and parsed the JSON dataset into a readable and understandable form.<br>
Now, it's time to transform data.
Let’s try to get date, time, day, month, year parts from 'date_string' column.

***Used functions:***<br>

1. pd.to_datetime - converting argument/string/object to datetime data type.<br>
2. dt.date - extracts date part from datetime.<br>
3. dt.day -  extracts day part from datetime.<br>
4. dt.month_name() - extracts month part (with name) from datetime.<br>
5. dt.year - extracts year part from datetime.<br>
6. dt.time - extracts time part from datetime.<br>

We need to add new columns and assign extracted value with above function to it.<br> 

***New columns:*** <br> 

df['match_date'] =<br> 
df['day'] =<br> 
df['month'] =<br> 
df['year'] =<br> 
df['time'] =<br> 

In Python, if you want to add new column to the pandas object you have to define column name and assign value to it. If new column name is existing column name in this case the existing column name will be updated, if there is no any matched column name with new column name then it will be added as a new column.

![image](https://user-images.githubusercontent.com/60735401/215339766-5ca25ef0-9950-4083-9985-4b5a45c23043.png)
<h4 align="center">Pic:3</h1>

***Continue transformation.***<br>

Let’s concatenate parentheses with ***'half_time_score'*** and ***'full_time_score'*** values.<br>
***df['half_time_score']*** = ***'(' + df[['half_time_score']] + ')'*** <br>
***df['full_time_score']*** = ***'(' + df[['full_time_score']] + ')'*** <br>

After that add new ***“match result “*** column and concatenate ***'home_team_name'*** and ***'away_team_name'*** column values with the values of ***'full_time_score'*** column.<br>
***df['match result']*** = ***df['home_team_name'] +' '+ df['full_time_score'] +' '+ df['away_team_name']***

***AND*** we should retrieve only needed columns and rename name of the existing columns:<br>
***Retrieving only needed columns:***<br>
***df*** = ***df[['home_team_name', 'away_team_name','match result','match_date','day','month','year',
         'time','half_time_score','full_time_score']]***

***Renaming existing columns:***<br>

***df.rename(columns = {'home_team_name':'home_team', 'away_team_name':'away_team'}, inplace = True)***<br>
***inplace*** function – performs changing on original DataFrame.<br>

![image](https://user-images.githubusercontent.com/60735401/215340660-b9121849-af3e-4b63-b0a4-3884d7ffd375.png)
<h4 align="center">Pic:4</h1>

So, There are already half time and full time score. We need to find half time winner and full time winner.<br>
Based on the “DataFrame”, we see that left side is home team and right side is away team. <br>

As an example of half time score of first row is **(0 : 2)** and we can say **half-time** winner is **“Liverpool”** , **full-time** score is **(0 : 3)** and we can full time winner is also **“Liverpool”** but this approach is not professional approach 😊<br>

We have to extract half time and full time scores from **'half_time_score'** and **'full_time_score'** column and determine the half and full time exact winners.
I am going to add four new columns and extract each single score and assign to new columns.<br>

***New columns:*** <br>

**df['home_team_score_half_time']** =<br>
**df['away_team_score_half_time']** =<br>
**df['home_team_score_full_time']** =<br>
**df['away_team_score_full_time']** =<br>

**df['home_team_score_half_time']** = **df['half_time_score'].str.strip().str[1]**<br>
**df['away_team_score_half_time']** = **df['half_time_score'].str.strip().str[-2]**<br>

**df['home_team_score_full_time']** = **df['full_time_score'].str.strip().str[1]**<br>
**df['away_team_score_full_time']** = **df['full_time_score'].str.strip().str[-2]**<br>
**str.strip()** function – is used to remove leading and trailing characters.<br>

![image](https://user-images.githubusercontent.com/60735401/215341125-32039a69-bcc2-4f88-81c9-0c59f7302762.png)
<h4 align="center">Pic:5</h1>

We have already extracted scores in the separate columns and we have to determine half-time and full-time winners.<br>

As we mentioned above that we know already **left side** and **right side** teams.<br>
Left side team is **“home_team”**, right side team is **“away_team”** and there are score extracted columns described below:<br>
1) **“home_team_score_half_time”**,  2) **“away_team_score_half_time”**, 3)**“home_team_score_full_time”**, 4) **“away_team_score_full_time”**<br>

## Now, time to add condition and determine the **half-time** and **full-time** winner.<br>

1. If the **“half time home team score”** is less than **“half time away team score”** it means **“away_team”** is half time winner then it will return **“away_team” name.**<br>
2. If the **“full time home team score”** is greater than **“full time away team score”** it means **“home_team”** is full time winner then it will return **“home_team”** name.<br>
3. If the **“half time home team score”** is equal to **“half time away team score”** it means scores are **draw** then it will return **“Draw”**.<br>
4. If the **“full time home team score”** is equal to **“full time away team score”** it means scores are **draw** then it will return **“Draw”**.<br>

**Condition code:**<br>

**df.loc[df['home_team_score_half_time']** >  **df['away_team_score_half_time']**, **'half_time_winner']** = **df['home_team']**<br>
**df.loc[df['home_team_score_half_time']** <  **df['away_team_score_half_time']**, **'half_time_winner']** = **df['away_team']**<br>
**df.loc[df['home_team_score_half_time']** == **df['away_team_score_half_time']**, **'half_time_winner']** = **'Draw'**<br>

**df.loc[df['home_team_score_full_time']** >  **df['away_team_score_full_time']**, **'full_time_winner']** = **df['home_team']**<br>
**df.loc[df['home_team_score_full_time']** <  **df['away_team_score_full_time']**, **'full_time_winner']** = **df['away_team']**<br>
**df.loc[df['home_team_score_full_time']** == **df['away_team_score_full_time']**, **'full_time_winner']** = **'Draw'**<br>

**loc()** function – helps us to retrieve data values from a dataset at an ease.<br>
Using the **loc()** function, we can access the data values fitted in the particular row or column based on the index value passed to the function.<br>

![image](https://user-images.githubusercontent.com/60735401/215341174-64602342-33b3-40d0-a304-10619ed3360b.png)
<h4 align="center">Pic:6</h1>

**Half-time** and **full-time** winners are determined, **full-time** winner is the main winner of the game. Now let’s add new winner column and assign **full-time** winner to it and retrieve only needed columns.<br>

Adding new winner column and assign **full_time_winner** to it <br>
**df['winner']** = **df['full_time_winner']**

Retrieving final needed columns <br>
**df = df[['home_team','away_team','match_result','half_time_winner','half_time_score','full_time_score','full_time_winner','winner','match_date','day','month','year','time']]**<br>

![image](https://user-images.githubusercontent.com/60735401/215341201-d4871741-1d01-4dd0-9906-d961bcae2773.png)
<h4 align="center">Pic:7</h1>
Thus, we have come to the end. Its time to load our work to an Excel file.<br>
df.to_excel('English_Premier_League.xlsx', sheet_name = 'English_League' )

Excel file name and sheet name can be set as desired.<br>
***to_excel()*** function -  is used to write object to an Excel file.

![image](https://user-images.githubusercontent.com/60735401/215341217-00333350-3434-4d26-8f38-747c2f72c230.png)
<h4 align="center">Pic:8</h1>

### Output: ###
![image](https://user-images.githubusercontent.com/60735401/215341230-4191a7ff-020f-46f6-ae25-a7483f9221d3.png)
<h4 align="center">Pic:9</h1>

![image](https://user-images.githubusercontent.com/60735401/215341235-e82004fb-6a0b-4278-83ce-567b93f45098.png)
<h4 align="center">Pic:10</h1>

### Conclusion ###
We have learnt how to extract data from JSON dataset, parse, transform it with powerful Pandas library of Python and load it to an Excel file.
