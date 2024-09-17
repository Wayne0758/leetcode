import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    min_event_dates = activity.groupby('player_id')['event_date'].min()
    df = pd.merge(activity, min_event_dates, on=['player_id', 'event_date'])
    df = df[['player_id', 'device_id']]
    return df
