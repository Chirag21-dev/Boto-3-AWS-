import os

directory = 'C:\Users\chirag_ks\Pictures\Saved Pictures'

for filename in os.listdir(directory):
    if filename.endswith('.png'):
        new_name = filename.replace(Screenshot (211)', 'Backup')
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
