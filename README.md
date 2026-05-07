# ⚽ English Premier League: Season Match Stats 2017/2018

### Extract data from the "English Premier League" semi-structured (JSON) dataset, then parse, transform, and load it into an Excel file.

---

### 
In this project, I will demonstrate how to extract data from a semi-structured (JSON) dataset, parse and transform it, and finally load it into an Excel file.

### Steps:
1. Extract data from JSON dataset  
2. Parse and transform the data  
3. Load data into an Excel file  

---

### Used tools:
1. Jupyter Notebook  
2. Python (Pandas Library)  

---

## JSON dataset content:
"English Premier League" – season match stats 2017/2018

![image](https://user-images.githubusercontent.com/60735401/215338209-e1eb446d-579c-473c-97a1-85ad94016394.png)

---

## First of all

We need Jupyter Notebook. The workflow can also be implemented using other tools; however, Jupyter Notebook is one of the most powerful web-based applications for data analysis.

1. We import the Pandas library  
2. We use the `read_json()` function to convert the JSON string into a Pandas object  

![image](https://user-images.githubusercontent.com/60735401/215338281-125577ec-7b93-42b4-925e-7cf42bf0f057.png)
<h4 align="center">Pic:1</h1>

The output is not immediately readable because the JSON keys are treated as indexes instead of column names.

In this case, we use `orient="index"` to convert indexes into columns.

***orient="index"*** – defines indexes as columns  
***head(10) function*** – retrieves the first 10 rows  

![image](https://user-images.githubusercontent.com/60735401/215338309-c2a2f6b5-cc51-43fb-a62d-4b56578c5d6a.png)
<h4 align="center">Pic:2</h1>

At this stage, we successfully extract and parse the JSON dataset into a readable and structured format.

Now it is time for data transformation.

Let’s extract date, time, day, month, and year components from the `date_string` column.

---

### Used functions:

1. `pd.to_datetime` – converts a string/object into datetime format  
2. `dt.date` – extracts date component  
3. `dt.day` – extracts day component  
4. `dt.month_name()` – extracts month name  
5. `dt.year` – extracts year  
6. `dt.time` – extracts time  

We create new columns and assign extracted values to them.

---

### New columns:

df['match_date'] =  
df['day'] =  
df['month'] =  
df['year'] =  
df['time'] =  

![image](https://user-images.githubusercontent.com/60735401/215339766-5ca25ef0-9950-4083-9985-4b5a45c23043.png)
<h4 align="center">Pic:3</h1>

---

### Continue transformation

Next, we add parentheses to the **'half_time_score'** and **'full_time_score'** columns for better formatting.

df['half_time_score'] = '(' + df[['half_time_score']] + ')'  
df['full_time_score'] = '(' + df[['full_time_score']] + ')'  

We then create a new **"match result"** column by combining team names and full-time score:

df['match result'] = df['home_team_name'] + ' ' + df['full_time_score'] + ' ' + df['away_team_name']

We also select only the required columns:

df = df[['home_team_name', 'away_team_name','match result','match_date','day','month','year',
         'time','half_time_score','full_time_score']]

Finally, we rename columns for clarity:

df.rename(columns={'home_team_name':'home_team', 'away_team_name':'away_team'}, inplace=True)

***inplace*** function – applies changes directly to the original DataFrame  

![image](https://user-images.githubusercontent.com/60735401/215340660-b9121849-af3e-4b63-b0a4-3884d7ffd375.png)
<h4 align="center">Pic:4</h1>

---

At this point, half-time and full-time scores already exist. Now we need to determine match winners.

Based on the DataFrame structure, the left side represents the home team and the right side represents the away team.

Although we could directly infer winners from scores, this is not a professional approach.

Therefore, we extract individual score values and determine winners properly.

---

### New columns:

df['home_team_score_half_time'] =  
df['away_team_score_half_time'] =  
df['home_team_score_full_time'] =  
df['away_team_score_full_time'] =  

df['home_team_score_half_time'] = df['half_time_score'].str.strip().str[1]  
df['away_team_score_half_time'] = df['half_time_score'].str.strip().str[-2]  

df['home_team_score_full_time'] = df['full_time_score'].str.strip().str[1]  
df['away_team_score_full_time'] = df['full_time_score'].str.strip().str[-2]  

***str.strip()*** – removes leading and trailing characters  

![image](https://user-images.githubusercontent.com/60735401/215341125-32039a69-bcc2-4f88-81c9-0c59f7302762.png)
<h4 align="center">Pic:5</h1>

---

We now determine half-time and full-time winners.

- Home team is represented on the left side  
- Away team is represented on the right side  

---

### Conditions:

1. If home team score < away team score → away team wins  
2. If home team score > away team score → home team wins  
3. If scores are equal → Draw  

The same logic is applied for both half-time and full-time results.

---

### Condition code:

df.loc[df['home_team_score_half_time'] > df['away_team_score_half_time'], 'half_time_winner'] = df['home_team']  
df.loc[df['home_team_score_half_time'] < df['away_team_score_half_time'], 'half_time_winner'] = df['away_team']  
df.loc[df['home_team_score_half_time'] == df['away_team_score_half_time'], 'half_time_winner'] = 'Draw'  

df.loc[df['home_team_score_full_time'] > df['away_team_score_full_time'], 'full_time_winner'] = df['home_team']  
df.loc[df['home_team_score_full_time'] < df['away_team_score_full_time'], 'full_time_winner'] = df['away_team']  
df.loc[df['home_team_score_full_time'] == df['away_team_score_full_time'], 'full_time_winner'] = 'Draw'  

***loc()*** function – allows efficient data selection and assignment based on conditions  

![image](https://user-images.githubusercontent.com/60735401/215341174-64602342-33b3-40d0-a304-10619ed3360b.png)
<h4 align="center">Pic:6</h1>

---

Half-time and full-time winners are now determined. The full-time winner represents the final match result.

We create a new column for the final winner:

df['winner'] = df['full_time_winner']

We then select the final required dataset:

df = df[['home_team','away_team','match_result','half_time_winner','half_time_score','full_time_score','full_time_winner','winner','match_date','day','month','year','time']]

![image](https://user-images.githubusercontent.com/60735401/215341201-d4871741-1d01-4dd0-9906-d961bcae2773.png)
<h4 align="center">Pic:7</h1>

---

Finally, we export the dataset into an Excel file:

df.to_excel('English_Premier_League.xlsx', sheet_name='English_League')

Excel file name and sheet name can be customized as needed.

***to_excel()*** function – exports a DataFrame to an Excel file  

![image](https://user-images.githubusercontent.com/60735401/215341217-00333350-3434-4d26-8f38-747c2f72c230.png)
<h4 align="center">Pic:8</h1>

---

### Output:

![image](https://user-images.githubusercontent.com/60735401/215341230-4191a7ff-020f-46f6-ae25-a7483f9221d3.png)
<h4 align="center">Pic:9</h1>

![image](https://user-images.githubusercontent.com/60735401/215341235-e82004fb-6a0b-4278-83ce-567b93f45098.png)
<h4 align="center">Pic:10</h1>

---

## Conclusion

In this project, we learned how to extract data from a JSON dataset, parse and transform it using the powerful Pandas library in Python, and load the processed data into an Excel file for further analysis.
