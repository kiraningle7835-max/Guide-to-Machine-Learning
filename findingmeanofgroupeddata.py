import pandas as pd
import numpy as np


data = {
    'Player': ["Amit", "John", "Amit", "David", "Steve", "John"],
    'Rank': [1, 4, 3, 5, 2, 7],
    'Points': [95, 70, 65, 80, 90, 50],
    'Year': [2023, 2022, 2021, 2022, 2023, 2019]
}


df = pd.DataFrame(data)
groupRes = df.groupby('Year')
print(groupRes['Points'].agg(np.mean))


