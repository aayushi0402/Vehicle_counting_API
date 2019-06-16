import pandas as pd
import numpy as np

data = pd.read_csv('traffic_measurement.csv',names = ['Vehicle Type','Direction'])
up = data.loc[data['Direction']== "up"].groupby("Vehicle Type").count()
down = data.loc[data['Direction']== "down"].groupby("Vehicle Type").count()
upcount = up.to_dict('series')
downcount = down.to_dict('series')
upcount
downcount
