# ⚽ English Premier League: Season Match Stats 2017/2018

# ⚽ "English Premier League" - Season Match Stats 2017/2018

### Extract data from semi-structured (JSON) dataset, parse, transform and load into an Excel file.

---

## 🚀 Project Overview
This project demonstrates a complete **ETL (Extract, Transform, Load)** process using Python. We take raw match statistics in JSON format and convert them into a structured Excel report.

### Key Steps:
1.  **Extract:** Getting data from the JSON dataset.
2.  **Transform:** Parsing, cleaning, and feature engineering.
3.  **Load:** Exporting the final results into an Excel file.

### 🛠 Tools Used:
* **Jupyter Notebook** (Powerful web application for data science)
* **Python** (Pandas Library for data manipulation)

---

## 📖 Implementation Details

### 1. Extraction and Initial Parsing
The first step is to import the Pandas library and load the JSON data. Since the JSON keys are defined as indices, we use the `orient="index"` parameter to correctly format the DataFrame.

![image](https://user-images.githubusercontent.com/60735401/215338209-e1eb446d-579c-473c-97a1-85ad94016394.png)

Using the `read_json` function with proper orientation:

![image](https://user-images.githubusercontent.com/60735401/215338281-125577ec-7b93-42b4-925e-7cf42bf0f057.png)
<h4 align="center">Pic: 1</h4>

![image](https://user-images.githubusercontent.com/60735401/215338309-c2a2f6b5-cc51-43fb-a62d-4b56578c5d6a.png)
<h4 align="center">Pic: 2</h4>

---

### 2. Data Transformation (Date & Time)
We extract specific details like date, day, month, and year from the `date_string` column using datetime functions.

**Used functions:**
* `pd.to_datetime` - converting strings to datetime objects.
* `.dt.date`, `.dt.day`, `.dt.month_name()`, `.dt.year`, `.dt.time` - extracting specific parts.

![image](https://user-images.githubusercontent.com/60735401/215339766-5ca25ef0-9950-4083-9985-4b5a45c23043.png)
<h4 align="center">Pic: 3</h4>

---

### 3. Cleaning and Column Management
We enhance the readability by formatting the scores and creating a new `match result` column that combines team names and full-time scores.

```python
# Renaming for clarity
df.rename(columns = {'home_team_name':'home_team', 'away_team_name':'away_team'}, inplace = True)
