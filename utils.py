import numpy as np
from scipy import integrate # kwadratura adaptacyjna, Gaussa, Romberga

def k(x):
    if x <= 1:
        return 1
    return 2
#funkcje kształtu dla i-tego elementu skończonego w punkcie x 
# i to indes elementu skończonego
# x to pozycja w przestrzeni
# h to długość elementu skończonego
def e(i, x):
    if x < h * (i - 1) or x > h * (i + 1):
        return 0
    if x < h * i:
        return x / h - i + 1
    return - x / h + i + 1

def e_prim(i, x):
    if x < h * (i - 1) or x > h * (i + 1):
        return 0
    if x < h * i:
        return 1 / h
    return -1 / h

# wartość całki z iloczynu pochodnych funkcji kształtu i-tego i j-tego elementu skończonego w zakresie od s do z.
def B(i, j, s, z):       
    return integrate.quad(lambda x: k(x) * e_prim(i, x) * e_prim(j, x), s, z)[0] - e(i, 0) * e(j, 0)

def L(i):
    return - 20 * e(i, 0)

# abs(i - j) > 1 to elementy skończone nie sąsiadują ze sobą (zbyt daleko od siebie) więc element macierzy równy 0
# abs(i - j) == 1 to elementy skończone sąsiadują ze sobą więc przedziały są wyznaczane tak, aby uwzględniały obszar, na który te dwa elemmenty sie nakładają
# abs(i - j) == 0 ten sam element, przedziały są wyznaczane tak, aby objęły cały obszar tego elementu

def create_A():
    matrix = [
        [
            0 if abs(i - j) > 1 else B(i, j, 2. * max(0, min(i, j) / elem_num), 2. * min(1, max(i, j) / elem_num))
            if abs(i - j) == 1 else B(i, j, 2. * max(0, (i - 1) / elem_num), 2. * min(1, (i + 1) / elem_num))
            for j in range(elem_num)
        ]
        for i in range(elem_num)
    ]

    return matrix

def create_B():
    matrix = []
    for i in range(elem_num):
        matrix.append(L(i))
    return matrix

def solve(n):
    global elem_num
    global h
    elem_num = n
    h = 2 / elem_num

    a = np.array(create_A())
    b = np.array(create_B())

    x = [h * i for i in range(elem_num + 1)]
    y = np.append(np.linalg.solve(a, b), 0)
    

    return (x, y)
