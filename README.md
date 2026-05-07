# English Premier League - Season Match Stats (2017/2018)

## Project Overview
This project demonstrates how to extract data from a semi-structured JSON dataset, parse it, transform it using Python (Pandas), and load the final structured data into an Excel file.

---

## Steps
1. Extract data from JSON dataset  
2. Parse and transform data  
3. Load data into Excel file  

---

## Tools Used

- Jupyter Notebook  
- Python (Pandas Library)  

---

## Dataset

English Premier League - Season Match Stats 2017/2018  

![image](https://user-images.githubusercontent.com/60735401/215338209-e1eb446d-579c-473c-97a1-85ad94016394.png)

---

## 1. Data Extraction

We start by loading the JSON dataset using Jupyter Notebook.

- Import Pandas
- Use `read_json()` to convert JSON into a DataFrame

![image](https://user-images.githubusercontent.com/60735401/215338281-125577ec-7b93-42b4-925e-7cf42bf0f057.png)

---

## 2. Data Parsing

The output is not structured properly because JSON keys are treated as indexes.

To fix this:
- Use `orient="index"`
- Convert indexes into columns

- `head(10)` → displays first 10 rows

![image](https://user-images.githubusercontent.com/60735401/215338309-c2a2f6b5-cc51-43fb-a62d-4b56578c5d6a.png)

---

## 3. Data Transformation

We extract date-related fields from the `date_string` column.

### Functions used:
- `pd.to_datetime()`
- `dt.date`
- `dt.day`
- `dt.month_name()`
- `dt.year`
- `dt.time`

### New columns:
- match_date  
- day  
- month  
- year  
- time  

![image](https://user-images.githubusercontent.com/60735401/215339766-5ca25ef0-9950-4083-9985-4b5a45c23043.png)

---

## 4. Feature Engineering

We format scores and create match results.

- Add parentheses to scores
- Create match result column

```python
df['match_result'] = df['home_team_name'] + ' ' + df['full_time_score'] + ' ' + df['away_team_name']
