from pivottablejs import pivot_ui
import numpy as np
import pandas as pd


data = pd.DataFrame(
    {
    "Date": pd.date_range("2023-01-01", periods=100),
    "Category": np.random.choice(["A", "B", "C"], size=100),
    "Sales": np.random.randint(0, 100, size= 100),
    "Region": np.random.choice(["North", "South", "West", "East"], size=100)
    }
)

print(data)

pivot_ui(data, rows=["Category"], cols=["Region"], vals=["Sales"], aggregatorName="Sum")
