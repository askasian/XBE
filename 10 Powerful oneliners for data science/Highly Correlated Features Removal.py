import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame(
    {
        "feature1": np.random.randn(100),
        "feature2": np.random.randn(100),
        "feature3": np.random.randn(100),
    }
)
df["feature4"] = df["feature1"] * 0.95 + np.random.randn(100) * 0.1

print(df)

# One-liner to remove highly correlated values
correlation_matrix = df.corr().abs()
print(correlation_matrix)

drop_features = [
    column
    for column in correlation_matrix.columns
    if any(
        correlation_matrix[column] > 0.9 and correlation_matrix[column].index != column
    )
]

print("correlation_matrix:")
print(correlation_matrix)

print("drop_features:")
print(drop_features)
