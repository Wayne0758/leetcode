import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:

    logs = logs[(logs.num == logs.num.shift(1)) &
                (logs.num == logs.num.shift(2))].drop_duplicates('num')
    logs.drop("id", axis=1, inplace=True)
    return logs.rename(columns = {'num':'ConsecutiveNums'})
