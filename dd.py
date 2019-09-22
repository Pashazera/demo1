import numpy as np
import pandas as pd
import math
pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)
data = pd.read_excel('data.xlsx')
data = data[['促销品单价','费用金额']]
data.columns=['productPrice','amount']

powerMax = 0.1
winningRating = 1
data['powerMax'] = 0.1
data['winningRating'] = 1

#pullRatio = int(input())
pullRatio = 2

data['pullRatio'] = pullRatio

price1 = 150
data['price1'] = price1
def tN(i,str):
    return np.array(data.loc[[i],[str]]).tolist()[0][0]

number1 = []

def tNL(str,number):
    for i in range(len(data)):
        if tN(i, 'winningRating') < 1:
            n = tN(i, 'productPrice') / tN(i, 'powerMax') / (tN(i, str) / 10) * tN(i, 'winningRating')
            n = math.ceil(n)
            number.append(n)
        else:
            n = tN(i, 'productPrice') / tN(i, 'powerMax') / (tN(i, str) / 10) * (1 / tN(i, 'pullRatio'))
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

totalValue = tN(len(data)-1,'amount') / tN(len(data)-1,'powerMax')
data['totalValue'] = totalValue
print(data)

#data.to_excel('result.xlsx',index=False)

newNumbers = pd.read_excel('newNumber.xlsx')
print(newNumbers.drop([5]))

def noNTL(price,newNumber):
    x = []
    if 1 in data.winningRating.values:
        for a , b , c , d ,e in zip(data.productPrice.values,data.powerMax.values,price,data.pullRatio.values,newNumber):
            n = e*d*b*c/10/a
            n = math.floor(n)
            x.append(n)

    else:
        for a , b , c , d ,e in zip(data.productPrice.values,data.powerMax.values,price,newNumber,data.winningRating.values):
            n = d*b*c/10/a/e
            n = math.floor(n)
            x.append(n)

    return x

print(noNTL(data.price1.values,newNumbers.newNumber1.values))
print(noNTL(data.price2.values,newNumbers.newNumber2.values))
print(noNTL(data.price3.values,newNumbers.newNumber3.values))
print(noNTL(data.price4.values,newNumbers.newNumber4.values))
print(noNTL(data.price5.values,newNumbers.newNumber5.values))

achievements = pd.DataFrame()
achievements['productPrice'] = data['productPrice']
achievements['price1'] = data['price1']
achievements['achievement1'] = noNTL(data.price1.values,newNumbers.newNumber1.values)
achievements['price2'] = data['price2']
achievements['achievement2'] = noNTL(data.price2.values,newNumbers.newNumber2.values)
achievements['price3'] = data['price3']
achievements['achievement3'] = noNTL(data.price3.values,newNumbers.newNumber3.values)
achievements['price4'] = data['price4']
achievements['achievement4'] = noNTL(data.price4.values,newNumbers.newNumber4.values)
achievements['price5'] = data['price5']
achievements['achievement5'] = noNTL(data.price5.values,newNumbers.newNumber5.values)
achievements.drop([5],inplace=True)
print(achievements)