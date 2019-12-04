# starter code for solving knapsack problem using genetic algorithm

#mutasyon implementasyonu
import random
import math
fc = open('./c.txt', 'r')
fw = open('./w.txt', 'r')
fv = open('./v.txt', 'r')
fout = open('./out.txt', 'w')

values = [] #0 = choromosome, 1 = ft, 2 = wt
weight = []

c = int(fc.readline())
w = []
v = []
for line in fw:
    w.append(int(line))
for line in fv:
    v.append(int(line))
values = v
weight = w

print('Capacity :', c)
print('Weight :', w)
print('Value : ', v)

ftarr = []
wtarr = []
chromarr = []
wheel = []

 # the elements to replace our available elements in the population
expected_value = [1,0,1,0,1,0,1,1,1,0,0,0,0,1,1]


MutationProb = False;
Age = []

new_childs = []

popSize = int(input('Size of population : '))
genNumber = int(input('Max number of generation : '))
print('\nParent Selection\n---------------------------')
print('(1) Roulette-wheel Selection')
print('(2) K-Tournament Selection')
parentSelection = int(input('Which one? '))
if parentSelection == 2:
    k = int(input('k=? (between 1 and ' + str(len(w)) + ') '))

print('\nN-point Crossover\n---------------------------')
n = int(input('n=? (between 1 and ' + str(len(w) - 1) + ') '))

print('\nMutation Probability\n---------------------------')
mutProb = float(input('prob=? (between 0 and 1) '))#if randomnum < mutprob; then do it

print('\nMutation Probability\n---------------------------')
print('(1) Age-based Selection')
print('(2) Fitness-based Selection')
survivalSelection = int(input('Which one? '))
elitism = bool(input('Elitism? (Y or N) ' ))


def AgeBasedSelection(childs):
    #print("age based child sayısı:",childs)
    Values = v
    Weight = w
    #print("AGE: ",Age)
    for r in range(int(len(childs)/2)):
        enyasliIndexi = Age.index(max(Age))
        for o in range(len(Age)):
            Age[o] += 1
        population[enyasliIndexi] = childs[int(random.random()*len(childs))]
        Age[enyasliIndexi] = 0
        #print("yaşlar: ", Age)
        ####################################3
    FTxWT = []
    for i, chrom in enumerate(population):
        ft = 0
        wt = 0
        for j, gene in enumerate(chrom):
            ft += gene * Values[j]
            wt += gene * Weight[j]
        FTxWT.append(ft/wt)
    #print("new population ftxwt ",FTxWT)
    new_childs = []#when generation is generated, new childs will be fill out


def NaturalSelection(childs):#pop values,weight,childs
    Values = values
    #print("naturalselection gelen childs : ", childs)

    Weight = weight
    #print("çağırıldım")
    for i in range(int(len(childs)/2)):
        FTxWT = []#array of rate of child: ft/wt
        for i in range(len(childs)):
            oneChild = childs[i]
            ft = 0
            wt = 0
            for j, gene in enumerate(oneChild):
                ft += int(gene) * Values[j]
                wt += int(gene) * Weight[j]
            FTxWT.append(ft/wt)
       # most_significant_child = sorted(FTxWT , reverse= True)[:(int)(len(childs)/2)] #most significant genes will be sorted
        #for q in range(len(most_significant_child)):
         #   arri.append(FTxWT.index(most_significant_child[q]))




        myarr = []#keep original poplation's min index
        for i in range(len(population)):

            ft = 0
            wt = 0
            for j, gene in enumerate(population[i]):
                ft += int(gene) * Values[j]
                wt += int(gene) * Weight[j]
            myarr.append(ft/wt)

        konulacakOlanElemIndexi = FTxWT.index(max(FTxWT))

        degisecekolanElemanIndexi = myarr.index(min(myarr))

        population[degisecekolanElemanIndexi] =childs[konulacakOlanElemIndexi]

        #print("konulacak olan eleman in child : ", childs[konulacakOlanElemIndexi])
        #print("degiğşecek olan eleman in population : ", population[degisecekolanElemanIndexi])
        childs.pop(konulacakOlanElemIndexi)
    #print("new populatıon",population)#generasyon miktarı kadar dönecek make wheel full
    #yeni jenerasyon üretilmeden önce new childs arrayını boşalt

def Mutation(Mutation,childs):
    for x in range(len(childs)):
        mutasyona_ugrat = random.random()
        hangi_gen = int(random.random()*14)
        if(mutasyona_ugrat < Mutation):
            if(childs[x][hangi_gen] == 0):
                childs[x][hangi_gen] = 1
            else:
                childs[x][hangi_gen] = 0
            #parent selection


    if(survivalSelection == 1):
        AgeBasedSelection(childs)

    else:
        NaturalSelection(childs);



