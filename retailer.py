import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


#Load the data
pd.options.display.float_format = '{:20.2f}'.format
pd.set_option('display.max_columns', 999)
retail_df = pd.read_excel('online_retail_II.xlsx', sheet_name=0)
print(retail_df.head(10))