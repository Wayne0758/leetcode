import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values('event_date', inplace=True)
    activity['games_played_so_far'] = activity.groupby('player_id')['games_played'].cumsum()
    df = activity[['player_id', 'event_date', 'games_played_so_far']]
    return df
