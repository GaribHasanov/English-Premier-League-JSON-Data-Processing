# English Premier League Season 2017/2018 – Match Statistics ETL Pipeline (JSON → Excel)

## Project Overview

This project demonstrates a complete **ETL (Extract, Transform, Load)** workflow applied to a semi-structured JSON dataset containing match statistics from the English Premier League 2017/2018 season.

The goal is to extract raw data, transform it into a structured and analyzable format using Python, and finally export it into an Excel file for further analysis or reporting.

---

## Objectives

- Extract data from a semi-structured JSON dataset  
- Parse and restructure the data into a tabular format  
- Perform data transformation and feature engineering  
- Derive meaningful match insights such as winners and scores  
- Export the processed dataset into an Excel file  

---

## Technologies Used

- Jupyter Notebook  
- Python  
- Pandas Library  

---

## Dataset Description

The dataset contains detailed match statistics from the **English Premier League 2017/2018 season**, including team names, scores, match dates, and results.

![image](https://user-images.githubusercontent.com/60735401/215338209-e1eb446d-579c-473c-97a1-85ad94016394.png)

---

## 1. Data Extraction

The first step involves loading the JSON dataset into a Pandas DataFrame using the `read_json()` function.

```python
import pandas as pd

df = pd.read_json("data.json")
