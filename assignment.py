import pandas
import numpy
from IPython.display import HTML

def print_df(df):
    print("function does something")
    return HTML(df.to_html().replace('class="dataframe"', 'class="dataframe" style="font-size: 15pt'))

data = pandas.read_csv('datasets.csv')
print(data)
print(print_df(data.head()))