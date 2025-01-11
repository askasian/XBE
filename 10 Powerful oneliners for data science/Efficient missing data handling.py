import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "A": [1, np.nan, 3, np.nan, 5],
        "B": [np.nan, 2, 3, 4, 5],
        "C": [1, 2, np.nan, 4, 5],
    }
)

cleaned_df = df.bfill()

print("Original DataFrame:")
print(df)

print("Cleaned DataFrame:")
print(cleaned_df)
