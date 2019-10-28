from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ortools.sat.python import cp_model
import re
import sys

ArrVertical = []
ArrHorizontal = []
with open(sys.argv[1], 'r') as dosya:
    Reader = dosya.read()
    Find = re.findall("\d+",Reader)
    for i in range(6):
        if i < 3:
            ArrVertical.append(int(Find[i]))
        else:
            ArrHorizontal.append(int(Find[i]))


def SimpleSatProgram():
    """Minimal CP-SAT example to showcase calling the solver."""
    # Creates the model.
    f = 7
    model = cp_model.CpModel()

    # Creates the variables.
    num_vals = 10
    x1 = model.NewIntVar(1, num_vals - 1, 'x1')
    x2 = model.NewIntVar(1, num_vals - 1, 'x2')
    x3 = model.NewIntVar(1, num_vals - 1, 'x3')

    y1 = model.NewIntVar(1, num_vals - 1, 'y1')
    y2 = model.NewIntVar(1, num_vals - 1, 'y2')
    y3= model.NewIntVar(1, num_vals - 1, 'y3')

    z1 = model.NewIntVar(1, num_vals - 1, 'z1')
    z2 = model.NewIntVar(1, num_vals - 1, 'z2')
    z3 = model.NewIntVar(1, num_vals - 1, 'z3')


    # Creates the constraints.
    model.Add(y1 != y2)
    model.Add(y1 != y3)
    model.Add(y2 != y3)

    model.Add(x1 != x2)
    model.Add(x1 != x3)
    model.Add(x2 != x3)

    model.Add(z1 != z3)
    model.Add(z2 != z3)
    model.Add(z1 != z2)


    model.Add(x1 != y1)
    model.Add(x1 != z1)
    model.Add(y1 != z1)

    model.Add(x2 != y2)
    model.Add(y2 != z2)
    model.Add(z2 != x2)

    model.Add(z3 != x3)
    model.Add(x3 != y3)
    model.Add(y3 != z3)













    model.Add(x1 + x2+ x3 ==  ArrHorizontal[0])
    model.Add(y1 + y2+ y3 == ArrHorizontal[1])
    model.Add(z1 + z2+ z3 == ArrHorizontal[2])

    model.Add(x1 + y1 + z1 == ArrVertical[0])
    model.Add(x2 + y2+ z2 == ArrVertical[1])
    model.Add(x3 + y3+ z3 == ArrVertical[2])









   # model.Maximize(x + 2 * y + 3 * z)

    # Creates a solver and solves the model.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE:

        print("x" , ArrVertical[0],ArrVertical[1],ArrVertical[2])
        print(ArrHorizontal[0],solver.Value(x1),solver.Value(x2),solver.Value(x3))
        print(ArrHorizontal[1],solver.Value(y1), solver.Value(y2), solver.Value(y3))
        print(ArrHorizontal[2],solver.Value(z1), solver.Value(z2), solver.Value(z3))

    def Write():
        WriteObject = open("kakuro_output.txt", "w+")

        WriteObject.write("x," + str(ArrVertical[0]) + "," + str(ArrVertical[1]) + "," + str(ArrVertical[2]) + "\n")
        WriteObject.write(str(ArrHorizontal[0]) + "," + str(solver.Value(x1)) + "," + str(solver.Value(x2)) + "," + str(
            solver.Value(x3))+"\n")

        WriteObject.write(str(ArrHorizontal[1]) + "," + str(solver.Value(y1)) + "," + str(solver.Value(y2)) + "," +
                          str(solver.Value(y3)) + "\n")

        WriteObject.write(str(ArrHorizontal[2]) + "," + str(solver.Value(z1)) + "," + str(solver.Value(z2)) +","+
                          str(solver.Value(z3)) + "\n")
        WriteObject.close()

    Write()


SimpleSatProgram()



