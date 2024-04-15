import numpy as np
import matplotlib.pyplot as plt

def fft(x):
    N = len(x)

    if (N <= 1): # verificar o comprimento 
        return x
        
    else:
        Wn = np.exp(-2j * np.pi * np.arange(N//2) / N)
        par = fft(x[0::2])
        impar = fft(x[1::2])

    # Caso para N = 2
    #X(0) = G(h) + Wn*H(h)
    #x(1) = G(h) - Wn*H(h)
    
    return np.concatenate([par + Wn * impar, par - Wn * impar])

def func(n):
    return np.cos(2*np.pi*n/10)

NFFT = 128
k = np.arange(0, NFFT)
signal = fft(func(k))

figure, ax = plt.subplots(3,1,figsize=(20,18))
ax[0].stem(k, func(k), label = 'x(n)') ## sinal amostrado
ax[0].grid(True)
ax[0].set_xlabel('n')
ax[0].legend(loc = 'upper right')

ax[1].stem(k, abs(signal))
ax[1].grid(True)
ax[1].set_xlabel('k')
ax[1].set_ylabel('FFT AMPLITUDE')

ax[2].plot(k, np.angle(signal))
ax[2].grid(True)
ax[2].set_xlabel('k')
ax[2].set_ylabel('PHASE')
