import numpy as np
import pandas as pd
import math
pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)
data = pd.read_excel('data.xlsx')
data = data[['促销品单价','费用金额']]

powerMax = 0.1
winningRating = 1
data['powerMax'] = 0.1
data['winningRating'] = 1

pullRatio = int(input())


data['pullRatio'] = pullRatio

price1 = 150
data['price1'] = price1
def tN(i,str):
    return np.array(data.loc[[i],[str]]).tolist()[0][0]

number1 = []

def tNL(str,number):
    for i in range(len(data)):
        if tN(i, 'winningRating') < 1:
            n = tN(i, '促销品单价') / tN(i, 'powerMax') / (tN(i, str) / 10) * tN(i, 'winningRating')
            n = math.ceil(n)
            number.append(n)
        else:
            n = tN(i, '促销品单价') / tN(i, 'powerMax') / (tN(i, str) / 10) * (1 / tN(i, 'pullRatio'))
            n = math.ceil(n)
            number.append(n)
    return number


data['number1'] = tNL('price1',number1)

price2 = 250
data['price2'] = price2
number2 = []
data['number2'] = tNL('price2',number2)

price3 = 300
data['price3'] = price3
number3 = []
data['number3'] = tNL('price3',number3)

price4 = 350
data['price4'] = price4
number4 = []
data['number4'] = tNL('price4',number4)

price5 = 500
data['price5'] = price5
number5 = []
data['number5'] = tNL('price5',number5)

totalValue = tN(len(data)-1,'费用金额') / tN(len(data)-1,'powerMax')
data['totalValue'] = totalValue
print(data)

#data.to_excel('result.xlsx',index=False)


