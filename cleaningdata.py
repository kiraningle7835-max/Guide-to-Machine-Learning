import pandas as pd
import numpy as np
df=pd.read_csv("data.csv")
newdf=df["Pulse"].to_string()
print((newdf))