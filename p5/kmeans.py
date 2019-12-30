
import matplotlib.pyplot as plt
import random

f = open("data.txt","r")
r = f.readlines()
array = []
xKoord = []
yKoord=[]
q = 0
for x in r:
    if q == 0:
        q += 1
        continue;

    p = x.strip("\n").split(",")
    xKoord.append(int(p[0]))
    yKoord.append(int(p[1]))

N = 0
x = xKoord

y = yKoord

randomx = []
randomy = []
cluster1x=[]
cluster1y = []
cluster2x = []
cluster2y =[]
cluster3x = []
cluster3y = []
cluster4x = []
cluster4y = []
cluster5x = []
cluster5y=[]

size_degisti = True

cluster1_onceki_size = len(cluster1x)
cluster2_onceki_size = len(cluster2x)
cluster3_onceki_size = len(cluster3x)
cluster4_onceki_size = len(cluster4x)
cluster5_onceki_size = len(cluster5x)
def calculateSquare(num):
    return num*num
def distance(point1,point2):
    SOD = 0  # sum of differences of dimenensions

    for i in range(len(point1)):  # calculate sum of square of points.etc: ((x2-x1)**2) + ((y2-y2)**2) + ((z2-z1)**2)
        SOD = SOD + calculateSquare(int(point1[i]) - int(point2[i]))
    # make some code
    return SOD ** (1 / 2)



def MEAN_BUL():
    total_for_cluster1x = 0
    total_for_cluster1y = 0
    mean_for_cluster1x = 0
    mean_for_cluster1y = 0
    for q in range(len(cluster1x)):
        total_for_cluster1x = total_for_cluster1x + cluster1x[q]
        total_for_cluster1y = total_for_cluster1y + cluster1y[q]

    mean_for_cluster1x = total_for_cluster1x/len(cluster1x)
    mean_for_cluster1y = total_for_cluster1y/len(cluster1y)
    randomx[0] = mean_for_cluster1x
    randomy[0] = mean_for_cluster1y


    ################################
    if(cluster2x != 0):
        total_for_cluster2x = 0
        total_for_cluster2y = 0
        mean_for_cluster2x = 0
        mean_for_cluster2y = 0
        for q in range(len(cluster2x)):
            total_for_cluster2x = total_for_cluster2x + cluster2x[q]
            total_for_cluster2y = total_for_cluster2y + cluster2y[q]

        mean_for_cluster2x = total_for_cluster2x / len(cluster2x)
        mean_for_cluster2y = total_for_cluster2y / len(cluster2y)
        randomx[1] = mean_for_cluster2x
        randomy[1] = mean_for_cluster2y
#############################################3
    if(len(randomy) >=3 and len(cluster3y) != 0):
        total_for_cluster3x = 0
        total_for_cluster3y = 0
        mean_for_cluster3x = 0
        mean_for_cluster3y = 0
        for q in range(len(cluster3x)):
            total_for_cluster3x = total_for_cluster3x + cluster3x[q]
            total_for_cluster3y = total_for_cluster3y + cluster3y[q]

        mean_for_cluster3x = total_for_cluster3x / len(cluster3x)
        mean_for_cluster3y = total_for_cluster3y / len(cluster3y)
        randomx[2] = mean_for_cluster3x
        randomy[2] = mean_for_cluster3y
#############################################3
    if(len(randomy) >=4 and len(cluster4y) != 0):
        total_for_cluster4x = 0
        total_for_cluster4y = 0
        mean_for_cluster4x = 0
        mean_for_cluster4y = 0
        for q in range(len(cluster4x)):
            total_for_cluster4x = total_for_cluster4x + cluster4x[q]
            total_for_cluster4y = total_for_cluster4y + cluster4y[q]

        mean_for_cluster4x = total_for_cluster4x / len(cluster4x)
        mean_for_cluster4y = total_for_cluster4y / len(cluster4y)
        randomx[3] = mean_for_cluster4x
        randomy[3] = mean_for_cluster4y
