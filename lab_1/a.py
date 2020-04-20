import numpy as np
import matplotlib.pyplot as plt
from math import atan, pi, sqrt


K = 0.75
w0 = 3
T1 = 0.01
T2 = 0.06
T3 = 0.03

def calc_det3():
    a3 = np.array([[0.09,   0.81,   0.75], \
                   [0.0018, 1.0162, 9.09], \
                   [0,      0.09,   0.81]])

    print(np.linalg.det(a3))

def mihailow():
    def Re(w):
        return K + T2 * w ** 4 - T2 * w0 ** 2 * w ** 2 + T3 * w ** 4 - T3 * w0 ** 2 * w ** 2    

    def Im(w):
        return K * T1 * w + T2 * T3 * w ** 5 - T2 * T3 * w0 ** 2 * w ** 3 - w ** 3 + w * w0 ** 2
        

    W3 = np.arange(0, 3.4, 0.001)
    W2 = np.arange(0, 1e3, 1) 

    W1 = np.arange(0, 1e9 + 1, 1e9)
    x1, y1 = Re(W1), Im(W1)
    delta = atan(y1[1] / x1[1]) - atan(y1[0] / x1[0])

    fig, (ax1, ax2) = plt.subplots(1, 2)
    plt.suptitle("delta(arg(jw)) = " + str(delta) + "\n" + "pi/2 = " + str(pi / 2))
    
    ax1.plot(Re(W3), Im(W3))
    ax2.plot(Re(W2), Im(W2))
    
    ax1.set_title("w from 0 to 3.4")
    ax1.grid()
    ax1.set_xlabel("Re(jw)")
    ax1.set_ylabel("Im(jw)")

    ax2.set_title("w from 0 to inf")
    ax2.grid()
    ax2.set_xlabel("Re(jw)")
    ax2.set_ylabel("Im(jw)")

    plt.show()

def nikvist():
    def ksi(w):
        i = 1j
        return 1 + K*(1 + T1*w*i) / (i*w*(w0*2-w*2)*(T2*i*w + 1)*(T3*i*w + 1))

    W = np.arange(0, 3.5, 0.01) 

    X = [ksi(x).real for x in W]
    Y = [ksi(x).imag for x in W]

    plt.grid()
    plt.plot(X, Y)
    plt.xlabel("Re(jw)")
    plt.ylabel("Im(jw)")
    plt.scatter(-1, 0, s=50, c='r')
    plt.show()

if __name__ == "__main__":
    calc_det3()
    # mihailow()
    # nikvist()
