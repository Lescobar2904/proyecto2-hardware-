import numpy as np 
import matplotlib.pyplot as plt

FREQ_0 = 1000
FREQ_1 = 50 
SAMPLE = 441000
S_RATE = 44100.0


s_1 = [np.sin(2*np.pi * FREQ_0 * i/S_RATE) for i in range(SAMPLE)]
s_2 = [np.sin(2*np.pi * FREQ_1 * i/S_RATE) for i in range(SAMPLE)]
w_1 = np.array(s_1) 
w_2 = np.array(s_2)

w12 = w_1 + w_2


#--------------------------------------------------------------------
# FFT
#--------------------------------------------------------------------

fft_w1  = np.fft.fft(w_1)
fft_w2  = np.fft.fft(w_2)
fft_w12 = np.fft.fft(w12)

#print("1- ", int(len(fft_w12/2)))
#print("2- ", len(fft_w12/2))
#print("3- ", fft_w12/2)

#--------------------------------------------------------------------
# grafica
#--------------------------------------------------------------------

plt.figure(figsize=(10, 8))


# grafica 1

plt.subplot(4,1,1)
plt.plot(w_1[:500])
plt.title("Onda Original")
plt.xlabel("Numero de muestra")
plt.ylabel("amplitud")

# grafica 2

plt.subplot(4,1,2)
plt.plot(w_2[:4000])
plt.title("Onda ruido")
plt.xlabel("Numero de muestra")
plt.ylabel("amplitud")

# grafica 3

plt.subplot(4,1,3)
plt.plot(w12[:4000])
plt.title("Onda Original + Ruidosa")
plt.xlabel("Numero de muestra")
plt.ylabel("amplitud")

# grafica 4

plt.subplot(4,1,4)
plt.plot(np.abs(fft_w12)[:(int(len(fft_w12/2)))])
plt.title("Frecuencia de las Ondas (FFT)")
plt.xlabel("Numero de muestra")
plt.ylabel("amplitud")
plt.xlim(0,12000)

plt.tight_layout()
plt.show()

#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
