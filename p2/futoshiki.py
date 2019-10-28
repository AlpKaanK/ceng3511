from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ortools.sat.python import cp_model
import re
import sys
Concatenated = []
ArrEquality = []
ArrUneq = []
with open(sys.argv[1], 'r') as dosya:
    Reader = dosya.read()
    mantar = Reader.split()
    for x in range(len(mantar)):
        Find = re.findall(("[^,]"), mantar[x])
        if(len(Find) == 2):
            Concatenated.append(str(Find[0]) + str(Find[1]))
        else:
            ArrEquality.append(Find[0])

def SimpleSatProgram():
    """Minimal CP-SAT example to showcase calling the solver."""
    # Creates the model.

    model = cp_model.CpModel()

    # Creates the variables.
    num_vals = 5
    A1 = model.NewIntVar(1, num_vals - 1, 'A1')
    A2 = model.NewIntVar(1, num_vals - 1, 'A2')
    A3 = model.NewIntVar(1, num_vals - 1, 'A3')
    A4 = model.NewIntVar(1, num_vals - 1, 'A4')

    B1 = model.NewIntVar(1, num_vals - 1, 'B1')
    B2 = model.NewIntVar(1, num_vals - 1, 'B2')
    B3= model.NewIntVar(1, num_vals - 1, 'B3')
    B4= model.NewIntVar(1, num_vals - 1, 'B4')

    C1 = model.NewIntVar(1, num_vals - 1, 'C1')
    C2 = model.NewIntVar(1, num_vals - 1, 'C2')
    C3 = model.NewIntVar(1, num_vals - 1, 'C3')
    C4 = model.NewIntVar(1, num_vals - 1, 'C4')


    D1 = model.NewIntVar(1, num_vals - 1, 'D1')
    D2 = model.NewIntVar(1, num_vals - 1, 'D2')
    D3 = model.NewIntVar(1, num_vals - 1, 'D3')
    D4 = model.NewIntVar(1, num_vals - 1, 'D4')


    # Creates the constraints.
    model.Add(B1 != B2)
    model.Add(B1 != B3)
    model.Add(B2 != B3)
    model.Add(B1 != B4)
    model.Add(B2 != B4)
    model.Add(B4 != B3)



    model.Add(A1 != A2)
    model.Add(A1 != A3)
    model.Add(A2 != A3)
    model.Add(A1 != A4)
    model.Add(A2 != A4)
    model.Add(A4 != A3)



    model.Add(C1 != C3)
    model.Add(C2 != C3)
    model.Add(C1 != C2)
    model.Add(C1 != C4)
    model.Add(C3 != C4)
    model.Add(C2 != C4)

    model.Add(D1 != D2)
    model.Add(D1 != D3)
    model.Add(D1 != D4)
    model.Add(D2 != D3)
    model.Add(D2 != D4)
    model.Add(D3 != D4)













    model.Add(A1 != B1)
    model.Add(A1 != C1)
    model.Add(A1 != D1)
    model.Add(B1 != C1)
    model.Add(B1 != D1)
    model.Add(D1 != C1)

    model.Add(A2 != B2)
    model.Add(A2 != C2)
    model.Add(A2 != D2)
    model.Add(B2 != C2)
    model.Add(B2 != D2)
    model.Add(D2 != C2)

    model.Add(A3 != B3)
    model.Add(A3 != C3)
    model.Add(A3 != D3)
    model.Add(B3 != C3)
    model.Add(B3 != D3)
    model.Add(D3 != C3)

    model.Add(A4 != B4)
    model.Add(A4 != C4)
    model.Add(A4 != D4)
    model.Add(B4 != C4)
    model.Add(B4 != D4)
    model.Add(D4 != C4)


    myArr =[]
    myArr.append(A1)
    myArr.append(A2)
    myArr.append(A3)
    myArr.append(A4)

    myArr.append(B1)
    myArr.append(B2)
    myArr.append(B3)
    myArr.append(B4)

    myArr.append(C1)
    myArr.append(C2)
    myArr.append(C3)
    myArr.append(C4)

    myArr.append(D1)
    myArr.append(D2)
    myArr.append(D3)
    myArr.append(D4)
    indexleri = []
    #print("Conc" ,Concatenated)
    #print(len(Concatenated), len(ArrEquality))
    for u in range(len(Concatenated) -len(ArrEquality)):
        for i in range(16):
            if(str(Concatenated[u+len(ArrEquality)]) == str(myArr[i])):
                #print("bu d0rü",myArr[i], i)
                indexleri.append(i)

    #print(indexleri)


    k = 0;
    while(k < len(indexleri) - 1):
        model.Add(myArr[indexleri[k]] > myArr[indexleri[k + 1]])
       # print(myArr[indexleri[k]], myArr[indexleri[k + 1]])
        k= k +2;






   # print(len(ArrEquality))
    cindexleri = []
    cindexlerinEsitlikleri = []
    for u in range(len(ArrEquality)):
        for i in range(16):
            if(str(Concatenated[u]) == str(myArr[i])):
                cindexleri.append(i)
                cindexlerinEsitlikleri.append(ArrEquality[u])

    for h in range(len(cindexlerinEsitlikleri)):
        model.Add(myArr[cindexleri[h]] == int(cindexlerinEsitlikleri[h]))





    # Creates a solver and solves the model.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE:
        print (str(solver.Value(A1))+","+str(solver.Value(A2))+","+ str(solver.Value(A3))+","+ str(solver.Value(A4)))
        print (str(solver.Value(B1))+"," +str(solver.Value(B2))+","+ str(solver.Value(B3))+ "," +str(solver.Value(B4)))
        print (str(solver.Value(C1))+"," + str(solver.Value(C2))+"," +str(solver.Value(C3))+"," +str(solver.Value(C4)))
        print(str(solver.Value(D1))+"," +str(solver.Value(D2))+"," +str(solver.Value(D3))+","+ str(solver.Value(D4)))



    def write():
        WriteObject = open("futoshiki_output.txt", "w+")

        WriteObject.write(str(solver.Value(A1))+","+str(solver.Value(A2))+","+
                          str(solver.Value(A3))+","+ str(solver.Value(A4)) + "\n")

        WriteObject.write(str(solver.Value(B1)) + "," + str(solver.Value(B2)) + "," +
                          str(solver.Value(B3)) + "," + str(solver.Value(B4))  + "\n")

        WriteObject.write(str(solver.Value(C1)) + "," + str(solver.Value(C2)) + "," +
                          str(solver.Value(C3)) + "," + str(solver.Value(C4)) + "\n")

        WriteObject.write(str(solver.Value(D1)) + "," + str(solver.Value(D2)) + "," +
                          str(solver.Value(D3)) + "," + str(solver.Value(D4))  + "\n")


        WriteObject.close()
    write()

SimpleSatProgram()



