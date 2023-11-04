import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import load

def piechart(df, target, output_filename):

    plt.figure(figsize=(12, 8))
    
    category_counts = df[target].value_counts()
    labels = category_counts.index
    sizes = category_counts / category_counts.sum() * 100

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal') 
    plt.title(f'Distribution of {target}')

    plt.savefig(output_filename)
    plt.close()
    
    return

load.r_dataset('res_dpre.csv')
data = load.call()
piechart(data, 'Target', 'vis.png')