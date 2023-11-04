import load
import pandas as pd
from sklearn.cluster import KMeans
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

load.r_dataset('res_dpre.csv')
df = load.call()

data = df[['Daytime/evening attendance', 'Previous qualification', 'Nacionality', 'Unemployment rate','Gender', 'Scholarship holder', 'Age at enrollment', 'International',
            'Inflation rate', 'GDP']]

model = KMeans(n_clusters=3, random_state=42)
model.fit(data)

cluster_counts = pd.Series(model.labels_).value_counts().sort_values()

with open('k.txt', 'w') as file:
    for cluster_label, count in cluster_counts.items():
        file.write(f"Cluster {cluster_label+1}: {count}\n")