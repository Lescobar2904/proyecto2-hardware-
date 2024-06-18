import numpy as np
import matplotlib.pyplot as plt


FREQ_0 = 9000
FREQ_1 = 5000
FREQ_2 = 100

SAMPLE = 20000
S_RATE = 20000.0

nMAX = 20000

# Ondas 
aW = [
      [2*np.sin((2*np.pi) * FREQ_0 * (i/S_RATE)) for i in range(SAMPLE)],
      [3*np.sin((2*np.pi) * FREQ_1 * (i/S_RATE)) for i in range(SAMPLE)],
      [9*np.sin((2*np.pi) * FREQ_2 * (i/S_RATE)) for i in range(SAMPLE)]
     ]
#señales
aS = [
      np.array(aW[0]) + np.array(aW[1]),
      np.array(aW[0]) + np.array(aW[2]),
      np.array(aW[1]) * np.array(aW[2])
     ]

def Filter_Comp(aV,nA):
    aF = np.zeros(len(aV)) #arreglo aF se completa con 0s del tamaño de aV
    #aF = aV
    for i in range(1,nMAX):
        aF[i] = nA * aV[i] + (1.0 - nA) * aF[i - 1]
    return aF



#--------------------------------------------------------------------
# grafica
#--------------------------------------------------------------------

plt.figure(figsize=(10,6))

# grafica 1

plt.subplot(3,1,1)
plt.plot(Filter_Comp(aS[0], 0.1)[:200], label = 'señal 1 filtrada',
color="red")
plt.plot(aS[0][:200], label = 'señal 1 original')
plt.title('señales filtradas y originales')
plt.legend()


# grafica 2

plt.subplot(3,1,2)
plt.plot(aS[1][:200], label = 'señal 2 original')
plt.plot(Filter_Comp(aS[1], 0.5)[:200], label = 'señal 2 filtrada'
,color="red")
plt.title('hola')
plt.legend()

# grafica 3

plt.subplot(3,1,3)
plt.plot(aS[2][:200], label = 'señal 3 original')
plt.plot(Filter_Comp(aS[2],0.1)[:200], label = 'señal 3 filtrada',
color="red")
plt.title('hola')
plt.legend()


#--------------------------------------------------------------------
#--------------------------------------------------------------------

plt.tight_layout()
plt.show()


#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------








