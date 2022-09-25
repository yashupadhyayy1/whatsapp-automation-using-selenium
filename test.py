import numpy as np
import pandas as pd

dataset = pd.read_csv('content_to share.csv')
username = dataset.iloc[:, 0].values
print(username)
for user_name in username:
    print('{}'.format(user_name))
username = ['mate']
for user_name in username:
    str2 = '\"' + user_name + '\"'
    print('{}'.format(str2))