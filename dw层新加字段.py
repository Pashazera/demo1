import pandas as pd

pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)

path = r'C:\\Users\\pashazera\\Desktop\\'
name = r'test.xlsx'
pathname = path + name
data = pd.read_excel(pathname, header=None)
data = pd.DataFrame(data)

for i in range(len(data)):
    print('UPDATE dm_hngy_mkt.dwd_shops_origin \n' +
          'SET defect_field = defect_field + 1 \n' +
          'WHERE length({0}) = 0 OR {1} IS null;\n'
          .format(data.values[i][0], data.values[i][0]))