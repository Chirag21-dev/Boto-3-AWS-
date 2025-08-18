import os
import datetime

directory = 'C:\Users\chirag_ks\Pictures'
threshold_date = datetime.datetime(2024, 10, 12)

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    if os.path.isfile(filepath) and os.path.getmtime(filepath) < threshold_date.timestamp():
        os.remove(filepath)
