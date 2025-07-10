import pandas as pd
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv("melb_data.csv") 
# print a summary of the data in Melbourne data
melbourne_data.describe()