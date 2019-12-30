import random
#a = 0, b = 1
import matplotlib.pyplot as plt

training_data =[]#[[8,8,0],[73,60,1],[18,18,0],[31,39,0],[60,80,1],[12,21,1],[73,85,1],[88,70,1]]#[[842,0,2.2,0,1,0,7,0.6,188,2,2,20,756,2549,9,7,19,0,0,1,1],[1021,1,0.5,1,0,1,53,0.7,136,3,6,905,1988,2631,17,3,7,1,1,0,2],[563,1,0.5,1,2,1,41,0.9,145,5,6,1263,1716,2603,11,2,9,1,1,0,2]]#attr x,attr y,label
test_data =[]#[[15,15,1],[5,5,0],[10,10,0],[18,60,0]]#[[594,0,0.8,0,2,1,28,0.1,132,5,3,1011,1263,3087,16,4,4,1,1,1,2]]

#################################################
##train
qwerty = 0
f = open("test.txt","r")
for line in f.readlines():
    if qwerty == 0:
        qwerty+=1
        continue;
    line1 = line.strip("\n").split(",")
    test_data.append(line1)
#############################################

qwerty = 0
f = open("train.txt","r")
for line2 in f.readlines():
    if qwerty == 0:
        qwerty+=1
        continue;
    line1 = line2.strip("\n").split(",")
    training_data.append(line1)


#############################################









clusterA = 0
clusterB = 1
clusterC = 2
clusterD = 3


keyList = []
AccuracyList = []
keys = 0
result_of_test_data = test_data[:]
result_of_test_data_index  = 0
oprs = 2
def Accuracy(resultofTestDATAindeX,result_oftest_data):
    global oprs


    accuracyArray = []
    #print(resultofTestDATAindeX)
    for p in range(resultofTestDATAindeX):

        if(int(result_oftest_data[p][-1])  == int(result_oftest_data[p][-oprs])):## son elemanı bizim bulduğumuz, bir önceki reel sonuç
            accuracyArray.append(True)
        else:
            accuracyArray.append(False)
    #calculating accurcy
    #print("yazdır",result_oftest_data[-1],result_oftest_data[-2])
    print("Accuracy = %",(accuracyArray.count(True)/len(accuracyArray))*100)
    global AccuracyList
    AccuracyList.append(accuracyArray.count(True)/len(accuracyArray)*100)
    global keys
    keys+=1
    keyList.append(keys)
    oprs+=1

def classify_Elements_Of_each_Test_data(HowManyClusterA,howManyClusterB,howManyClusterC, howManyClusterD):#one by one in test data
    countofclusters = []
    countofclusters.append(HowManyClusterA)
    countofclusters.append(howManyClusterB)
    countofclusters.append(howManyClusterC)
    countofclusters.append(howManyClusterD)

    #print("coc",max(countofclusters))
    global result_of_test_data_index
    global result_of_test_data
    if(max(countofclusters) ==HowManyClusterA):
        result_of_test_data[result_of_test_data_index].append(clusterA)
    elif(max(countofclusters) == howManyClusterB):
        result_of_test_data[result_of_test_data_index].append(clusterB)
    elif(max(countofclusters) == howManyClusterC):
        result_of_test_data[result_of_test_data_index].append(clusterC)
    elif(max(countofclusters) == howManyClusterD):
        result_of_test_data[result_of_test_data_index].append(clusterD)
    result_of_test_data_index +=1
    #print(result_of_test_dataH
    #print("a :", HowManyClusterA,"B =",howManyClusterB,"C =",howManyClusterC,"D =", howManyClusterD)
    if(result_of_test_data_index == len(result_of_test_data)):
        Accuracy(result_of_test_data_index,result_of_test_data)

def findClosestK_Element(k,closenessList):#one by one
    closenessList1 = closenessList[:]

    HowManyClusterA = 0
    howManyClusterB = 0
    howManyClusterC = 0
    howManyClusterD = 0


    for q in range(k):
        closenessIndex = closenessList1.index(min(closenessList1))#get index of closest element and pop it
        #print(training_data)
        if (int(training_data[closenessIndex][-1]) == clusterA):
            HowManyClusterA += 1
        elif int(training_data[closenessIndex][-1]) == clusterB:
            howManyClusterB += 1
        elif int(training_data[closenessIndex][-1]) == clusterC:
            howManyClusterC+=1
        elif int(training_data[closenessIndex][-1]) == clusterD:
            howManyClusterD+=1
        closenessList1.pop(closenessIndex)

    classify_Elements_Of_each_Test_data(HowManyClusterA,howManyClusterB,howManyClusterC,howManyClusterD)



def calculateSquare(num):
    return num*num

def calculateDistance(point1,point2):

    SOD = 0#sum of differences of dimenensions
    point1 = point1[:2]
    for i in range(len(point1)): # calculate sum of square of points.etc: ((x2-x1)**2) + ((y2-y2)**2) + ((z2-z1)**2)
       SOD = SOD +  calculateSquare(int(point1[i]) - int(point2[i]))
    #make some code
    return SOD**(1/2)



followLOT = 0
LOT  =len(test_data[0]) #lenght  of any element of test data

for ut in range(1,11):
    result_of_test_data = test_data[:]

    result_of_test_data_index = 0
    closenessList = []
    labelOfclosenessList = []
    result_of_test_data_index  = 0
    for x in range(len(test_data)):
            closenessList = []

            for y in range(len(training_data)):
                training_data1 = training_data[y][:-1]
                test_data1 = test_data[x][:-ut]

                closenessList.append(calculateDistance(test_data1,training_data1))
                labelOfclosenessList.append(training_data[y][-1])
                test_data1.pop(len(test_data1) -1)
                training_data1.pop(len(training_data1)- 1)
            #print(closenessList)

            findClosestK_Element(ut,closenessList)
                #print(closenessList)
                #print("labelOfclosenessList",labelOfclosenessList)
            labelOfclosenessList = []
            if  x == len(test_data) -1 :
                pass;







# importing the required module


# plotting the points

plt.plot(keyList, AccuracyList, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)

# naming the x axis
plt.xlabel('Key Value')
# naming the y axis
plt.ylabel('Accuracy')

# giving a title to my graph
plt.title('PROJECT 4')

# function to show the plot
plt.show()

