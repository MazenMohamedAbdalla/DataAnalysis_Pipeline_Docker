import load
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

def data_cleaning(data):

    data = data.drop_duplicates()

    data = data.fillna(0)

    return data


def data_transformation(data):
    numeric_columns = data.select_dtypes(include='number').columns

    for column in numeric_columns:
        if data[column].dtype == 'object':
            data[column] = data[column].str.lower()

    for column in numeric_columns:
        min_val = data[column].min()
        max_val = data[column].max()
        data[column] = (data[column] - min_val) / (max_val - min_val)

    return data


def data_reduction(data):
    data = data.sample(frac=0.7)

    z_scores = np.abs((data - data.mean(numeric_only=True)) / data.std(numeric_only=True))

    z_threshold=3
    # Find rows with any Z-score greater than the threshold
    outliers = z_scores.apply(lambda x: any(x > z_threshold), axis=1)

    # Remove rows with outliers
    df_cleaned = data[~outliers]
    return df_cleaned

def data_discretization(data):
    numeric_columns = data.select_dtypes(include=['number'])
    num_clusters = 4
    kmeans = KMeans(n_clusters=num_clusters, random_state=0, n_init=10)
    data['cluster_label'] = kmeans.fit_predict(numeric_columns)

    bins = [0, 18, 30, 50, 80]
    labels = ['Child', 'Young Adult', 'Adult', 'Elderly']
    data['AgeGroup'] = pd.cut(data['Age at enrollment'], bins=bins, labels=labels)

    return data

if __name__ == "__main__":
    data = load.call()
    data = data_cleaning(data)
    data = data_transformation(data)
    data = data_reduction(data)
    data = data_discretization(data)
    data.to_csv('res_dpre.csv', index=False)
