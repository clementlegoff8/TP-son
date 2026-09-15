# TP : un peu de musique ###################################################################################################

import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio,display
from scipy.io import wavfile

RATE = 44_100
LA = 440
DO = 523.25

# Génération d'une sinusoïde ##################################################################################################

#1. Il faut 44100 échantillons pour 1 seconde
#2. x(t) = sin(2π(phi)t)
#3.

temps = np.linspace(0,1,44100)
position = np.sin(np.multiply(temps,2*np.pi*440))
plt.plot(temps[:int(44100*0.05)],position[:int(44100*0.05)])
plt.show()

#4.

def display_signal(signal,rate=RATE,title="Signal",width=1):
    pass