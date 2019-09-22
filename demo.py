import numpy as np
import pandas as pd

class Resources:
    def __init__(self,sourcesName,price,number,cost):
        self.sourcesName = sourcesName
        self.price = price
        self.number = number
        self.cost = price * number
        self.proprotion = None



    def setProprotion(self,x):
        self.proprotion = x

    def info(self):
        print(self.sourcesName,self.price,self.number,self.cost)

class ResourcesSheet:
    def __init__(self):
        self.resources = []
        self.resourcesAge = np.array([])

    def setResourcesSheet(self,*resources):

        for x in resources:
            self.resources.append(x)
        self.resources = np.array(resources)


        # self.resourcesAge = Resources('平均',sum(resources[:,1]),sum(resources[:,2]),cost=sum(resources[:,3]))
        # addTemp = []
        # for x in self.resources:
        #     addTemp.append(x[3]/self.resourcesAge[3])
        # self.resources[0,-1] = np.array(addTemp)


    def info(self):

        for re in self.resources:
            print(re.sourcesName,re.price,re.number,re.cost,re.proprotion)
        for re in self.resourcesAge:
            print(re.sourcesName,re.price,re.number,re.cost,re.proprotion)





r1 = Resources('一档',50,1500,None)
r2 = Resources('二档',100,800,None)
r3 = Resources('三档',200,200,None)
r4 = Resources('四档',500,78,None)
r5 = Resources('五档',800,20,None)

sheet = ResourcesSheet()
sheet.setResourcesSheet(r1,r2,r3,r4,r5)
sheet.info()