def CrossOver(parent1,parent2,n):#çiftleştirme
    #print("gelen parentler ", parent1,parent2)
    Values = values

    Weight =  weight
    secilenler=[]
    secildi = False
    child =[]
    #print("N değeri", n)
    i = 0
    b = 0
    while(i < n):#wdetermine which genes will be cross over
        a = int((random.random() * len(parent1)))
        b = a
        #print("A değerleri ", secilenler, "   :", a, "N değeri :", n)
        for x in range(len(secilenler)):
            if(a == secilenler[x]):
                secildi = True
        if(secildi):

            #print("secildi")
            secildi = False
        else:
            secilenler.append(a)
            i +=1
   # print("secilenler" ,secilenler)
    child = parent2
    zar3 = int(random.random() * len(population))

    for x in range(zar3):
        # zar at
        zar = int (random.random() *10) + 1
        zar2 = int (random.random() *10) + 1


        if(True):
            #print("parent 1 işeniyor, parent 2 ye akatarılacak")

            #print("parent 2", parent2)
            w = 0
            child[zar] = parent1[zar2]
            #population[zar3] = child
                #print("child", q ,"nuncu değer", parent1[q],"ile değiştirildi")
                #print("child =", child)
        else:
            pass;#print("parent 2 işleniyor")


        #print("our new child" ,child, ft, wt)
        #print("child which is made" , child)
        new_childs.append(child)# add the produced and used "cross over operation" to new_child array
    return new_childs







def make_wheel_full(n):
    yeni_childs = []
    #print("make wheel full")
    totalNum = 0
    fitness_elements = []

    for i in range(len(ftarr)):
        wheel.append(totalNum +(ftarr[i] /wtarr[i]))
        totalNum = totalNum + (ftarr[i] /wtarr[i])
        #print(ftarr[i] /wtarr[i])
    #print("Anan baban" ,roundWheel(totalNum))
   # print(wheel)
    for u in range(len(population)):
        for h in range(2):#parent selection
                fitness_elements.append(roundWheel(totalNum))# fitness elements is put in fitness elem array
                #print("fitness elems", fitness_elements)

        yeni_childs = CrossOver(fitness_elements[0],fitness_elements[1],n)#the produced child will be used "cross over" operation
       # print("our childss :", new_childs)
    #print("gönderilen childlar", new_childs)
    #print("yeni childss:" ,yeni_childs)
    Mutation(mutProb,yeni_childs)#

#wheel.append(totalPoint + (ft/wt))


def roundWheel(totalnum):# fitness elements


        a =random.random() * totalnum
        y=0
        #print("a = " , a)
       # a = random.randrange(0, totalnum)
        for i in range(len(wheel)):
            x = wheel[i]
            if (a > x):
                y+=1
                continue;
            break;
        return population[y]




def KTournament(k,crossovercount):
    Values = v
    Weight = w
    yeni_childs = []
    for y in range(len(population)):
        ciftlesecekolanElemeanlar = []

        for u in range(2):
            #print("selam")
            FTxWT=[]
            original_population = population
            secilen_elemanlar = []# k kadar eleman seçilir
            for x in range(k):
                abc =  int ((random.random()*len(population)))
                secilen_elemanlar.append(original_population[abc])


            for c in range(len(secilen_elemanlar)):
                my_elem = secilen_elemanlar[c]
                ft = 0
                wt = 0
                for j, gene in enumerate(my_elem):
                    ft += gene * Values[j]
                    wt += gene * Weight[j]
                FTxWT.append(ft/wt)
            endegerli_ft_wt = max(FTxWT)
            ciftlesecekolanElemeanlar.append(secilen_elemanlar[FTxWT.index(endegerli_ft_wt)])
       # print("ciftlesecekolanElemeanlar",ciftlesecekolanElemeanlar)
        yeni_childs = CrossOver(ciftlesecekolanElemeanlar[0],ciftlesecekolanElemeanlar[1],crossovercount)

    #print("new chids k tournement = ", yeni_childs)
    #NaturalSelection(new_childs) or

    Mutation(mutProb,yeni_childs)





print('\n----------------------------------------------------------')
print('initalizing population')
population = []
for i in range(popSize):
    temp = []
    for j in range(len(w)):
        temp.append(random.randint(0,1))
    population.append(temp)


print('evaluating fitnesses')
for i, chrom in enumerate(population):
    ft = 0
    wt = 0
    for j, gene in enumerate(chrom):
        ft += gene * v[j]
        wt += gene * w[j]
    ftarr.append(ft)
    wtarr.append(wt)
Deneme = v[1] +v[2] + v[4]+ v[6]+ v[8] +v[10]+v[11]+v[12]
##make_wheel_full(n)
print(ftarr , wtarr,wheel)

for x in range(len(population)):
    Age.append(0)
if(parentSelection == 1):
   for x in range(genNumber):
        make_wheel_full(n)
else:

    for q in range(genNumber):
        KTournament(k,n)


#KTournament(5,n)

##################################################################


print(population)

fout.write('chromosome: 101010111000011\n')
fout.write('weight: 749\n')
fout.write('value: 1458')
fout.close()
FTXWT =[]
for c in range(len(population)):
    my_elem = population[c]
    ft = 0
    wt = 0
    for j, gene in enumerate(my_elem):
        ft += gene * v[j]
        wt += gene * w[j]
    FTXWT.append(ft / wt)
endegerli_ft_wt = max(FTXWT)
element = population[FTXWT.index(endegerli_ft_wt)]
value = 0
weight = 0
#print("element == ",element)
for j, gene in enumerate(element):
    value += gene * v[j]
    weight += gene * w[j]
myelem = ""
for o in range(len(element)):
    myelem = myelem + str(element[o])

def Write():
    WriteObject = open("out.txt", "w")

    WriteObject.write(str(myelem)+"\n")
    WriteObject.write("weight:"+str(weight)+"\n")
    WriteObject.write('value:'+str(value)+"\n")

    WriteObject.close()

Write()
