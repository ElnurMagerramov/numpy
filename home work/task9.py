import numpy as np

yesterday=np.datetime64('today','D') - np.timedelta64(1, 'D')
print("yesterday: ", yesterday)
today=np.datetime64('today','D')
print("\ntoday: ", today)
tomorrow=np.datetime64('today','D') + np.timedelta64(1, 'D')
print("\ntomorrow: ", tomorrow)