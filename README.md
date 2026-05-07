# "English Premier League"- season match stats 2017/2018

## Extract data from "English Premier League" semi-structed (JSON) dataset, parse, transform and load into an Excel file.

---

### Hi,Friends

I am going to show you getting data from semi-structed (JSON) dataset, parse, transform and load into an Excel file

### Steps:
1. Extracting data from JSON dataset  
2. Parsing and Transforming  
3. Loading into an Excel file  

---

### Used tools:
1. Jupyter Notebook  
2. Pyton (Pandas Library)  

---

## JSON dataset content:
"English Premier League"-season match stats 2017/2018

![image](https://user-images.githubusercontent.com/60735401/215338209-e1eb446d-579c-473c-97a1-85ad94016394.png)

---

## First of all

We need Jupyter notebook. We can follow the steps with different application or tools. The Jupyter notebook is one of the powerful web application for data purpose.

1. We have to import pandas  
2. Use “read_json” function to convert JSON string to pandas object  

![image](https://user-images.githubusercontent.com/60735401/215338281-125577ec-7b93-42b4-925e-7cf42bf0f057.png)

<h4 align="center">Pic:1</h4>

The output is not understandable because keys of JSON are defined as indexes instead of columns.

In this case, we have to use `orient="index"` and replace indexes to columns and columns to indexes.

**orient="index"** – defines indexes as columns  
**head(10) function** – retriving 10 rows  

![image](https://user-images.githubusercontent.com/60735401/215338309-c2a2f6b5-cc51-43fb-a62d-4b56578c5d6a.png)

<h4 align="center">Pic:2</h4>

So, we extracted and parsed the JSON dataset into a readable and understandable form.

Now, it's time to transform data.

Let’s try to get date, time, day, month, year parts from 'date_string' column.

---

### Used functions:

1. pd.to_datetime - converting argument/string/object to datetime data type  
2. dt.date - extracts date part from datetime  
3. dt.day - extracts day part from datetime  
4. dt.month_name() - extracts month part (with name) from datetime  
5. dt.year - extracts year part from datetime  
6. dt.time - extracts time part from datetime  

We need to add new columns and assign extracted value with above function to it.

### New columns:
df['match_date'] =  
df['day'] =  
df['month'] =  
df['year'] =  
df['time'] =  

![image](https://user-images.githubusercontent.com/60735401/215339766-5ca25ef0-9950-4083-9985-4b5a45c23043.png)

<h4 align="center">Pic:3</h4>

---

### Continue transformation

Let’s concatenate parentheses with **'half_time_score'** and **'full_time_score'** values.

df['half_time_score'] = '(' + df[['half_time_score']] + ')'  
df['full_time_score'] = '(' + df[['full_time_score']] + ')'  

After that add new **“match result”** column:

df['match result'] = df['home_team_name'] +' '+ df['full_time_score'] +' '+ df['away_team_name']

Retrieve only needed columns:

df = df[['home_team_name', 'away_team_name','match result','match_date','day','month','year',
         'time','half_time_score','full_time_score']]

Rename columns:

df.rename(columns = {'home_team_name':'home_team', 'away_team_name':'away_team'}, inplace = True)

**inplace** – performs changing on original DataFrame  

![image](https://user-images.githubusercontent.com/60735401/215340660-b9121849-af3e-4b63-b0a4-3884d7ffd375.png)

<h4 align="center">Pic:4</h4>

---

### Extract scores

df['home_team_score_half_time'] = df['half_time_score'].str.strip().str[1]  
df['away_team_score_half_time'] = df['half_time_score'].str.strip().str[-2]  

df['home_team_score_full_time'] = df['full_time_score'].str.strip().str[1]  
df['away_team_score_full_time'] = df['full_time_score'].str.strip().str[-2]  

![image](https://user-images.githubusercontent.com/60735401/215341125-32039a69-bcc2-4f88-81c9-0c59f7302762.png)

<h4 align="center">Pic:5</h4>

---

### Determine winners

df.loc[df['home_team_score_half_time'] > df['away_team_score_half_time'], 'half_time_winner'] = df['home_team']  
df.loc[df['home_team_score_half_time'] < df['away_team_score_half_time'], 'half_time_winner'] = df['away_team']  
df.loc[df['home_team_score_half_time'] == df['away_team_score_half_time'], 'half_time_winner'] = 'Draw'  

df.loc[df['home_team_score_full_time'] > df['away_team_score_full_time'], 'full_time_winner'] = df['home_team']  
df.loc[df['home_team_score_full_time'] < df['away_team_score_full_time'], 'full_time_winner'] = df['away_team']  
df.loc[df['home_team_score_full_time'] == df['away_team_score_full_time'], 'full_time_winner'] = 'Draw'  

![image](https://user-images.githubusercontent.com/60735401/215341174-64602342-33b3-40d0-a304-10619ed3360b.png)

<h4 align="center">Pic:6</h4>

---

### Final dataset

df['winner'] = df['full_time_winner']

df = df[['home_team','away_team','match_result','half_time_winner','half_time_score','full_time_score','full_time_winner','winner','match_date','day','month','year','time']]

![image](https://user-images.githubusercontent.com/60735401/215341201-d4871741-1d01-4dd0-9906-d961bcae2773.png)

<h4 align="center">Pic:7</h4>

---

### Load to Excel

df.to_excel('English_Premier_League.xlsx', sheet_name = 'English_League')

![image](https://user-images.githubusercontent.com/60735401/215341217-00333350-3434-4d26-8f38-747c2f72c230.png)

<h4 align="center">Pic:8</h4>

---

### Output

![image](https://user-images.githubusercontent.com/60735401/215341230-4191a7ff-020f-46f6-ae25-a7483f9221d3.png)

![image](https://user-images.githubusercontent.com/60735401/215341235-e82004fb-6a0b-4278-83ce-567b93f45098.png)

<h4 align="center">Pic:9</h4>

<h4 align="center">Pic:10</h4>

---

## Conclusion

We have learnt how to extract data from JSON dataset, parse, transform it with powerful Pandas library of Python and load it to an Excel file.
