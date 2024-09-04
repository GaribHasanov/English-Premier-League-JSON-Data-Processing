# English Premier League - season_match_stats 2017/2018
import pandas as pd
df = pd.read_json("English_Premier_League_match_stats.json",orient="index")
#df.iloc[:,2:10]
df['match_date'] = pd.to_datetime(df['date_string']).dt.date
df['day'] = pd.to_datetime(df['date_string']).dt.day
df['month'] = pd.to_datetime(df['date_string']).dt.month_name()
df['year'] = pd.to_datetime(df['date_string']).dt.year
df['time'] = pd.to_datetime(df['date_string']).dt.time
df['half_time_score'] = '(' + df[['half_time_score']] + ')'
df['full_time_score'] = '(' + df[['full_time_score']] + ')'
df['match result'] = df['home_team_name'] +' '+ df['full_time_score'] +' '+ df['away_team_name']
df = df[['home_team_name', 'away_team_name','match result','match_date','day','month','year','time','half_time_score','full_time_score']]
df.rename(columns = {'home_team_name':'home_team', 'away_team_name':'away_team'}, inplace = True)

df['home_team_score_half_time'] = df['half_time_score'].str.strip().str[1]
df['away_team_score_half_time'] = df['half_time_score'].str.strip().str[-2]

df['home_team_score_full_time'] = df['full_time_score'].str.strip().str[1]
df['away_team_score_full_time'] = df['full_time_score'].str.strip().str[-2]


df.loc[df['home_team_score_half_time'] >  df['away_team_score_half_time'], 'half_time_winner'] = df['home_team']  
df.loc[df['home_team_score_half_time'] <  df['away_team_score_half_time'], 'half_time_winner'] = df['away_team']  
df.loc[df['home_team_score_half_time'] == df['away_team_score_half_time'], 'half_time_winner'] = 'Draw' 


df.loc[df['home_team_score_full_time'] >  df['away_team_score_full_time'], 'full_time_winner'] = df['home_team']  
df.loc[df['home_team_score_full_time'] <  df['away_team_score_full_time'], 'full_time_winner'] = df['away_team']  
df.loc[df['home_team_score_full_time'] == df['away_team_score_full_time'], 'full_time_winner'] = 'Draw' 

df['winner'] = df['full_time_winner']

df = df[['home_team', 'away_team','match result','half_time_winner','half_time_score','full_time_score','full_time_winner','winner','match_date','day','month','year','time']]

df.to_excel('English_Premier_League.xlsx',sheet_name = 'English_League' )
df