#install pandas
#pip install pandas-profiling


import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('Dummy dataset.csv')
print(df)


#generate Report

profile = ProfileReport(df, minimal=True)
profile.to_file(output_file="Dummy_dataset.html")

profile.to_notebook_iframe()