import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.drop_duplicates(["salary"])
    if len(employee["salary"]) < N or N<1:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    employee = employee.sort_values("salary", ascending=False)
    employee.drop(columns='id', inplace=True)
    employee.rename(columns={'salary':f'getNthHighestSalary({N})'}, inplace=True)
    return employee.head(N).tail(1)