#############################################3

    if(len(randomy) >= 5):
        total_for_cluster5x = 0
        total_for_cluster5y = 0
        mean_for_cluster5x = 0
        mean_for_cluster5y = 0
        for q in range(len(cluster5x)):
            total_for_cluster5x = total_for_cluster5x + cluster5x[q]
            total_for_cluster5y = total_for_cluster5y + cluster5y[q]

        mean_for_cluster5x = total_for_cluster5x / len(cluster5x)
        mean_for_cluster5y = total_for_cluster5y / len(cluster5y)
        randomx[4] = mean_for_cluster5x
        randomy[4] = mean_for_cluster5y


def SINIFLANDIR_BAKALIM(mesafeler):
    global  N
    minimum_mesafe_indexi = mesafeler.index(min(mesafeler))
    if minimum_mesafe_indexi ==0:
        cluster1x.append(x[N])
        cluster1y.append(y[N])
    if minimum_mesafe_indexi == 1:
        cluster2x.append(x[N])
        cluster2y.append(y[N])
    if minimum_mesafe_indexi == 2:
        cluster3x.append(x[N])
        cluster3y.append(y[N])
    if minimum_mesafe_indexi == 3:
        cluster4x.append(x[N])
        cluster4y.append(y[N])
    if minimum_mesafe_indexi == 4:
        cluster5x.append(x[N])
        cluster5y.append(y[N])
    N+=1


def hesapala_bakalım():
    global cluster5_onceki_size
    global cluster4_onceki_size
    global cluster3_onceki_size
    global cluster2_onceki_size
    global cluster1_onceki_size
    global cluster5x
    global cluster4x
    global cluster3x
    global cluster2x
    global cluster1x
    global cluster5y
    global cluster4y
    global cluster3y
    global cluster2y
    global cluster1y
    global N
    distances = []

    for t in range(len(x)):
        point2 = []
        point2.append(x[t])
        point2.append(y[t])
        for u in range(len(randomy)):
            point1 = []
            point1.append(randomx[u])
            point1.append(randomy[u])
            distances.append(distance(point1,point2))
        SINIFLANDIR_BAKALIM(distances)
        distances =[]
    MEAN_BUL()

    if(cluster1_onceki_size != len(cluster1x) ):
        cluster1_onceki_size = len(cluster1x)
        cluster2_onceki_size = len(cluster2x)
        cluster3_onceki_size = len(cluster3x)
        cluster4_onceki_size = len(cluster4x)
        cluster5_onceki_size = len(cluster5x)

        cluster1x = []
        cluster1y = []
        cluster2x = []
        cluster2y = []
        cluster3x = []
        cluster3y = []
        cluster4x = []
        cluster4y = []
        cluster5x = []
        cluster5y = []
        N = 0
        size_degisti = True

        hesapala_bakalım()
    else:
        size_degisti = False

    if size_degisti == False:
        return 0;






def random_belirle(k):


    for u in range(k):
        myrandomx = random.randrange(int(min(xKoord)),int(max(xKoord)))
        myrandomy = random.randrange(int(min(yKoord)),150)
        randomx.append(myrandomx)
        randomy.append(myrandomy)

    hesapala_bakalım()

random_belirle(5)#enter value k
plt.scatter(cluster1x,cluster1y,c="brown")
plt.scatter(cluster2x,cluster2y,c = "purple")
plt.scatter(cluster3x,cluster3y,c = "black")
plt.scatter(cluster4x,cluster4y,c="teal")
plt.scatter(cluster5x,cluster5y,c="green")

plt.scatter(randomx, randomy, c="yellow",marker=(5,2))
plt.tick_params(axis='x', which='major', labelsize=10)
plt.tick_params(axis='y', which='major', labelsize=10)
plt.title("PROJECT 5")

plt.show()


