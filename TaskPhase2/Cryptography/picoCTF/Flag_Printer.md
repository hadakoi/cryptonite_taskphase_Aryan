# Flag Printer

## Method

```
I made a program to solve a problem, but it seems too slow :(
Download the program here.
Download the message here.
```

**Hint1:** ax^2 + bx + c

Ok upon getting the files we first look at the text file which seems to have a format of which seems to go on for nearly 1769611 lines. ;'(

Message
```
0 66
1 77611334
2 7296865972
3 6005985327
4 2768154539
5 3553732454
6 1992438015
7 538931207
8 3393488850
9 1014238907
10 5980514119
11 928281187
12 3328481670
```

Solve
```python
import galois
import numpy as np
MOD = 7514777789

points = []

for line in open('encoded.txt', 'r').read().strip().split('\n'):
    x, y = line.split(' ')
    points.append((int(x), int(y)))

GF = galois.GF(MOD)

matrix = []
solution = []
for point in points:
    x, y = point
    solution.append(GF(y % MOD))

    row = []
    for i in range(len(points)):
        row.append(GF((x ** i) % MOD))
    
    matrix.append(GF(row))

open('output.bmp', 'wb').write(bytearray(np.linalg.solve(GF(matrix), GF(solution)).tolist()[:-1]))
```

Now upon analysing the python script we understand that we are using a getting an output.bmp file at the end of all of this which most likely will contain our flag.

Now upon mapping the txt file and the solver code we can understand a few things ->

1. we are given a text file with 1769611 lines of pairs of integers **(xi, yi)** 
2. The python script loads the pair of points and tries to solve a linear system of equations using ``Vandermonde matrix`` that goes through **Ap=y**, A is the matrix, P is the vector of th ecoefficients and y is the vector of y values
3. Essentially what it is doing is each row of the matrix will look like this ``1 x0 x0^2 x0^3 ....`` and so on until n. Now these cofffecients of this polynomial are essentially components to the solution *p* given in the above equation. The script uses the np.linalg.solve() function to solve the entire system of equations simultaneously. This is essentially doing p(xi) = y(i) where it finds p for each point 
4. The results are then converted into a list which will give us a byte array of sorts with a graphical representation of the flag.

However there is just 1 big issue. This script is extremely infefficient as the Matrix contains nearly 3 x 10^12 elements which would be way to big. Now combine this with the complexity of the problem and its already going to take forever. I tried running the script for about an hour with no Luck.

Now luckily there are algorithims to compute coefficents when the **(xi, yi)** are given in pairs to us however even these will take to long.

Which is why we come to the method of Lagrange's Interpolation method.

This is where **yi** are known as the values at **xi**




The general formula for the Lagrange polynomial is:

Image1

**Li(x)** are the Lagrange basis polynomials, defined as

Image2

For each data point **(xi, yi)**, the Lagrange basis polynomial Li(x) is calculated. Then, the final polynomial P(x) is the weighted sum of these basis polynomials. Here's an example process: 

To calculate this Polynomial example
Let’s say we have three points: **(x_0, y_0) = (1, 2), (x_1, y_1) = (2, 3), (x_2, y_2) = (3, 5)**

Image3

Now looking online for a way to use these commands in sage we find the **fast_interpolate** command
```python
def _fast_interpolate(weights, tree):
    if len(tree) == 1:
        return weights[0]

    W1 = weights[:len(tree.left)]
    W2 = weights[len(tree.left):]

    r0 = _fast_interpolate(W1, tree.left)
    r1 = _fast_interpolate(W2, tree.right)

    return r0 * tree.right.poly + r1 * tree.left.poly

def fast_interpolate(X, Y):
    print("computing tree")
    tree = compTree(X)
    print("computing weights")
    weights = calcWeights(Y, tree)
    print("interpolating...")
    return _fast_interpolate(weights, tree)

def test():
    Xt = X[:10000]
    Yt = Y[:10000]

    f = fast_interpolate(Xt, Yt)
    for x, y in zip(Xt, Yt):
        assert f(x) == y

test()

f = fast_interpolate(X, Y)

open("output.bmp", "wb").write(bytearray(f.coefficients(sparse=False)[:-1]))
```

This effectively uses the **interpolate** function based on a recursive tree structure.

1. **_fast_interpolate(weights, tree):** This function recursively calculates the interpolation result by splitting the weights into two parts based on the tree structure. It computes the interpolation for the left and right subtrees and combines the results using a weighted sum, where each part is adjusted by a polynomial term.

It then outputs the coefficients for graphical reference.

2. **fast_interpolate(X, Y):** This function orchestrates the interpolation process. It first computes the tree structure (compTree(X)), calculates the interpolation weights (calcWeights(Y, tree)), and then uses _fast_interpolate to perform the recursive interpolation, ultimately returning the interpolated function f. 

3. Its then tested on 10000 lines of x and y. 

4. Then put to the real test

5. Finally it outputs a bmp file which we can view as an Image 

Why this is even a question idk give this to the mnc kids Pls

(I hate meths)

## Flag

> picoctf{i_do_hope_you_used_the_favorite_algorithm_of_every_engineering_student}