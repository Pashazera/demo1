import pandas as pd

data = pd.read_table('student.txt', encoding='utf-8', sep='[ \\t]+', engine='python')

print(data.values[:,1:])




