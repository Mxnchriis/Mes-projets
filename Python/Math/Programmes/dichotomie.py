# def f(x):
#     return x*x-4

iteration = 0
gX1 = 0
gX2 = 0

def dichotomie(f, x1, x2, epsilon):
    global iteration, gX1, gX2
    while abs(x2 - x1) > epsilon:
        xm = (x1 + x2)/2
        if f(x1) * f(xm) <= 0:
            x2 = xm
            iteration+=1
        else:
            x1 = xm
            iteration+=1
        return x1, x2, (x1+x2)/2, iteration


# dichotomie(f, 0, 5, 0.01)