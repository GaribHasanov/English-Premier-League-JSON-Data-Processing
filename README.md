# ⚽ English Premier League: Season Match Stats 2017/2018

### Data Extraction, Transformation, and Loading (ETL) Pipeline

This project demonstrates a complete ETL process: extracting raw data from a semi-structured **JSON** dataset, performing data cleaning and transformation using **Python**, and finally loading the processed data into an **Excel** file for reporting.

---

## 🚀 Project Overview
The goal is to convert complex JSON match statistics into a human-readable, structured format suitable for analysis.

### Workflow:
1.  **Extraction:** Loading raw JSON data.
2.  **Parsing & Transformation:** Cleaning strings, handling date-time objects, and calculating match winners.
3.  **Loading:** Exporting the final DataFrame to `.xlsx` format.

### 🛠 Tech Stack
*   **Language:** Python
*   **Library:** Pandas
*   **Environment:** Jupyter Notebook

---

## 📖 Step-by-Step Implementation

### 1. Initial Data Loading
We start by importing the necessary library and loading the dataset. To correctly parse the JSON structure where keys act as indices, we use the `orient="index"` parameter.
```python
import pandas as pd

# Reading the JSON file
df = pd.read_json("path_to_file.json", orient="index")
df.head(10)
