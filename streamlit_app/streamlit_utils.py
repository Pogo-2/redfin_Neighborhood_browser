import pandas as pd

def transform_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=["ADDRESS"])
    return df