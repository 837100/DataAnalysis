import pandas as pd

df = pd.read_csv(
    "data.csv",
    sep=",",
    nrows=None,
    header=0,
    encoding="utf-8",
    skiprows=None,
    index_col=None,
)
print(df)
