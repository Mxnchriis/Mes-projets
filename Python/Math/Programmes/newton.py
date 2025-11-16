# def f(x):
#     return x*x-4

# def derf(x):
#     return 2*x

def inter(f,derf,x2):
    return (-f(x2)/derf(x2)) + x2

GNBITER = 0

def newton(f,derf,x2,eps):
    global GNBITER
    x2m = x2
    xinter= x2m + 2 * eps
    while abs(x2m - xinter) > eps:
        x2m = x2
        xinter = inter(f,derf,x2)
        x2 = xinter
        GNBITER += 1
    print (f"La solution Newton serait {xinter} et a été itéré {GNBITER} fois\n")


# newton(f,derf,5,0.01)