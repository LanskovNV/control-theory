import numpy as np
import matplotlib.pyplot as plt
from control import lqr
from math import sqrt


q = 1 / 3
r = 1 / 9
w0 = 1.5
x0 = 1
v0 = 8

def p12(s):
    return r*w0**2 + s * sqrt(r**2 * w0**4 + r)

def p22(s):
    return s * sqrt(2*r*p12(s) + q*r)

def p11(s):
    return p12(s)*p22(s)/r - w0**2*p22(s)

def calculate_lqr():
    A = np.matrix([[0, 1], [w0**2, 0]])
    B = np.matrix([[0], [1]])
    Q = np.matrix([[1, 0], [0, q]])
    R = np.matrix([[r]])
    
    K, P, E = lqr(A, B, Q, R)
    print("K = ", K)
    print("P = ", P)

    x = np.matrix([[x0], [v0]])
    Jmin = x.transpose() * P * x
    print("Jmin = ", Jmin)

def calculate_p():
    s = 1
    P = np.matrix([[p11(s), p12(s)], [p12(s), p22(s)]])
    print(P)

if __name__ == "__main__":
    # calculate_lqr()
    calculate_p()