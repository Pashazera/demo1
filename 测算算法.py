import numpy as np
import copy

class Shop(object):
    def __init__(self,id,num_execution):
        self.id = id
        self.num_execution = num_execution #店铺执行频次 [2,3,3,2,2,2,6]
        self.classification = np.array([0,0,0])#店铺类别  [1,1,1]甲乙丙


    def set_num_execution(self,num_execution):
        self.num_execution=num_execution

class Label(object):
    def __init__(self,labels):
        self.labels = labels  #1 非  2 县级

    def get_true_labels(self):
        labels = self.labels
        tlabel = []
        for label in labels:
            tlabel.append(label[1])
        return tlabel

class Adminor(object):
    def __init__(self,task_diffs,resource,shops,times):

        self.task_diffs = task_diffs  #任务项 [3,3,2,2,1,1,1] 3 2 1 难中易 shape [1,N]
        self.resource = resource      #任务资源  [[3,3,2,2,1,1,1],[100,200,50,150,200,200,200]]  shape [2,N]
        self.shops = shops            #店铺数组
        self.packages = np.array([0,0,0])     #包数 shape[1,3] example [200,100,200]
        self.times = times        #到店次数 [ ]
        self.max_sum = np.array(None)      #限制执行总量  shape[1,N]

    def max_times(self,newshop):
        shops = newshop
        Max = []
        for shop in shops:
            num_execution = shop.num_execution
            m = num_execution[0]
            for i in range(len(num_execution)):
                if m < num_execution[i]:
                    m = num_execution[i]
            Max.append(m)
        return Max

    def get_labelTimes(self,newshop,labels):
        labels = labels
        tlabels = labels.get_true_labels()

        Max = self.max_times(newshop)
        m1,m0,t1,t0 = 0,0,0,0
        for i in range(len(tlabels)):
            if tlabels[i] == 1:
                t1 += 1
                m1 = max(m1,Max[i])
            else:
                t0 += 1
                m0 = max(m0,Max[i])

        return m1 * t1 , m0 * t0

    def is_end(self,X,Y):
        flag1 = True
        flag2 = True

        resource = X
        times = Y
        sum1 = 0
        for i in range(resource.shape[1]):
            sum1 += resource[1][i]
        if sum1 == 0:
            flag1 = False

        sum2 = 0
        for i in range(times.shape[1]):
            sum2 += times[1][i]
        if sum2 == 0:
            flag2 = False

        return flag1 and flag2

    def run(self):
        task_diffs = self.task_diffs
        resource = self.resource
        #packages = self.packages
        times = self.times
        shops = self.shops
        max_sum = self.max_sum

        for shop in shops:
            print(shop.num_execution)

        K = True
        m = 1
        while K :
            #循环执行
            for i in range(times.shape[1]):
                #取每家店
                temp = np.array([0,0,0])
                if times[1][i] > 0 :
                    #让能够到店的执行
                    shop = shops[i]
                    for j in range(resource.shape[1]):
                        if resource[1][j] > 0 and shop.num_execution[j] > 0:
                            resource[1][j] -= 1
                            shop.num_execution[j] -= 1
                            temp[resource[0][j]-1] += 1
                    times[1][i] -= 1
                    #甲乙丙
                    print("店铺",i,"第",m,"次")
                    a = temp[2]
                    b = temp[1]
                    c = temp[0]

                    if a > 0:
                        self.packages[0] += a
                        shop.classification[0] = 1

                    if b + c >= 3 and b >= 1 :
                        self.packages[1] += 1
                        shop.classification[1] = 1

                    else:
                        self.packages [2] += 1
                        shop.classification[2] = 1


            K = self.is_end(resource,times)
            m += 1

#店铺信息
shop1 = Shop(1,[2,4,3,7,6,7,8])
shop2 = Shop(2,[3,2,2,6,5,7,8])
shop3 = Shop(3,[6,5,6,6,6,6,8])
shop4 = Shop(4,[4,3,3,4,6,6,6])

#任务项难度,3 2 1 难中易
task_diffs = np.array([3,3,2,2,1,1,1])
resource = np.array([[3,3,2,2,1,1,1],[10,10,10,15,10,20,30]])
shops = np.array([shop1,shop2,shop3,shop4])
newshops = copy.deepcopy(shops)
times = np.array([[1,2,3,4],[4,4,5,5]])

adminor = Adminor(task_diffs,resource,newshops,times)

adminor.run()
print("[甲包,乙包,丙包]  :",adminor.packages)

a,b,c =0,0,0
for shop in newshops:
    print("第%d家店铺类型[甲,乙,丙]："%(shop.id),shop.classification)
    a += shop.classification[0]
    b += shop.classification[1]
    c += shop.classification[2]

print("甲店%d  \n乙店%d  \n丙店%d"%(a,b,c))

labels = Label(np.array([[1,1],[1,1],[0,1],[1,0]]))

x1,x2 =adminor.get_labelTimes(shops,labels)
print("非固定市店次数：",x1)
print("县级终端店次数：",x2)

