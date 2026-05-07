import pandas as pd


# =========================
# 1. LOAD DATA
# =========================
def load_data(file_path: str) -> pd.DataFrame:
    df = pd.read_json(file_path, orient="index")
    return df


# =========================
# 2. DATE FEATURES
# =========================
def add_date_features(df: pd.DataFrame) -> pd.DataFrame:
    date = pd.to_datetime(df['date_string'])

    df['match_date'] = date.dt.date
    df['day'] = date.dt.day
    df['month'] = date.dt.month_name()
    df['year'] = date.dt.year
    df['time'] = date.dt.time

    return df


# =========================
# 3. SCORE FORMATTING
# =========================
def format_scores(df: pd.DataFrame) -> pd.DataFrame:
    df['half_time_score'] = '(' + df['half_time_score'] + ')'
    df['full_time_score'] = '(' + df['full_time_score'] + ')'
    return df


# =========================
# 4. MATCH RESULT
# =========================
def add_match_result(df: pd.DataFrame) -> pd.DataFrame:
    df['match_result'] = (
        df['home_team_name'] + ' ' +
        df['full_time_score'] + ' ' +
        df['away_team_name']
    )
    return df


# =========================
# 5. RENAME COLUMNS
# =========================
def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    return df.rename(columns={
        'home_team_name': 'home_team',
        'away_team_name': 'away_team'
    })


# =========================
# 6. SCORE EXTRACTION
# =========================
def extract_scores(df: pd.DataFrame) -> pd.DataFrame:
    df['home_ht'] = df['half_time_score'].str[1]
    df['away_ht'] = df['half_time_score'].str[-2]

    df['home_ft'] = df['full_time_score'].str[1]
    df['away_ft'] = df['full_time_score'].str[-2]

    return df


# =========================
# 7. WINNER LOGIC
# =========================
def determine_winners(df: pd.DataFrame) -> pd.DataFrame:

    df['half_time_winner'] = df.apply(
        lambda x: 'Draw' if x['home_ht'] == x['away_ht']
        else x['home_team'] if x['home_ht'] > x['away_ht']
        else x['away_team'], axis=1
    )

    df['full_time_winner'] = df.apply(
        lambda x: 'Draw' if x['home_ft'] == x['away_ft']
        else x['home_team'] if x['home_ft'] > x['away_ft']
        else x['away_team'], axis=1
    )

    df['winner'] = df['full_time_winner']

    return df


# =========================
# 8. FINAL CLEANUP
# =========================
def finalize(df: pd.DataFrame) -> pd.DataFrame:

    columns = [
        'home_team', 'away_team', 'match_result',
        'half_time_winner', 'full_time_winner', 'winner',
        'match_date', 'day', 'month', 'year', 'time'
    ]

    return df[columns]


# =========================
# 9. EXPORT
# =========================
def export(df: pd.DataFrame, output_path: str):
    df.to_excel(output_path, sheet_name="English_League", index=False)


# =========================
# MAIN PIPELINE (ENTRY POINT)
# =========================
def main():
    file_path = "data/English_Premier_League_match_stats.json"
    output_path = "output/English_Premier_League.xlsx"

    df = load_data(file_path)
    df = add_date_features(df)
    df = format_scores(df)
    df = add_match_result(df)
    df = rename_columns(df)
    df = extract_scores(df)
    df = determine_winners(df)
    df = finalize(df)
    export(df, output_path)


if __name__ == "__main__":
    main()