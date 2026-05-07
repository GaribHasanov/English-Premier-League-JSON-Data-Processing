# English Premier League (2017/2018) Data Pipeline

## Project Overview
This project demonstrates an end-to-end data pipeline using the **English Premier League 2017/2018 match dataset**. The goal is to extract semi-structured JSON data, transform it using Python (Pandas), and load it into an Excel file for analysis.

---

## Objectives
- Extract data from a JSON dataset
- Parse and transform raw match data
- Perform data cleaning and feature engineering
- Determine half-time and full-time winners
- Export final dataset to Excel

---

## Tech Stack

- Python
- Pandas
- Jupyter Notebook
- Excel

---

## Data Processing Steps

### 1. Data Extraction
Load JSON dataset using Pandas:
- Convert semi-structured JSON into DataFrame

📌 Example:
![image](https://user-images.githubusercontent.com/60735401/215338209-e1eb446d-579c-473c-97a1-85ad94016394.png)

---

### 2. Data Parsing
- Convert JSON structure into readable tabular format
- Use `orient="index"` for proper column alignment

📌 Example:
![image](https://user-images.githubusercontent.com/60735401/215338309-c2a2f6b5-cc51-43fb-a62d-4b56578c5d6a.png)

---

### 3. Data Transformation
- Extract date, day, month, year, time from datetime column
- Create new columns for match metadata

📌 Example:
![image](https://user-images.githubusercontent.com/60735401/215339766-5ca25ef0-9950-4083-9985-4b5a45c23043.png)

---

### 4. Feature Engineering
- Extract half-time and full-time scores
- Create match result column
- Determine winners based on scores

📌 Example:
![image](https://user-images.githubusercontent.com/60735401/215340660-b9121849-af3e-4b63-b0a4-3884f675f43.png)

---

### 5. Winner Calculation Logic
- Compare home vs away scores
- Assign:
  - Home team winner
  - Away team winner
  - Draw (if equal)

📌 Example:
![image](https://user-images.githubusercontent.com/60735401/215341174-64602342-33b3-40d0-a304-10619ed3360b.png)

---

### 6. Final Dataset Preparation
- Add final winner column
- Select required columns
- Rename columns for clarity

📌 Example:
![image](https://user-images.githubusercontent.com/60735401/215341201-d4871741-1d01-4dd0-9906-d961bcae2773.png)

---

### 7. Export to Excel
Final dataset is exported using Pandas:

```python
df.to_excel('English_Premier_League.xlsx', sheet_name='English_League')
